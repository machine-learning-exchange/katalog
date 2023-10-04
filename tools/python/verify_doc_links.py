#!/usr/bin/env python3

# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0

import concurrent.futures
import itertools
import re
import requests

from glob import glob
from os import environ as env
from os.path import abspath, dirname, exists, relpath
from random import randint
from time import sleep
from urllib3.util.url import parse_url
from urllib3.exceptions import LocationParseError


GITHUB_REPO = env.get("GITHUB_REPO", "https://github.com/machine-learning-exchange/katalog/")

md_file_path_expressions = [
    "/**/*.yaml",
    "/**/*.md",
]

excluded_paths = [
    "tools",
    "temp",
]

url_excludes = ["localhost", "...", "lorem", "ipsum", "/path/to/",
                "/user/repository/branch", "address", "port"]

script_folder = abspath(dirname(__file__))
project_root_dir = abspath(dirname(dirname(script_folder)))
github_repo_master_path = "{}/blob/master".format(GITHUB_REPO.rstrip("/"))

parallel_requests = 60  # GitHub rate limiting is 60 requests per minute, then we sleep a bit

url_status_cache = dict()


def find_md_files() -> [str]:

    print("Checking for Markdown files here:\n")
    for path_expr in md_file_path_expressions:
        print("  " + path_expr.lstrip("/"))
    print("")

    list_of_lists = [glob(project_root_dir + path_expr, recursive=True)
                     for path_expr in md_file_path_expressions]

    flattened_list = list(itertools.chain(*list_of_lists))

    filtered_list = [path for path in flattened_list
                     if not any(s in path for s in excluded_paths)]

    return sorted(filtered_list)


def get_links_from_file_content(file_path: str) -> [(int, str, str)]: # -> [(line, link_text, URL)]

    with open(file_path, "r") as f:
        file_content = f.read()

    folder = relpath(dirname(file_path), project_root_dir)

    # replace relative links that are siblings to the README, i.e. [link text](FEATURES.md)
    if file_path.endswith(".md"):
        file_content = re.sub(
            r"\[([^]]+)\]\((?!http|#|/)([^)]+)\)",
            r"[\1]({}/{}/\2)".format(github_repo_master_path, folder).replace("/./", "/"),
            file_content)

    # replace links that are relative to the project root, i.e. [link text](/sdk/FEATURES.md)
    if file_path.endswith(".md"):
        file_content = re.sub(
            r"\[([^]]+)\]\(/([^)]+)\)",
            r"[\1]({}/\2)".format(github_repo_master_path),
            file_content)

    # return completed links
    line_text_url = []
    for line_number, line_text in enumerate(file_content.splitlines()):

        all_urls_in_this_line = set()

        # find markdown-styled links [text](url)
        for (link_text, url) in re.findall(r"\[([^]]+)\]\((%s[^)]+)\)" % "http", line_text):
            line_text_url.append((line_number + 1, link_text, url))
            all_urls_in_this_line.add(url)

        # find plain http(s)-style links
        for url in re.findall(r"https?://[a-zA-Z0-9./?=_&%${}<>:-]+", line_text):
            if url not in all_urls_in_this_line \
                    and not any(s in url for s in url_excludes):
                try:
                    url = str(url).rstrip(".")  # if URL is last word in a sentence ending with a dot "."
                    parse_url(url)
                    line_text_url.append((line_number + 1, "", url))
                except LocationParseError:
                    pass

    # return completed links
    return line_text_url


def test_ibm_developer_url(url):
    content_apis = ["https://developer.ibm.com/middleware/v1/contents/static",
                    "https://developer.ibm.com/middleware/v1/contents"]

    url = url.replace("exchanges/data/all", "data")
    path = parse_url(url).path
    status = 404

    if path:
        for api_base_url in content_apis:
            api_url = api_base_url + path
            try:
                resp = requests.get(api_url.rstrip("/"), timeout=5)
                status = resp.json()["code"]
                if status == 200:
                    break
                else:
                    status = 404
            except requests.exceptions.RequestException as e:
                print(f"Error test_ibm_developer_url({url}): {e}")
                status = 500
    else:
        status = requests.head(url, timeout=5).status_code

    return status


