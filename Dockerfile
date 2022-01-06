FROM python:3

WORKDIR /app

COPY . .

RUN pip install django

RUN pip install pymongo

ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]