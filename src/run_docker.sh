#!/bin/bash

# Define variables
IMAGE_NAME="challenge_de_latam"
IMAGE_VERSION="1.0"
CONTAINER_NAME="challenge_container"

# Build the Docker image
docker build . -t ${IMAGE_NAME}:${IMAGE_VERSION}
if [ $? -ne 0 ]; then
    echo "Docker build failed"
    exit 1
fi

# Stop and remove the previous container if it exists
docker rm -f ${CONTAINER_NAME} 2>/dev/null

# Run the Docker container
docker run --name ${CONTAINER_NAME} ${IMAGE_NAME}:${IMAGE_VERSION}
if [ $? -ne 0 ]; then
    echo "Docker run failed"
    exit 1
fi

echo "Container ${CONTAINER_NAME} is not running anymore"
