import pathlib
import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from image_processing_exercises import BASE_OUTPUT_DIR, utils
from PIL import Image

# run plotting in non interactive mode
matplotlib.use("Agg")


def exercise_01(img_path, output_path):
    """Show that image pixel can be modified.

    Here we simply add some noise to the image but multiplying each pixel value with a random number between 0 and 1.

    Parameters
    ----------
    img_path : [type], optional
        [description]
    output_path : [type], optional
        [description]
    """
    img_arr = np.array(Image.open(img_path))

    for i in range(img_arr.shape[0]):
        for j in range(img_arr.shape[1]):
            img_arr[i, j] = img_arr[i, j] * random.random()

    Image.fromarray(img_arr).save(output_path)


def exercise_02a_thresh(img_path, value, output_path):
    input_img = Image.open(img_path)
    utils.threshold_image(input_img, threshold=value).save(output_path)


def exercise_02b_compare(img_one_path, img_two_path, output_path) -> tuple:
    output_val = int(
        utils.images_are_equal(Image.open(img_one_path), Image.open(img_two_path))
    )
    with open(output_path, "w") as out_file:
        out_file.write(str(output_val))
        output_file_path = pathlib.Path(out_file.name).absolute()

    return output_file_path, output_val


def exercise_03a_erosion(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    utils.erosion(img, i).save(output_path)


def exercise_03b_dilation(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    utils.dilation(img, i).save(output_path)


def exercise_04a_opening(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    utils.opening(img, i).save(output_path)


def exercise_04b_closing(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    utils.closing(img, i).save(output_path)


def exercise_05a_idempotence_opening(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    output_val = utils.check_idempotence(img, i, operation="opening")
    with open(output_path, "w") as out_file:
        out_file.write(str(int(output_val)))


def exercise_05b_idempotence_closing(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    output_val = utils.check_idempotence(img, i, operation="closing")
    with open(output_path, "w") as out_file:
        out_file.write(str(int(output_val)))


def exercise_06a_closing_opening(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    utils.closing_opening_alternated_filter(img, i).save(output_path)


def exercise_06b_closing_opening(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    utils.closing_opening_alternated_filter(img, i).save(output_path)


def exercise_07a_idempotence_closing_opening(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    output_val = utils.check_idempotence(
        img, i, operation="closing_opening_alternated_filter"
    )
    with open(output_path, "w") as out_file:
        out_file.write(str(int(output_val)))


def exercise_07b_idempotence_opening_closing(i: int, img_path: str, output_path: str):
    img = Image.open(img_path)
    output_val = utils.check_idempotence(
        img, i, operation="opening_closing_alternated_filter"
    )
    with open(output_path, "w") as out_file:
        out_file.write(str(int(output_val)))


def exercise_08a(img_path, max_size=2, show=False):
    """Apply 4 filters to the given image.

    Parameters
    ----------
    img_path : [type], optional
        [description]
    max_size : int, optional
        [description], by default 2
    show : bool, optional
        [description], by default False
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
                axarr[i, j].set_ylabel(f"{i+1}", rotation=0, size="large")

    plt.tight_layout()
    if show:
        plt.show()

    plt.savefig(BASE_OUTPUT_DIR / "exercise_08a_output_02.png")
    with open(BASE_OUTPUT_DIR / "exercise_08a_output_01.txt", "w") as f_out:
        f_out.write("3\n")
        f_out.write("4\n")
        f_out.write(
            "The best two filters are the opening-closing and closing-opening filters as can be seen in 'exercise_08a_output_02.png'"
        )
