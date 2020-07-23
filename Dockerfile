FROM alpine:3.12.0

LABEL Maintainer="Hugo Almeida" e-mail="info@boldlink.io" version="0.0.1-rc1"

ENV USER=${USER:-app}
ENV UID=${UID:-12100}
ENV APP_HOST=${APP_HOST:-0.0.0.0}
ENV APP_PORT=${APP_PORT:-8000}
ENV APP_DEBUG=${APP_DEBUG:-True}

RUN apk update \
    && apk upgrade --no-cache

RUN apk add python3 py3-pip --no-cache

ADD src/requirements.txt .
RUN pip3 install -r ./requirements.txt --no-cache-dir

RUN adduser \
    --disabled-password \
    --uid "${UID}" \
    "${USER}"

WORKDIR /home/app

USER app

COPY src/main.py app.py

ENTRYPOINT ["/usr/bin/python3", "app.py"]
