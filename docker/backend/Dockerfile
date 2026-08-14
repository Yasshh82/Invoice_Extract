# syntax=docker/dockerfile:1

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# PDF rendering dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        poppler-utils \
        libgl1 \
        libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir \
    -r requirements.txt

COPY backend/app ./app
COPY backend/ml ./ml

RUN useradd \
    --create-home \
    --shell /bin/bash \
    appuser

RUN mkdir -p /app/uploads /app/temp \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD [
    "uvicorn",
    "app.main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]