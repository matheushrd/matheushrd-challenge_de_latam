# Define variables
$IMAGE_NAME = "challenge_de_latam"
$IMAGE_VERSION = "1.0"
$CONTAINER_NAME = "challenge_container"

# Build the Docker image
docker build . -t $IMAGE_NAME:$IMAGE_VERSION
if (-not $?) {
    Write-Host "Docker build failed"
    exit 1
}

# Stop and remove the previous container if it exists
docker rm -f $CONTAINER_NAME 2>$null

# Run the Docker container
docker run --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_VERSION
if (-not $?) {
    Write-Host "Docker run failed"
    exit 1
}

Write-Host "Container $CONTAINER_NAME is not running anymore"
