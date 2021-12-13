#!/usr/bin/env bash

# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

# TODO: parameterize
export LOG_FILE="notebook_runs_$( date +"%m%d_%H%M" ).txt"

date > "${LOG_FILE}"

run_notebook() {

  echo "$1"

  #IMAGE="tensorflow/tensorflow:2.7.0"  # used by Elyra
  IMAGE=$( sed -n "s/^ *image: \(.*\)$/\1/p" "$1" | sed 's/"//g' | sed "s/'//g" )

  # TODO: create and use mlexchange/elyra-tensorflow:2.7.0 image to run notebooks, here and in mlx
  #   - copy elyra-requirements to katalog repo notebook-sample/src/docker/elyra-tensorflow folder
  #   - update Elyra requirements
  #   - create Dockerfile and README and script to build and push an image for mlexchange/elyra-tensorflow:2.7.0 with elyra-requirements preinstalled
  #   - add image field to notebook yaml, default `mlexchange/elyra-tensorflow:2.7.0`

  NAME=$( sed -n "s/^name: \(.*\)$/\1/p" "$1" | sed 's/"//g' | sed "s/'//g" )

  NOTEBOOK_URL=$( sed -n "s/^ *source: \(.*\)$/\1/p" "$1" | sed 's/"//g' | sed "s/'//g" )

  # grep the existing requirements from the notebook YAML file, i.e. "matplotlib==3.3.4,numpy==1.19.5,tensorflow==2.6.0"
  # remove the enclosing (single-/double-) quotes and remove the `==1.2.3`, i.e. matplotlib,numpy,tensorflow
  REQUIREMENTS=$( sed -n "s/^ *requirements: \(.*\)$/\1/p" "$1" | sed 's/"//g' | sed "s/'//g" | sed "s/,/ /g" )

  if [[ -z "${NOTEBOOK_URL}" || -z "${IMAGE}" ]]; then
    echo "Must have a notebook URL and an Docker image to run on."
    exit 1
  fi

  if [[ "${NOTEBOOK_URL}" == *"/blob/"* ]]; then
    NOTEBOOK_URL="${NOTEBOOK_URL/github.com/raw.githubusercontent.com}"
    NOTEBOOK_URL="${NOTEBOOK_URL/\/blob\//\/}"
  fi

  header="
  *******************************************************************************************
   NAME:         ${NAME}
   NOTEBOOK_URL: ${NOTEBOOK_URL}
   REQUIREMENTS: ${REQUIREMENTS}
   IMAGE:        ${IMAGE}
  *******************************************************************************************
  "
  echo "$header" >> "${LOG_FILE}"

  docker run -i --rm  --entrypoint "" "${IMAGE}" bash -c "
    wget -q -O notebook_in.ipynb '${NOTEBOOK_URL}' 2> /dev/null || curl -s -o notebook_in.ipynb '${NOTEBOOK_URL}'
    python3 -m pip install pip --upgrade --quiet --progress-bar=ascii
    python3 -m pip install -r https://raw.githubusercontent.com/elyra-ai/elyra/master/etc/generic/requirements-elyra.txt --quiet --progress-bar on
    [[ -n '${REQUIREMENTS}' ]] && python3 -m pip install ${REQUIREMENTS} --quiet --progress-bar=on
    python3 -m pip list
    papermill --log-level CRITICAL --report-mode notebook_in.ipynb notebook_out.ipynb
  " >> "${LOG_FILE}" 2>&1  && echo OK || echo FAILED

  # to show notebook cell outputs, use:   papermill --log-output notebook_in.ipynb notebook_out.ipynb
}

# export the function so it can be used by find
export -f run_notebook

find notebook-samples -type f \
    -not -path '*template*' \
    -a -not -path '*/\.*' \
    -a -not -path '*maintainer.yaml*' \
    -a \( -name '*.yaml' -o -name '*.yml' \) \
    -exec bash -c 'run_notebook "$0"' {} \;

#run_notebook notebook-samples/codenet-lang.yaml
#run_notebook notebook-samples/codenet-mlm.yaml
#run_notebook notebook-samples/qiskit-ml.yaml
#run_notebook notebook-samples/qiskit-nncr.yaml
#run_notebook notebook-samples/art-poison.yaml
#run_notebook notebook-samples/art-detector.yaml                          # TF 2.3.0 only, TF 2.7.0: eager execution, recursion limit exceeded, kernel died
#run_notebook notebook-samples/aif-bias.yaml                              # Exception encountered at "In [2]": An exception has occurred, use %tb to see the full traceback.
#run_notebook notebook-samples/JFK-airport.yaml                           # need PVC, or FileNotFoundError: [Errno 2] No such file or directory: 'data-vol-1/noaa-weather-data-jfk-airport.tar.gz'
#run_notebook notebook-samples/src/notebook-yaml-samples/maintainer.yaml  # need K8s Minio and metrics.csv, or timeout HTTPConnectionPool(host='minio-service.kubeflow', port=9000)
