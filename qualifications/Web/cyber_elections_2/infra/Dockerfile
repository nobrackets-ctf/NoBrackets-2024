FROM python:3.12-slim

RUN pip3 install flask

WORKDIR /app

RUN adduser flask

COPY src /app
RUN chown -R flask:flask /app

USER flask

CMD ["python3", "app.py"]

