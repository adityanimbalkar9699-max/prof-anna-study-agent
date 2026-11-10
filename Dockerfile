# Multi-Platform Deployable Dockerfile for Prof. Anna Sovereign Agent
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    PORT=5000

# Install system dependencies for reportlab & matplotlib
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libfreetype6-dev \
    libpng-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt setup.py ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e .

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
