from numpy import asarray
from PIL.ImageFile import ImageFile

# %%


def calc_avg_intensity(image: ImageFile) -> float:
    """
    this method takes an image, loaded using PIL.Image.open(),
    and calculates the average RGB intensity of the entire image.
    """

    # read image data into an array
    pixels = asarray(image.getdata())

    # calculate the average value of that array
    return pixels.mean()
