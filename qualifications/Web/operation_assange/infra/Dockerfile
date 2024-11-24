FROM python:3.11-alpine

RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

RUN apk add --update --no-cache openssl-dev chromium chromium-chromedriver supervisor gcc g++ make

RUN python -m pip install --upgrade pip

RUN mkdir -p /app

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./infra/site .

RUN python -m venv venv
COPY ./infra/requirements.txt /tmp/requirements.txt
RUN . /app/venv/bin/activate && pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

COPY ./infra/config/supervisord.conf /etc/supervisord.conf

EXPOSE 5000

USER www

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
