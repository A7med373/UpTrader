FROM python:3.10-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd libpq-dev gcc && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create a non-root user to run the application
RUN adduser --disabled-password --gecos '' appuser
RUN mkdir -p /app/static /app/media
RUN chown -R appuser:appuser /app
RUN chmod -R 755 /app/static /app/media
USER appuser

# Run the application
CMD ["gunicorn", "UpTrader.wsgi:application", "--bind", "0.0.0.0:8000"]
