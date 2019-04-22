FROM python:3.8-rc

WORKDIR /var/www

COPY . ./

ADD requirements.txt .

RUN apt-get update && \
    apt-get install -y libpq-dev

RUN pip install -r requirements.txt