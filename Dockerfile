FROM python:3.9-alpine
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

COPY sources /opt/
WORKDIR /opt/

RUN apk update && \
    apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/UTC  /etc/localtime && echo 'UTC' > /etc/timezone && \
    pip install -r requirements.txt && \
    apk del && \
    rm -Rf /var/cache/apk/*

WORKDIR /opt/www
USER nobody
ENV PYTHONPATH=/opt/

ENTRYPOINT ["/usr/bin/env", "python3", "-u", "app.py"]
