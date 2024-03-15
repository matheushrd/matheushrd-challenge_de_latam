@echo off

REM Define variables
SET IMAGE_NAME=challenge_de_latam
SET IMAGE_VERSION=1.0
SET CONTAINER_NAME=challenge_container

REM Build the Docker image
docker build . -t %IMAGE_NAME%:%IMAGE_VERSION%
IF NOT "%ERRORLEVEL%" == "0" (
    echo Docker build failed
    exit /b 1
)

REM Stop and remove the previous container if it exists
docker rm -f %CONTAINER_NAME% 2> nul

REM Run the Docker container
docker run --name %CONTAINER_NAME% %IMAGE_NAME%:%IMAGE_VERSION%
IF NOT "%ERRORLEVEL%" == "0" (
    echo Docker run failed
    exit /b 1
)

echo Container %CONTAINER_NAME% is not running anymore
