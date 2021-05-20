FROM python:3.9-alpine
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

EXPOSE 8080
ENV PYTHONPATH=/opt/

WORKDIR /tmp

RUN apk update && \
    apk add --no-cache tzdata git && \
    cp /usr/share/zoneinfo/UTC  /etc/localtime && echo 'UTC' > /etc/timezone && \
    git clone https://github.com/caa06d9c/demin.co.git && \
    mv /tmp/demin.co/www/ /opt/www/ && \
    pip3 install -r /tmp/demin.co/requirements.txt && \
    apk del git && \
    rm -Rf /var/cache/apk/* /tmp/*

WORKDIR /opt/www
USER nobody

ENTRYPOINT ["/usr/bin/env", "python3", "-u", "app.py"]
