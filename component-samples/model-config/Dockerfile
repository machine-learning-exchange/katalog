FROM registry.access.redhat.com/ubi8/python-38

RUN pip install kubernetes Flask flask-cors requests ruamel.yaml

ENV APP_HOME /app
COPY src $APP_HOME
WORKDIR $APP_HOME

ENTRYPOINT ["python"]
CMD ["app.py"]
