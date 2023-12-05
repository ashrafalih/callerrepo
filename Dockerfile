FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

COPY . /app

# Run hello-world when the container launches
CMD ["echo", "Hello, World!"]
