from json import loads
from PIL import Image

REST_ENDPOINT = "/average_intensity"
TEST_IMAGE = "media/gray.png"

# %%


# Valid request
def test_request_success(client):

    with open(TEST_IMAGE, "rb") as image:
        response = client.post(REST_ENDPOINT, data={"image": image})

    assert response.status_code == 200

    data = loads(response.data)

    assert data["data"] == 64.0


# Invalid request, no file provided
def test_request_no_file(client):

    response = client.post(REST_ENDPOINT)

    assert response.status_code == 400


# Invalid request, wrong file type provided
def test_request_bad_file(client):

    with open("README.md", "rb") as not_an_image:
        response = client.post(REST_ENDPOINT, data={"image": not_an_image})

    assert response.status_code == 500


def test_request_get(client):

    with open(TEST_IMAGE, "rb") as image:
        response = client.get(REST_ENDPOINT, data={"image": image})

    assert response.status_code == 405
