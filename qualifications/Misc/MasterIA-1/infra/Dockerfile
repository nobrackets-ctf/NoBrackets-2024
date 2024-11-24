FROM python:3.10-slim-buster

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./src/ /app/src/

WORKDIR /app/src

CMD [ "python3.10", "-m" , "flask", "run", "--host=0.0.0.0"]