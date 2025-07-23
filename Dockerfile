# Use official Python slim image
FROM python:3.9-slim

# Install curl & necessary packages for kubectl
RUN apt-get update && apt-get install -y curl git && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    && rm kubectl

# Set working directory
WORKDIR /app

# Copy the summarizer script to the container
COPY summarizer.py .

# Install Python dependencies
RUN pip install --no-cache-dir transformers torch

# Pre-download FLAN-T5 model to speed up container start (optional but recommended)
RUN python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; AutoTokenizer.from_pretrained('google/flan-t5-base'); AutoModelForSeq2SeqLM.from_pretrained('google/flan-t5-base')"

# Entrypoint to run the summarizer
ENTRYPOINT ["python3", "summarizer.py"]

