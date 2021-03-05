import pytest
from image_processing_exercises import utils


@pytest.mark.parametrize(
    "img_one,img_two,expected_result",
    [
        (utils.get_image("02ab", "cam_74"), utils.get_image("02ab", "cam_74"), True),
        (
            utils.get_image("02ab", "cam_74"),
            utils.get_image("02ab", "cam_74_threshold100"),
            False,
        ),
    ],
)
def test_images_are_equal(img_one, img_two, expected_result):
    assert utils.images_are_equal(img_one, img_two) == expected_result
