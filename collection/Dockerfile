FROM --platform=linux/amd64 python:3.9-buster
 
COPY . /collection

WORKDIR /collection

RUN pip install -r requirements.txt

RUN mkdir /collection/image

RUN touch /collection/image/log.txt
