import pathlib

from image_processing_exercises import utils
from PIL import Image


def exercise_02a_thresh(
    img_path, value: int, output_path: str = "exercise_02a_output_01.pgm"
):
    """Wrap threshold_image function.

    Parameters
    ----------
    img_path : [type]
        [description]
    value : int
        [description]
    output_path : str, optional
        [description], by default "exercise_02a_output_01.pgm"
    """
    input_img = Image.open(img_path)
    utils.threshold_image(input_img, threshold=100).save(output_path)


def exercise_02b_compare(img_one_path, img_two_path) -> tuple:
    """Wrap images_are_equal function.

    The program should write '1' or '0' (without quotes) to an output
    file called exercise_02b_output_01.txt depending on whether the
    pgm images are equal or not.

    Parameters
    ----------
    img_one_path : [type]
        [description]
    img_two_path : [type]
        [description]

    Returns
    -------
    Tuple
        [description]
    """
    output_val = int(
        utils.images_are_equal(Image.open(img_one_path), Image.open(img_two_path))
    )
    output_file = "exercise_02b_output_01.txt"
    with open(output_file, "w") as out_file:
        out_file.write(str(output_val))
        output_file_path = pathlib.Path(out_file.name).absolute()

    return output_file_path, output_val
