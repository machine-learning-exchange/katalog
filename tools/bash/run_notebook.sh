#!/usr/bin/env bash

# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0

# Usage: ./run_notebook.sh <notebook-url> <requirements>

set -euo pipefail

#IMAGE="python:3.9"
IMAGE="tensorflow/tensorflow:2.7.0"  # used by Elyra


# copy elyra-requirements to katalog repo notebook-sample/src/docker/elyra-tensorflow folder
# create Dockerfile and README and script to build and push an image for mlexchange/elyra-tensorflow:2.7.0 with elyra-requirements preinstalled
# add image field to notebook yaml

NOTEBOOK_URL="${1}"
REQUIREMENTS="${2//,/ }"

if [[ -z "${NOTEBOOK_URL}" || -z "${REQUIREMENTS}" ]]; then
  echo "Must specify a notebook URL and a list of requirements."
  exit 1
fi

if [[ "${NOTEBOOK_URL}" == *"/blob/"* ]]; then
  NOTEBOOK_URL="${NOTEBOOK_URL/github.com/raw.githubusercontent.com}"
  NOTEBOOK_URL="${NOTEBOOK_URL/\/blob\//\/}"
fi

echo "NOTEBOOK_URL: ${NOTEBOOK_URL}"
echo "REQUIREMENTS: ${REQUIREMENTS}"



docker run -i --rm  --entrypoint "" "${IMAGE}" bash -c "
  wget -q -O notebook_in.ipynb '${NOTEBOOK_URL}' 2> /dev/null || curl -s -o notebook_in.ipynb '${NOTEBOOK_URL}'
  python3 -m pip install pip --upgrade --quiet --progress-bar=ascii
  python3 -m pip install -r https://raw.githubusercontent.com/elyra-ai/elyra/master/etc/generic/requirements-elyra.txt --quiet --progress-bar on
  python3 -m pip install ${REQUIREMENTS} --quiet --progress-bar=on
  papermill --log-level ERROR notebook_in.ipynb notebook_out.ipynb
"

# do nothing after the docker run so we automatically pass on the exit code
