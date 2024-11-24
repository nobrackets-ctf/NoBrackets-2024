FROM python:3.9-alpine3.19

COPY sudoku.py /app/chall.py
WORKDIR /app

RUN apk add socat coreutils

EXPOSE 1337

ENTRYPOINT socat TCP-LISTEN:1337,fork,reuseaddr,bind=0.0.0.0 EXEC:"stdbuf -i0 -o0 -e0 python3 /app/chall.py"
