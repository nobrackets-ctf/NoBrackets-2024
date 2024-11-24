FROM python:3

RUN adduser challenge

RUN python -m pip install --upgrade pip
RUN mkdir -p /app

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./infra/site .

COPY ./infra/requirements.txt /app

RUN chown -R challenge:challenge /app

USER challenge 

RUN pip install -r requirements.txt

CMD python3 app.py
