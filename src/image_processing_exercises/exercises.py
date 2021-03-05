from image_processing_exercises import utils
from PIL import Image


def exercise_02a_thresh(
    input_path, value: int, output_path: str = "exercise_02a_output_01.pgm"
):
    """TODO.

    Parameters
    ----------
    input_path : [type]
        [description]
    value : int
        [description]
    output_path : str, optional
        [description], by default "exercise_02a_output_01.pgm"
    """
    input_img = Image.open(input_path)
    utils.threshold_image(input_img, threshold=100).save(output_path)


# def exercise_02b_compare(input_img_one, input_img_two) -> None:

#     output_val = int(
#         utils.images_are_equal(Image.open(input_img_one), Image.open(input_img_two))
#     )
#     out_file = HERE / "exercise_02b_output_01.txt"
#     with open(output_file, "w") as out_file:
#         out_file.write(output_val)
