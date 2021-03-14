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


def threshold_image(img: Image, threshold: int, method="loop") -> Image:
    """Apply threshold operation to image.

    a pixel p will have a value of 255 if its value is greater or equal than
    that of the threshold value; otherwise, p will have a value of 0.

    Parameters
    ----------
    img : Image
        [description]
    threshold : int
        [description]
    method : str, optional
        the way to calculate the result, can either be mask (using numpy boolean indexing) or loop (accessing pixels explicitly), by default "loop"

    Returns
    -------
    Image
        [description]

    Raises
    ------
    ValueError
        [description]
    """
    img_arr = np.array(img)

    if method == "mask":
        mask = img_arr >= threshold
        img_arr[mask] = 255
        img_arr[~mask] = 0

    elif method == "loop":
        for i in range(img_arr.shape[0]):
            for j in range(img_arr.shape[1]):
                img_arr[i, j] = 255 if img_arr[i, j] >= threshold else 0
    else:
        raise ValueError(f"Unknown method '{method}'")

    return Image.fromarray(img_arr)


def images_are_equal(img_one: Image, img_two: Image, method="loop") -> bool:
    """Check if two images are equal.

    Two images img_one and img_two of identical sizes are equal if and only if
    the intensity value of every pixel (x,y) of img_one is equal to the
    intensity value of the same pixel (x,y) of img_two.

    Parameters
    ----------
    img_one : Image
    img_two : Image
    method : str, optional
        the way to calculate the result, can either be mask (using numpy boolean indexing) or loop (accessing pixels explicitly), by default "loop"

    Returns
    -------
    bool
        [description]
    """
    img_one_arr = np.array(img_one)
    img_two_arr = np.array(img_two)

    have_same_shape = img_one_arr.shape == img_two_arr.shape
    if not have_same_shape:
        return False

    if method == "mask":
        return (img_one_arr == img_two_arr).all()

    elif method == "loop":
        for i in range(img_one_arr.shape[0]):
            for j in range(img_one_arr.shape[1]):
                if img_one_arr[i, j] != img_two_arr[i, j]:
                    return False  # we have found two pixels with different values
        return True

    else:
        raise ValueError(f"Unknown method '{method}'")


def _sup_or_inf(
    img_one: Image, img_two: Image, sup_or_inf: str, method="loop"
) -> Image:
    """Compute supremum or infimum of two images.

    This is intended as a helper function. Use "supremum(...)" or "infimum(...)" instead.

    Parameters
    ----------
    img_one : Image
        [description]
    img_two : Image
        [description]
    sup_or_inf : str
        [description]
    method : str, optional
        the way to calculate the result, can either be mask (using numpy boolean indexing) or loop (accessing pixels explicitly), by default "loop"

    Returns
    -------
    Image
        [description]

    Raises
    ------
    ValueError
        [description]
    ValueError
        [description]
    ValueError
        [description]
    """
    img_one_arr = np.array(img_one)
    img_two_arr = np.array(img_two)

    if sup_or_inf not in ["sup", "inf"]:
        raise ValueError(f"Unknown sup_or_inf '{sup_or_inf}'")

    have_same_shape = img_one_arr.shape == img_two_arr.shape
    if not have_same_shape:
        raise ValueError("Images should be of equal size.")

    if method == "mask":
        compare_func = np.maximum if sup_or_inf == "sup" else np.minimum
        return Image.fromarray(compare_func(img_one_arr, img_two_arr))

    elif method == "loop":
        result_img_arr = np.empty(img_one_arr.shape, dtype=img_one_arr.dtype)

        compare_func = max if sup_or_inf == "sup" else min
        for i in range(img_one_arr.shape[0]):
            for j in range(img_one_arr.shape[1]):
                result_img_arr[i, j] = compare_func(
                    img_one_arr[i, j], img_two_arr[i, j]
                )

        return Image.fromarray(result_img_arr)

    else:
        raise ValueError(f"Unknown method '{method}'")


def supremum(img_one: Image, img_two: Image, method: str = "loop") -> Image:
    """Compute the supremum of two images.

    Parameters
    ----------
    img_one : Image
        [description]
    img_two : Image
        [description]
    method : str, optional
        the way to calculate the result, can either be mask (using numpy boolean indexing) or loop (accessing pixels explicitly), by default "loop"

    Returns
    -------
    Image
        [description]
    """
    return _sup_or_inf(img_one, img_two, "sup", method)


def infimum(img_one: Image, img_two: Image, method: str = "loop") -> Image:
    """Compute the infimum of two images.

    Parameters
    ----------
    img_one : Image
        [description]
    img_two : Image
        [description]
    method : str, optional
        the way to calculate the result, can either be mask (using numpy boolean indexing) or loop (accessing pixels explicitly), by default "loop"

    Returns
    -------
    Image
        [description]
    """
    return _sup_or_inf(img_one, img_two, "inf", method)


def _erosion_or_dilation_of_size_one(
    img: Image, erosion_or_dilation: str, method: str
) -> Image:
    """Calculate an erosion or dilation of size 1.

    This is intended as a helper function.

    Parameters
    ----------
    img : Image
        [description]
    erosion_or_dilation : str
        [description]
    method : str, optional
        the way to calculate the result, can either be mask (using numpy boolean indexing) or loop (accessing pixels explicitly), by default "loop"

    Returns
    -------
    Image
        [description]

    Raises
    ------
    ValueError
        [description]
    """
    img_arr = np.array(img)

    result_img = np.empty(img_arr.shape, dtype=img_arr.dtype)

    nrows = img_arr.shape[0]
    ncols = img_arr.shape[1]

    for i in range(nrows):
        for j in range(ncols):
            # we need max / min here to handle the pixels at the edge of the image correctly
            if method == "mask":
                sub_arr = img_arr[
                    max(i - 1, 0) : min(i + 1, nrows) + 1,
                    max(j - 1, 0) : min(j + 1, ncols) + 1,
                ]
            if method == "loop":
                sub_arr = []
                for sub_i in range(i - 1, i + 2):
                    for sub_j in range(j - 1, j + 2):
                        if (0 <= sub_i < nrows) and (0 <= sub_j < ncols):
                            sub_arr.append(img_arr[sub_i, sub_j])

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


def _erosion_or_dilation_of_size_i(
    img: Image, i: int, erosion_or_dilation, method: str
) -> Image:
    assert i > 0

    result_img = _erosion_or_dilation_of_size_one(img, erosion_or_dilation, method)
    for _ in range(i - 1):
        result_img = _erosion_or_dilation_of_size_one(
            result_img, erosion_or_dilation, method
        )

    return result_img


def erosion(img: Image, i: int, method: str = "loop"):
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
    return _erosion_or_dilation_of_size_i(img, i, "erosion", method)


def dilation(img: Image, i: int, method: str = "loop"):
    """Compute dilation of image.

    Parameters
    ----------
    img : Image
        [description]
    i : int
        [description]
    method : str
        [description]

    Returns
    -------
    [type]
        [description]
    """
    return _erosion_or_dilation_of_size_i(img, i, "dilation", method)


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
