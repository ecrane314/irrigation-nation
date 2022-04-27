FROM python:3.8-slim-bullseye

ADD . .
RUN pip install -r requirements.txt

#CMD pip freeze
CMD ls