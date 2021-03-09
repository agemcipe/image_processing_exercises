import pathlib

import matplotlib.pyplot as plt
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


def exercise_08a(
    img_path=utils.get_image_path("08a", "isn_256"), max_size=3, show=True
):
    """Apply 4 filters to the given image.

    Parameters
    ----------
    img_path : [type], optional
        [description], by default utils.get_image_path("08a", "isn_256")
    max_size : int, optional
        [description], by default 3
    show : bool, optional
        [description], by default True
    """
    img = Image.open(img_path)
    f, axarr = plt.subplots(max_size, 4, figsize=(14, 3 * max_size))

    operations = {
        "opening": utils.opening,
        "closing": utils.closing,
        "opening-closing-filter": utils.opening_closing_alternated_filter,
        "closing-opening-filter": utils.closing_opening_alternated_filter,
    }

    for i in range(max_size):
        for j, (title, f) in enumerate(operations.items()):
            axarr[i, j].imshow(f(img, i + 1), cmap="gray", vmin=0, vmax=255)
            axarr[i, j].set_xticks([])
            axarr[i, j].set_yticks([])
            if i == 0:
                axarr[i, j].set_title(title)
            if j == 0:
                axarr[i, j].set_ylabel(f"Size {i+1}", rotation=0, size="large")

    plt.tight_layout()
    if show:
        plt.show()

    plt.savefig("exercise_08a_output_02.png")
    with open("exercise_08a_output_01.txt", "w") as f_out:
        f_out.write("3")
        f_out.write("4")
        f_out.write(
            "The best two filters are the opening-closing and closing-opening filters as can be seen in 'exercise_08a_output_02.png'"
        )
