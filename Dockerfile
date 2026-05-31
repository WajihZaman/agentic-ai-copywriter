# Use a lightweight, pre-configured Python environment
FROM python:3.10-slim-buster

# Force root execution to update core network configurations
USER root
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create the standard non-root user account required by Hugging Face
RUN useradd -m -u 1000 user
WORKDIR /home/user/app

# Copy the repository and set folder permissions for user 1000
COPY --chown=user:user . /home/user/app

# Switch to the non-root account to run the application securely
USER user
ENV PATH="/home/user/.local/bin:${PATH}"

# Install your dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the mandatory Hugging Face web port
EXPOSE 7860

# Start the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
