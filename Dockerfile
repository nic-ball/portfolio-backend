# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Fix warnings: Use '=' for environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
# Added '--no-install-recommends' to keep image small
# Separated update and install to prevent caching issues
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Start command
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
