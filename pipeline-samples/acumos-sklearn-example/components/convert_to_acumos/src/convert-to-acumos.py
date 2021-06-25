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

"""
Provides a scikit-learn Acumos model example
"""
import numpy as np
import os

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from acumos.metadata import Options
from acumos.modeling import Model, List, create_namedtuple
from acumos.session import AcumosSession
from minio import Minio
import argparse


def main():
    """
    This parses arguments passed in from the CLI and performs the corresponding action.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--onboarding", type=str, help="Whether to onboard the Acumos model on Acumos Marketplace", default="false"
    )
    parser.add_argument(
        "--push-api", type=str, help="Acumos Marketplace push API", default=""
    )
    parser.add_argument(
        "--data-bucket", type=str, help="S3 bucket to persist the Acumos Models", default="mlpipeline"
    )
    args = parser.parse_args()

    data_bucket = args.data_bucket
    onboarding = args.onboarding.lower()
    push_api = args.push_api


    iris = load_iris()
    X = iris.data
    y = iris.target

    clf = RandomForestClassifier(random_state=0)
    clf.fit(X, y)

    IrisDataFrame = create_namedtuple('IrisDataFrame', [('sepal_length', List[float]),
                                                        ('sepal_width', List[float]),
                                                        ('petal_length', List[float]),
                                                        ('petal_width', List[float])])

    # =============================================================================
    # # starting in Python 3.6, you can alternatively use this simpler syntax:
    #
    # from acumos.modeling import NamedTuple
    #
    # class IrisDataFrame(NamedTuple):
    #     '''DataFrame corresponding to the Iris dataset'''
    #     sepal_length: List[float]
    #     sepal_width: List[float]
    #     petal_length: List[float]
    #     petal_width: List[float]
    # =============================================================================

    # =============================================================================
    # # A pandas DataFrame can also be used to infer appropriate NamedTuple types:
    #
    # import pandas as pd
    # from acumos.modeling import create_dataframe
    #
    # X_df = pd.DataFrame(X, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    # IrisDataFrame = create_dataframe('IrisDataFrame', X_df)
    # =============================================================================


    def classify_iris(df: IrisDataFrame) -> List[int]:
        '''Returns an array of iris classifications'''
        X = np.column_stack(df)
        return clf.predict(X)


    model = Model(classify=classify_iris)

    if onboarding == "true":
        session = AcumosSession(push_api=push_api) # push onboarding URL is available on your onboarding model page of your Acumos instance
        opts=Options(create_microservice=True)
        session.push(model,'my-iris',options=opts)

        print("Onboarded Acumos files to Marketplace")
    else:
        session = AcumosSession()
        session.dump(model, 'my-iris', '.')  # creates ./my-iris for web onboarding

        # Store Acumos files to S3
        cos = Minio(os.getenv('S3_ENDPOINT', 'minio-service:9000'),
                    access_key=os.getenv('S3_ACCESS_KEY', 'minio'),
                    secret_key=os.getenv('S3_SECRET_KEY', 'minio123'),
                    secure=False)


        cos.fput_object(data_bucket, 'my-iris/metadata.json', 'my-iris/metadata.json')
        cos.fput_object(data_bucket, 'my-iris/model.proto', 'my-iris/model.proto')
        cos.fput_object(data_bucket, 'my-iris/model.zip', 'my-iris/model.zip')

        print("Uploaded Acumos files to Object Storage")


if __name__ == "__main__":
    main()
