FROM --platform=${BUILDPLATFORM} python:3.12-alpine3.19

ARG BUILDPLATFORM=${BUILDPLATFORM}
ARG TZ=UTC
ARG APP_PORT
ARG DATABASE_URL
ARG DEBUG

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ="${TZ:-UTC}"
ENV DATABASE_URL="${DATABASE_URL}"
ENV APP_PORT=8000

RUN echo 'Define o diretório de trabalho como /app'
RUN mkdir -p /app
WORKDIR /app

RUN apk add --update g++ gcc git curl tcpdump libffi-dev libc-dev ca-certificates unzip wget zip zlib-dev bash

RUN apk add --no-cache --virtual .build-deps git autoconf automake flex bison libtool pkgconf make libxslt-dev musl-dev linux-headers  && \
    apk add --no-cache libxslt py3-lxml bash tzdata musl && \
    apk del --no-cache .build-deps && \
    apk add --no-cache py3-requests && \
    rm -rf /var/cache/apk/*

RUN apk update && apk --no-cache --upgrade add tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

RUN apk add --no-cache --update postgresql-dev

RUN apk add --no-cache --update jpeg-dev zlib-dev libjpeg libwebp-dev

RUN pip install --upgrade pip

RUN pip install wheel
RUN pip install pyopenssl
RUN pip install Pillow
RUN pip install psycopg2 psycopg2-binary SQLAlchemy

RUN echo 'Copia o arquivo requirements.txt para o diretório de trabalho'
COPY requirements.txt .

RUN echo 'Instala as dependências do projeto'
RUN pip install --no-cache-dir -r requirements.txt

RUN echo 'Copia o conteúdo da pasta src para o diretório de trabalho no contêiner'
COPY ./src .

RUN echo `Exponha a porta ${APP_PORT} para o tráfego externo`

EXPOSE ${APP_PORT}

RUN echo 'Comando para executar o servidor FastAPI quando o contêiner for iniciado'

ENTRYPOINT uvicorn --host 0.0.0.0 --port ${APP_PORT} server:app --workers ${APP_WORKERS} --threads ${APP_THREADS}