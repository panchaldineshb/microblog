FROM python:3.5
LABEL maintainer="AKIKO TAKANO / (Twitter: @akiko_pusu)" \
description="Image to run Redmine simply with sqlite to try/review plugin."
ADD . /todo
WORKDIR /todo
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "./run.sh"]
