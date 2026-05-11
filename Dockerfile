FROM python:3.11-slim

# Keep Python lean and container logs unbuffered.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install Python dependencies first to improve layer caching.
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app

# Create directories used by SQLite and collected static files.
RUN mkdir -p /data /app/staticfiles

EXPOSE 8000

# Replace "sahyadrihealth" if your Django project module name changes.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--timeout", "60", "--access-logfile", "-", "--error-logfile", "-", "sahyadrihealth.wsgi:application"]
