FROM python:3.10-slim
RUN apt-get update && apt-get install -y git
RUN python -m pip install --upgrade pip
COPY requirements.txt /tmp
RUN python -m pip install -r /tmp/requirements.txt
