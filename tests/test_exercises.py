import os

import pytest
from image_processing_exercises import exercises, utils
from PIL import Image


def test_exercise_02a_thresh(tmp_path):
    output_path = tmp_path / "cam_74_threshold100_myresult.pgm"
    exercises.exercise_02a_thresh(
        utils.get_image_path("02ab", "cam_74"), value=100, output_path=output_path
    )

    assert utils.images_are_equal(
        Image.open(output_path), utils.get_image("02ab", "cam_74_threshold100")
    )


@pytest.mark.parametrize(
    "img_one_path,img_two_path,expected_result",
    [
        (
            utils.get_image_path("02ab", "cam_74"),
            utils.get_image_path("02ab", "cam_74"),
            "1",
        ),
        (
            utils.get_image_path("02ab", "cam_74"),
            utils.get_image_path("02ab", "cam_74_threshold100"),
            "0",
        ),
    ],
)
def test_exercise_02a_compare(img_one_path, img_two_path, expected_result, tmpdir):
    _cwd = os.getcwd()
    os.chdir(tmpdir)
    assert (
        open(exercises.exercise_02b_compare(img_one_path, img_two_path)[0]).read()
        == expected_result
    )
    os.chdir(_cwd)  # change back
