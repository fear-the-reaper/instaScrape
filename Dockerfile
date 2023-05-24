FROM python:3-slim-buster

ENV DB_HOST instaScrape-db
ENV DATABASE instaScrape
ENV DB_USER postgres
ENV DB_PASSWORD 1234
ENV DB_PORT 5432

WORKDIR /instaScrape

COPY requirements.txt requirements.txt

#Image python:3.9.5-slim also works # Image python:3.9.5-slim-buster also works

RUN apt-get update 
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get -y install ./google-chrome-stable_current_amd64.deb
RUN apt-get -y install libpq-dev gcc 
RUN pip install -r requirements.txt




COPY . .

WORKDIR /instaScrape/src

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]