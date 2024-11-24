FROM ghcr.io/downunderctf/docker-vendor/nsjail:ubuntu-22.04
FROM python:3.13.0-bookworm

ENV HOSTNAME cracknhash

ENV JAIL_CWD=/chal
RUN apt update && apt install -y socat \
	&& pip install inputimeout pwntools \
	&& mkdir /home/ctf

COPY ./src/cracknhash.py /home/ctf
COPY ./src/rockyou.txt /home/ctf

EXPOSE 1337

WORKDIR /home/ctf
ENTRYPOINT ["socat", "tcp-listen:1337,fork,reuseaddr", "exec:'python3 /home/ctf/cracknhash.py'"]
