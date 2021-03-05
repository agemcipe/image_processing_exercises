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
