FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /wallstreet

WORKDIR /wallstreet

ADD . /wallstreet/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
