# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
import kfp.dsl as dsl
import kfp
from kfp import components
import yaml

dlf_op = components.load_component_from_file('component.yaml')

with open("dlf_example.yaml", 'r') as stream:
    sample_dlf = yaml.safe_load(stream)

@dsl.pipeline(
  name='dlf',
  description='A pipeline for dfl'
)
def dlfPipeline(
    action='create',
    dataset_yaml=yaml.safe_dump(sample_dlf)
):

    # define workflow
    dlf = dlf_op(action=action,
                 dataset_yaml=dataset_yaml).set_image_pull_policy('Always')

# Compile pipeline
from kfp_tekton.compiler import TektonCompiler
TektonCompiler().compile(dlfPipeline, 'dlf.yaml')
