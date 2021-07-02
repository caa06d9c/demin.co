FROM python:3.9-alpine
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

EXPOSE 8080
ENV PYTHONPATH=/opt/
ADD www /opt/www/


RUN apk update && \
    apk add --no-cache tzdata && \
    cp /usr/share/zoneinfo/UTC  /etc/localtime && echo 'UTC' > /etc/timezone && \
    pip3 install -r /opt/www/requirements.txt && \
    apk del && \
    rm -Rf /var/cache/apk/*

WORKDIR /opt/www/
USER nobody

ENTRYPOINT ["/usr/bin/env", "python3", "-u", "app.py"]
