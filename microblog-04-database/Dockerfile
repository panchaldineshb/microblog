FROM ubuntu:16.04

LABEL maintainer="AKIKO TAKANO / (Twitter: @akiko_pusu)" \
description="Image to run Redmine simply with sqlite to try/review plugin."

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

ADD . /todo
WORKDIR /todo
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "./run.sh"]
