import numpy as np
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


def test_supremum():
    assert utils.images_are_equal(
        utils.supremum(
            utils.get_image("02c_1", "image1"), utils.get_image("02c_1", "image2")
        ),
        utils.get_image("02c_1", "image1_sup_image2"),
    )


def test_infimum():
    assert utils.images_are_equal(
        utils.infimum(
            utils.get_image("02c_1", "image1"), utils.get_image("02c_1", "image2")
        ),
        utils.get_image("02c_1", "image1_inf_image2"),
    )


@pytest.mark.parametrize(
    "size,expected_result",
    [
        (1, utils.get_image("03ab", "immed_gray_inv_20051123_ero1")),
        (2, utils.get_image("03ab", "immed_gray_inv_20051123_ero2")),
    ],
)
def test_erosion(size, expected_result):

    assert utils.images_are_equal(
        utils.erosion(utils.get_image("03ab", "immed_gray_inv"), size), expected_result
    )


@pytest.mark.parametrize(
    "size,expected_result",
    [
        (1, utils.get_image("03ab", "immed_gray_inv_20051123_dil1")),
        (2, utils.get_image("03ab", "immed_gray_inv_20051123_dil2")),
    ],
)
def test_dilation(size, expected_result):

    assert utils.images_are_equal(
        utils.dilation(utils.get_image("03ab", "immed_gray_inv"), size), expected_result
    )


@pytest.mark.parametrize(
    "size,expected_result",
    [
        (1, utils.get_image("04ab", "immed_gray_inv_20051123_ope1")),
        (2, utils.get_image("04ab", "immed_gray_inv_20051123_ope2")),
    ],
)
def test_opening(size, expected_result):

    print(np.array(expected_result))
    actual_result = utils.opening(utils.get_image("03ab", "immed_gray_inv"), size)

    assert utils.images_are_equal(actual_result, expected_result)


@pytest.mark.parametrize(
    "size,expected_result",
    [
        (1, utils.get_image("04ab", "immed_gray_inv_20051123_clo1")),
        (2, utils.get_image("04ab", "immed_gray_inv_20051123_clo2")),
    ],
)
def test_closing(size, expected_result):

    actual_result = utils.closing(utils.get_image("03ab", "immed_gray_inv"), size)

    print(np.array(actual_result))
    assert utils.images_are_equal(actual_result, expected_result)
