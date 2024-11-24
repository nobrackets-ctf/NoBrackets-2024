FROM debian:trixie@sha256:57b3949871ca74f5e9050c1b7295c445d51fd0cc6504672d7ea08c2a92feaac5

ENV TIMEZONE Europe/Paris

RUN apt-get update && apt-get install -y socat python3 curl && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
COPY chall.py /app/chall.py
COPY flag.txt /app/flag.txt

RUN chmod 755 /app/chall.py
RUN chmod 744 /app/flag.txt

WORKDIR /app

RUN useradd -u 666 --home=/app -U challenge

USER challenge

ENV SOCAT_OPTIONS=",stderr,pty,cfmakeraw,echo=0"

ENTRYPOINT ["sh", "-c", "socat TCP-LISTEN:10202,reuseaddr,fork EXEC:/app/chall.py${SOCAT_OPTIONS}"]
