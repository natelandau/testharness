# Use the official Python base image
FROM python:3.11


# Set labels
LABEL org.opencontainers.image.source=https://github.com/natelandau/testharness
LABEL org.opencontainers.image.description="Test Harness"
LABEL org.opencontainers.image.licenses=MIT
LABEL org.opencontainers.image.url=https://github.com/natelandau/testharness
LABEL org.opencontainers.image.title="Test Harness"

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install git
RUN apt-get update && apt-get install -y git tzdata

# Install Poetry
RUN pip install poetry

# Install dependencies and script
RUN poetry install --without dev

# Set the entrypoint to run the script
ENTRYPOINT ["poetry", "run", "testharness"]
