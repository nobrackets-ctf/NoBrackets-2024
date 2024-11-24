FROM python:3.9-alpine3.19

COPY chall.py /app/chall.py
WORKDIR /app

RUN apk add socat coreutils

RUN python3 -m pip install --upgrade pip && python3 -m pip install pycryptodome more-itertools --break-system-packages

EXPOSE 1338

ENTRYPOINT socat TCP-LISTEN:1338,fork,reuseaddr,bind=0.0.0.0 EXEC:"stdbuf -i0 -o0 -e0 python3 /app/chall.py"