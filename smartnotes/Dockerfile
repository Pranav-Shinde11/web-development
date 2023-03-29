FROM python:3.7.3-alpine3.9

WORKDIR /app

COPY requirement.txt  /app

RUN pip install --no-cache-dir -r requirement.txt

COPY . .

EXPOSE 5000

CMD python /app/manage.py runserver 0.0.0.0:5000