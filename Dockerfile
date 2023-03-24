FROM python:3.9.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
WORKDIR /book_service
COPY requirements.txt /book_service/
RUN pip install -r requirements.txt
COPY . /book_service/