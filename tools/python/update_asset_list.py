#!/usr/bin/env python3

# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0

"""
    This script is used to (re)generate the katalog/README.md file with the current
    default assets currently held by Katalog. Run it from the project root folder via
    `make update_asset_list`.
"""


from __future__ import print_function

from glob import glob
from os.path import abspath, dirname, relpath
import yaml
import textwrap


asset_types = [
    "pipeline",
    "component",
    "model",
    "dataset",
    "notebook"
]

script_path = abspath(dirname(__file__))
project_dir = dirname(script_path)

katalog_dir = f"{project_dir}/../"


def get_list_of_yaml_files_in_katalog(asset_type: str) -> list[str]:

    yaml_files = glob(f"{katalog_dir}/{asset_type}-samples/**/*.yaml", recursive=True)

    yaml_files = [filepath for filepath in yaml_files
                  if not any(word in filepath for word in ["template", "test", "src"])]

    return sorted(yaml_files)


def generate_katalog_dict() -> dict:

    katalog_dict = dict()

    for asset_type in asset_types:

        yaml_files = get_list_of_yaml_files_in_katalog(asset_type)
        katalog_asset_list = []

        for yaml_file in yaml_files:

            with open(yaml_file) as f:
                yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
                asset_name = yaml_dict.get("name") or yaml_dict.get("metadata", {})\
                    .get("name", "").replace("-", " ").title() or ""
                asset_url = "./" + relpath(yaml_file, katalog_dir)

            katalog_asset_item = {
                "name": asset_name,
                "url": asset_url
            }

            katalog_asset_list.append(katalog_asset_item)

        katalog_dict[asset_type + "s"] = katalog_asset_list

    return katalog_dict


def generate_katalog_md() -> None:

    katalog_dict = generate_katalog_dict()

    md = []
    md.append(textwrap.dedent("""\
        <!-- Do not edit. This file was generated by ./tools/python/update_asset_list.py (make update_asset_list) -->
        # MLX Katalog
        MLX _Katalog_ is a project to hold the default content to bootstrap the _Machine Learning Exchange_.
        # List of Default Catalog Assets"""))

    for key in katalog_dict.keys():
        if(key == 'components'):
            md.append("## Pipeline Components")
        else:
            md.append("## " + key.capitalize())
        for item in katalog_dict[key]:
            content = "[" + item['name'] + "](" + item['url'] + ")"
            md.append("* " + content)
    with open('README.md', 'w') as f:
        f.write("\n".join(md))


if __name__ == '__main__':

    print("Regenerating katalog/README.md asset list.\n")

    # TODO: Add functionality to compare current list containing external asset links 
    # to make it easier for the user to prune, or move external pipelines into the 
    # katalog repo instead.

    generate_katalog_md()

    print("Done. Use git diff to evaluate if and which changes are desired!")
