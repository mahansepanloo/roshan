

FROM python:3.11-slim

WORKDIR /code

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    g++ \
    python3-dev \
    unixodbc \
    unixodbc-dev \
    libodbc1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "Roshan.wsgi", ":8000"]
















services:
  web:
    container_name: web
    build: .
    command: >
      sh -c "python3 manage.py migrate &&
             gunicorn Roshan.wsgi:application --bind 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - postgres
    networks:
      - webnet

  postgres:
    container_name: postgres
    image: postgres:latest
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
    ports:
      - "5433:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - webnet

networks:
  webnet:

volumes:
  postgres_data:
