FROM python:3.7-slim-bullseye
USER root

ADD . .
RUN pip install -r requirements.txt

#CMD pip freeze
CMD ls