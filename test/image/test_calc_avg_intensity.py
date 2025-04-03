from PIL import Image
import pytest

from src.image import calc_avg_intensity

# %%


def test_white():

    with Image.open("media/white.png") as image:
        result = calc_avg_intensity(image)

    assert result == 255.0


def test_gray():

    with Image.open("media/gray.png") as image:
        result = calc_avg_intensity(image)

    assert result == 64.0


def test_black():

    with Image.open("media/black.png") as image:
        result = calc_avg_intensity(image)

    assert result == 0.0
