# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from kfp import dsl
from kubernetes.client.models import V1EnvVar


def convert_to_acumos_op(acumos_onboarding="false",
                         acumos_push_api='http://acumos-api-endpoint',
                         model_persistent_bucket='mlpipeline'):
    return dsl.ContainerOp(
        name='convert-models-to-acumos',
        image='tomcli/acumos-model-convert:latest',
        command=['python'],
        arguments=['-u', 'convert-to-acumos.py',
                   '--onboarding', acumos_onboarding,
                   '--push-api', acumos_push_api,
                   '--data-bucket', model_persistent_bucket]
    )


def echo_op(name="echo", text="placeholder"):
    return dsl.ContainerOp(
        name=name,
        image='busybox',
        command=['sh', '-c'],
        arguments=['echo "%s"' % text]
    )


@dsl.pipeline(
    name='Onboard MLX models to Acumos Marketplace',
    description='A pipeline for onboarding MLX models to Acumos Marketplace'
)
def acumos_pipeline(
    acumos_onboarding='true',
    acumos_push_api='http://acumos-api-endpoint',
    model_persistent_bucket='mlpipeline'
):
    pull_metadata = echo_op(name="process-model-source-files")
    convert_to_acumos = convert_to_acumos_op(acumos_onboarding=acumos_onboarding,
                                             acumos_push_api=acumos_push_api,
                                             model_persistent_bucket=model_persistent_bucket).after(pull_metadata)


if __name__ == '__main__':
    from kfp_tekton.compiler import TektonCompiler
    TektonCompiler().compile(acumos_pipeline, __file__.replace('.py', '.tgz'))
