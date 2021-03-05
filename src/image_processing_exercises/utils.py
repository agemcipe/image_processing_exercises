import pathlib

import image_processing_exercises
import numpy as np
from PIL import Image


def get_image_path(
    exercise_id: str, img_id: str, file_extension: str = "pgm"
) -> pathlib.Path:
    """Get image path.

    Parameters
    ----------
    exercise_id : str
        [description]
    img_id : str
        [description]
    file_extension : str, optional
        [description], by default "pgm"

    Returns
    -------
    pathlib.Path
        [description]

    Raises
    ------
    ValueError
        [description]
    """
    exercise_dir = [
        p
        for p in image_processing_exercises.EXERCISE_DIRS
        if p.name.endswith(exercise_id)
    ]
    if len(exercise_dir) != 1:
        raise ValueError(
            f"Cannot identify exercise_dir'{exercise_id}' in {image_processing_exercises.EXERCISE_DIRS}"
        )

    img_path = exercise_dir[0] / f"{img_id}.{file_extension}"
    assert img_path.exists()

    return img_path


def get_image(exercise_id: str, img_id: str, file_extension: str = "pgm") -> Image:
    """Get image.

    Parameters
    ----------
    exercise_id : str
        [description]
    img_id : str
        [description]
    file_extension : str, optional
        [description], by default "pgm"

    Returns
    -------
    Image
        [description]
    """
    return Image.open(get_image_path(exercise_id, img_id, file_extension))


def threshold_image(img: Image, threshold: int) -> Image:
    """Apply threshold operation to image.

    a pixel p will have a value of 255 if its value is greater or equal than
    that of the threshold value; otherwise, p will have a value of 0.

    Parameters
    ----------
    img : Image
        [description]
    threshold : int
        [description]

    Returns
    -------
    Image
        [description]
    """
    img_arr = np.array(img)
    mask = img_arr >= threshold
    img_arr[mask] = 255
    img_arr[~mask] = 0

    return Image.fromarray(img_arr)


def images_are_equal(img_one: Image, img_two: Image) -> bool:
    """Check if two images are equal.

    Two images img_one and img_two of identical sizes are equal if and only if
    the intensity value of every pixel (x,y) of img_one is equal to the
    intensity value of the same pixel (x,y) of img_two.

    Parameters
    ----------
    img_one : Image
    img_two : Image

    Returns
    -------
    bool
        [description]
    """
    img_one_arr = np.array(img_one)
    img_two_arr = np.array(img_two)

    return (img_one_arr.shape == img_two_arr.shape) and (
        img_one_arr == img_two_arr
    ).all()
