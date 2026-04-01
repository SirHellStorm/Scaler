# Use slim base image for lightweight execution
FROM python:3.10-slim

# Prevent python from writing pyc files to disk and disable output buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Ensure lightweight installation without cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app

# Runtime execution parameter suggestion for orchestrators (2 CPU, 8GB RAM constraints applied externally via: docker run --cpus="2" --memory="8g" ...)
CMD ["python", "inference.py"]
