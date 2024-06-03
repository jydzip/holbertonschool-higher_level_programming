# Use the previous Docker image as the base
FROM hello-alpine

# Install curl package
RUN apk add --no-cache curl

# Copy config.txt into the container
COPY config.txt /app/config.txt
