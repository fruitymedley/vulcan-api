# Vulcan API Technical Interview

## Getting Started

1. Install Docker
1. Run 

```
docker compose build
docker compose up
```

The API is now running on your machine!

## Usage

This creates a docker container on your local machine which exposes a REST API at `127.0.0.1:8000`. Using the route `/average_intensity` executes a function which takes an image file and calculates the average intensity of the pixels in the image.

To use this function, use a `POST` request to `127.0.0.1:8000/average_intensity` with a `form-data` body type, and a key `image` of type file with the desired file uploaded.

## Tests

This repo uses PyTest. This can be installed with `pip install -U pytest`

Tests can be run by running `pytest` or by using the testing extension in VSCode.