FROM python:3.11-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR  /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]