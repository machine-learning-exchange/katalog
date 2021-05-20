FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y curl gnupg unzip
RUN apt-get install -y apt-transport-https

RUN pip install scikit-learn numpy protobuf acumos "minio<7.0.0"

ENV PROTOC_ZIP protoc-3.14.0-linux-x86_64.zip
RUN curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v3.14.0/$PROTOC_ZIP
RUN unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
RUN unzip -o $PROTOC_ZIP -d /usr/local 'include/*'
RUN rm -f $PROTOC_ZIP

ENV APP_HOME /app
COPY src $APP_HOME
WORKDIR $APP_HOME

ENTRYPOINT ["python"]
CMD ["sample.py"]
