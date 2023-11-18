FROM python:3.9-bullseye
EXPOSE 4444
# FROM selenium/standalone-chrome:119.0.6045.123
# USER root
# RUN apt-get -y update && \
#     apt-get install -y --no-install-recommends python3.10 python3-pip
#     # python -m pip install --upgrade pip
RUN python -m pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
# USER 1200
WORKDIR /app
