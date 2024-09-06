FROM python:3.12.5-slim-bookworm

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/appuser/.local/bin:${PATH}" \
    PYTHONPATH="/app:${PYTHONPATH}"

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Set up the working directory in the container
WORKDIR /app

# Gather all requirements into a single file
COPY ./requirements.txt /tmp/requirements.txt


# Install and remove requirements
RUN pip3 install --no-cache-dir --default-timeout=180 -r /tmp/requirements.txt \
    && rm -f /tmp/requirements.txt

# # Copy the .env file into the container
# COPY .env .

# Copy the rest of the application code
COPY container_a /app/container_a
COPY container_b /app/container_b


CMD ["python3", "container_a/app.py"]
