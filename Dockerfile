FROM python:3.10-slim

COPY requirements.txt /main_app/
COPY . /main_app
WORKDIR /main_app

RUN pip install psycopg2-binary;
RUN pip install --upgrade pip; pip install -r /main_app/requirements.txt

