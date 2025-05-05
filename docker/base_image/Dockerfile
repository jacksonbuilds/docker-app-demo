FROM ubuntu:22.04

# Install required packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Create a non-root user
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

# Set working directory and switch to user
WORKDIR /app
COPY . /app
RUN chown -R appuser:appuser /app
USER appuser

# Expose the web server port
EXPOSE 8080

# Run the web server
CMD ["python3", "demo_app.py"]