def test_url(file: str, line: int, text: str, url: str) -> (str, int, str, str, int):  # (file, line, text, url, status)

    short_url = url.split("#", maxsplit=1)[0]

    if short_url not in url_status_cache:

        # mind GitHub rate limiting, use local files to verify link
        if short_url.startswith(github_repo_master_path):
            local_path = short_url.replace(github_repo_master_path, "")
            if exists(abspath(project_root_dir + local_path)):
                status = 200
            else:
                status = 404
        elif "developer.ibm.com" in short_url:
            status = test_ibm_developer_url(short_url)
        else:
            try:
                status = requests.head(short_url, allow_redirects=True, timeout=5).status_code
                if status == 405:  # method not allowed, use GET instead of HEAD
                    status = requests.get(short_url, allow_redirects=True, timeout=5).status_code
                if status == 429:  # GitHub rate limiting, try again after 1 minute
                    sleep(randint(60, 90))
                    status = requests.head(short_url, allow_redirects=True, timeout=5).status_code
            except requests.exceptions.Timeout:
                status = 408
            except requests.exceptions.RequestException:
                status = 500

        url_status_cache[short_url] = status

    status = url_status_cache[short_url]

    return file, line, text, url, status


def verify_urls_concurrently(file_line_text_url: [(str, int, str, str)]) -> [(str, int, str, str)]:
    file_line_text_url_status = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=parallel_requests) as executor:
        check_urls = (
            executor.submit(test_url, file, line, text, url)
            for (file, line, text, url) in file_line_text_url
        )
        for url_check in concurrent.futures.as_completed(check_urls):
            try:
                file, line, text, url, status = url_check.result()
                file_line_text_url_status.append((file, line, text, url, status))
            except Exception as e:
                print(str(type(e)))
                file_line_text_url_status.append((file, line, text, url, 500))
            finally:
                print("{}/{}".format(len(file_line_text_url_status),
                                     len(file_line_text_url)), end="\r")

    return file_line_text_url_status


def verify_doc_links() -> [(str, int, str, str)]:

    # 1. find all relevant Markdown files
    md_file_paths = find_md_files()

    # 2. extract all links with text and URL
    file_line_text_url = [
        (file, line, text, url)
        for file in md_file_paths
        for (line, text, url) in get_links_from_file_content(file)
    ]

    # 3. validate the URLs
    file_line_text_url_status = verify_urls_concurrently(file_line_text_url)

    # 4. filter for the invalid URLs (status 404: "Not Found") to be reported
    file_line_text_url_404 = [(f, l, t, u, s)
                              for (f, l, t, u, s) in file_line_text_url_status
                              if s == 404]

    # 5. print some stats for confidence
    print("{} {} links ({} unique URLs) in {} files.\n".format(
        "Checked" if file_line_text_url_404 else "Verified",
        len(file_line_text_url_status),
        len(url_status_cache),
        len(md_file_paths)))

    # for url in sorted(url_status_cache.keys()):
    #     print(url)

    # 6. report invalid links, exit with error for CI/CD
    if file_line_text_url_404:

        for (file, line, text, url, status) in file_line_text_url_404:
            print("{}:{}: `[{}]({})` {}".format(
                relpath(file, project_root_dir), line, text,
                url.replace(github_repo_master_path, ""), status))

        # print a summary line for clear error discovery at the bottom of Travis job log
        print("\nERROR: Found {} invalid links".format(
            len(file_line_text_url_404)))

        exit(1)


def apply_monkey_patch_to_force_ipv4_connections():
    # Monkey-patch socket.getaddrinfo to force IPv4 conections, since some older
    # routers and some internet providers don't support IPv6, in which case Python
    # will first try an IPv6 connection which will hang until timeout and only
    # then attempt a successful IPv4 connection
    import socket

    # get a reference to the original getaddrinfo function
    getaddrinfo_original = socket.getaddrinfo

    # create a patched getaddrinfo function which uses the original function
    # but filters out IPv6 (socket.AF_INET6) entries of host and port address infos
    def getaddrinfo_patched(*args, **kwargs):
        res = getaddrinfo_original(*args, **kwargs)
        return [r for r in res if r[0] == socket.AF_INET]

    # replace the original socket.getaddrinfo function with our patched version
    socket.getaddrinfo = getaddrinfo_patched


if __name__ == '__main__':
    apply_monkey_patch_to_force_ipv4_connections()

    # # works
    # assert 200 == test_ibm_developer_url("https://developer.ibm.com/exchanges/data/")
    # # test_url("file", 0, "should", "https://developer.ibm.com/middleware/v1/contents/static/exchanges/data")
    # # test_url("file", 0, "should", "https://developer.ibm.com/middleware/v1/contents/data/doclaynet")
    #
    # # 301 redirect to location https://developer.ibm.com
    # assert 404 == test_ibm_developer_url("https://developer.ibm.com/exchanges/models")
    #
    # # 200: We are unable to find the page you have requested
    # assert 404 == test_ibm_developer_url("https://developer.ibm.com/technologies/artificial-intelligence/data/pubtabnet/")
    #
    # # 200: found
    # assert 200 == test_ibm_developer_url("https://developer.ibm.com/exchanges/data/all/doclaynet/")

    verify_doc_links()
