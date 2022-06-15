FROM registry.access.redhat.com/ubi8/python-38

RUN pip3 install PyYaml exchange-metadata-converter==0.0.9

ENV APP_HOME /app
COPY src $APP_HOME
WORKDIR $APP_HOME

ENTRYPOINT ["python"]
CMD ["dataset_converter.py"]
