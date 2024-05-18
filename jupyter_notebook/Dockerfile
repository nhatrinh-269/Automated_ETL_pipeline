FROM --platform=linux/amd64 jupyter/minimal-notebook

USER root

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

