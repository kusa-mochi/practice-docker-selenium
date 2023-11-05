FROM python:3.9-bullseye
RUN apt-get -y update && \
    python -m pip install --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
