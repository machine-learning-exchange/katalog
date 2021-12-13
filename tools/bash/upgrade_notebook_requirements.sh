#!/usr/bin/env bash

# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0

# This script uses pip-compile to upgrade the Python requirements in the notebook YAML files.
# It starts by finding all the notebook-sample YAML files and for each file it will:
#   - get the `requirements: ...`
#   - remove the ==1.2.3 version constraints
#   - break the package list into separate lines
#   - wrap the packages inside a temp file and feed to pip-compile --upgrade
#   - then filter the output to only the original required packages
#   - from the pip-compile output only get original required packages using grep
#   - replace line breaks with commas
#   - and use sed to replace the original requirements with the updated ones


# TODO: create alias 'gsed' for Linux and macOS compatibility "sed -i ''" on macOS  vs "sed -i" on Linux

# verify "pip-compile" is installed
if ! command -v pip-compile &> /dev/null
then
    echo "Could not find the 'pip-compile' command. Run 'pip install pip-tools'. Virtual environment recommended."
    exit 1
fi


update_requirements() {

  echo "$1"

  IMAGE=$( sed -n "s/^ *image: \(.*\)$/\1/p" "$1" | sed 's/"//g' | sed "s/'//g" )

  if [[ "${IMAGE}" == *"tensorflow:2.3"* ]]; then
    echo "Not upgrading requirements pinned down to old versions of tensorflow (2.3.x)."
    exit 0
  fi

  # grep the existing requirements from the notebook YAML file, i.e. "matplotlib==3.3.4,numpy==1.19.5,tensorflow==2.6.0"
  # remove the enclosing (single-/double-) quotes and remove the `==1.2.3`, i.e. matplotlib,numpy,tensorflow
  requirements=$( sed -n "s/^ *requirements: \(.*\)$/\1/p" "$1" | sed 's/"//g' | sed "s/'//g" | sed 's/==[^,]*//g' )

  # create in-memory file with required packages on separate lines:  <(echo "${requirements}" | tr ',' '\n')
  # use pip-compile --upgrade to compute latest compatible PyPi packages
  # create a grep pattern to only return the original input packages from the pip-compile output
  # use tr to convert back into single line, and sed to replace the trailing comma
  updated_requirements=$( \
    pip-compile -q -U - --output-file=- < <(echo "${requirements}" | tr ',' '\n') | \
      grep -iE "^($(echo "${requirements//,/|}" | sed 's/\[/./g' | sed 's/\]/./g'))==" | \
      tr '\n' ',' | sed 's/,$//' \
  )

  # use sed to replace the old requirements with the newly computed ones
  sed -i '' "s/^\( *\)requirements: .*/\1requirements: '${updated_requirements}'/" "$1"

  # show the before/after diff in the console output
  git diff "$1" | grep -E "^(\+|-) *requirements: "
}

# export the function so it can be used by find
export -f update_requirements

find notebook-samples -type f -not -path '*template*' -a -not -path '*/\.*' \
    -a \( -name '*.yaml' -o -name '*.yml' \) \
    -exec bash -c 'update_requirements "$0"' {} \;

#update_requirements notebook-samples/aif-bias.yaml

# export requirements=$( grep "requirements: " notebook-samples/codenet-lang.yaml | sed -n "s/^ *requirements: '\(.*\)'$/\1/p" | sed 's/==[^,]*//g' )
# export updated_requirements=$( pip-compile -q -U - --output-file=- < <( echo "${requirements}" | tr "," "\n" )  | grep -E "^(${requirements//,/|})==" | tr '\n' ',' | sed 's/,$//' )
# sed -i '' "s/requirements: .*/requirements: '${updated_requirements}'/" notebook-samples/codenet-lang.yaml
# git diff notebook-samples/codenet-lang.yaml | grep requirements
#-    requirements: 'matplotlib==3.3.4,numpy==1.19.5,tensorflow==2.6.0'
#+    requirements: 'matplotlib==3.5.0,numpy==1.21.4,tensorflow==2.7.0'
