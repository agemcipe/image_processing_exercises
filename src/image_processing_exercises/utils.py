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


def _sup_or_inf(img_one: Image, img_two: Image, sup_or_inf: str) -> Image:
    img_one_arr = np.array(img_one)
    img_two_arr = np.array(img_two)

    if sup_or_inf == "sup":
        return np.maximum(
            img_one_arr, img_two_arr
        )  # element-wise comparison of two arrays
    elif sup_or_inf == "inf":
        return Image.fromarray(np.minimum(img_one_arr, img_two_arr))
    else:
        raise ValueError(f"Unknown sup_or_inf '{sup_or_inf}'")


def supremum(img_one: Image, img_two: Image) -> Image:
    """Compute the supremum of two images.

    Parameters
    ----------
    img_one : Image
        [description]
    img_two : Image
        [description]

    Returns
    -------
    Image
        [description]
    """
    return _sup_or_inf(img_one, img_two, "sup")


def infimum(img_one: Image, img_two: Image) -> Image:
    """Compute the infimum of two images.

    Parameters
    ----------
    img_one : Image
        [description]
    img_two : Image
        [description]

    Returns
    -------
    Image
        [description]
    """
    return _sup_or_inf(img_one, img_two, "inf")


def _erosion_or_dilation_of_size_one(img: Image, erosion_or_dilation: str) -> Image:

    img_arr = np.array(img)

    result_img = np.empty(img_arr.shape, dtype=img_arr.dtype)

    nrows = img_arr.shape[0]
    ncols = img_arr.shape[1]

    for i in range(nrows):
        for j in range(ncols):
            sub_arr = img_arr[
                max(i - 1, 0) : min(i + 1, nrows)
                + 1,  # we need max / min here to handle the pixels at the edge of the image correctly
                max(j - 1, 0) : min(j + 1, ncols) + 1,
            ]

            if erosion_or_dilation == "erosion":
                result_img[i, j] = np.min(sub_arr)
            elif erosion_or_dilation == "dilation":
                result_img[i, j] = np.max(sub_arr)
            else:
                raise ValueError(f"Unknown erosion_or_dilation '{erosion_or_dilation}'")

    assert not np.isnan(
        result_img
    ).any()  # if any np.nan are in the result image something must have gone wrong

    return Image.fromarray(result_img)


def _erosion_or_dilation_of_size_i(img: Image, i: int, erosion_or_dilation) -> Image:
    assert i > 0

    result_img = _erosion_or_dilation_of_size_one(img, erosion_or_dilation)
    for _ in range(i - 1):
        result_img = _erosion_or_dilation_of_size_one(result_img, erosion_or_dilation)

    return result_img


def erosion(img: Image, i: int):
    """Compute erosion of image.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]

    Returns
    -------
    [type]
        [description]
    """
    return _erosion_or_dilation_of_size_i(img, i, "erosion")


def dilation(img: Image, i: int):
    """Compute dilation of image.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]

    Returns
    -------
    [type]
        [description]
    """
    return _erosion_or_dilation_of_size_i(img, i, "dilation")


def opening(img: Image, i: int) -> Image:
    """Compute the opening of an image.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]

    Returns
    -------
    Image
        [description]
    """
    return dilation(erosion(img, i), i)


def closing(img: Image, i: int) -> Image:
    """Compute the closing of an image.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]

    Returns
    -------
    Image
        [description]
    """
    return erosion(dilation(img, i), i)


def closing_opening_alternated_filter(img: Image, i: int) -> Image:
    """Apply an closing-opening alternated filter to image.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]

    Returns
    -------
    Image
        [description]
    """
    return closing(opening(img, i), i)


def opening_closing_alternated_filter(img: Image, i: int) -> Image:
    """Apply an opening-closing alternated filter to image.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]

    Returns
    -------
    Image
        [description]
    """
    return opening(closing(img, i), i)


def check_idempotence(img: Image, i: int, operation: str) -> bool:
    """Check if an operation is idempotent.

    The operation can either be an opening, closing, opening_closing filter or closing_opening filter.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]
    operation : str
        [description]

    Returns
    -------
    bool
        [description]

    Raises
    ------
    ValueError
        [description]
    """
    if operation == "opening":
        f = opening
    elif operation == "closing":
        f = closing
    elif operation == "opening_closing_alternated_filter":
        f = opening_closing_alternated_filter
    elif operation == "closing_opening_alternated_filter":
        f = closing_opening_alternated_filter
    else:
        raise ValueError(f"Unknown operation '{operation}'")

    result_img_one = f(img, i)
    result_img_two = f(result_img_one, i)

    return images_are_equal(result_img_one, result_img_two)
