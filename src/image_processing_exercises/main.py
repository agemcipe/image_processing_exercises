from image_processing_exercises import BASE_OUTPUT_DIR, exercises, utils

if __name__ == "__main__":

    cam_74_img_p = utils.get_image_path("02ab", "cam_74")

    # Exercise 1
    exercises.exercise_01(
        img_path=utils.get_image_path("01a", "particles01__rows480__cols638", "jpg"),
        output_path=BASE_OUTPUT_DIR / "exercise_01a.jpg",
    )

    # exercise 2
    exercises.exercise_02a_thresh(
        img_path=utils.get_image_path("02ab", "cam_74"),
        value=100,
        output_path=BASE_OUTPUT_DIR / "exercise_02a_output_01.pgm",
    )
    exercises.exercise_02b_compare(
        img_one_path=cam_74_img_p,
        img_two_path=utils.get_image_path("02ab", "cam_74_threshold100"),
        output_path=BASE_OUTPUT_DIR / "exercise_02b_output_01.txt",
    )  # output should be 0

    # Exercise 3
    immed_grey_image_p = utils.get_image_path("03ab", "immed_gray_inv")
    exercises.exercise_03a_erosion(
        i=1,
        img_path=immed_grey_image_p,
        output_path=BASE_OUTPUT_DIR / "exercise_03a_ouput_01.pgm",
    )
    exercises.exercise_03b_dilation(
        i=1,
        img_path=immed_grey_image_p,
        output_path=BASE_OUTPUT_DIR / "exercise_03b_ouput_01.pgm",
    )

    # Exercise 4
    exercises.exercise_04a_opening(
        i=1,
        img_path=immed_grey_image_p,
        output_path=BASE_OUTPUT_DIR / "exercise_04a_ouput_01.pgm",
    )
    exercises.exercise_04b_closing(
        i=1,
        img_path=immed_grey_image_p,
        output_path=BASE_OUTPUT_DIR / "exercise_04b_ouput_01.pgm",
    )

    # Exercise 5
    exercises.exercise_05a_idempotence_opening(
        i=1,
        img_path=cam_74_img_p,
        output_path=BASE_OUTPUT_DIR / "exercise_05a_ouput_01.txt",
    )
    exercises.exercise_05b_idempotence_closing(
        i=1,
        img_path=cam_74_img_p,
        output_path=BASE_OUTPUT_DIR / "exercise_05b_ouput_01.txt",
    )

    # Ecercise 6
    exercises.exercise_06a_closing_opening(
        i=1,
        img_path=immed_grey_image_p,
        output_path=BASE_OUTPUT_DIR / "exercise_06a_ouput_01.pgm",
    )
    exercises.exercise_06b_closing_opening(
        i=1,
        img_path=immed_grey_image_p,
        output_path=BASE_OUTPUT_DIR / "exercise_06b_ouput_01.pgm",
    )

    # Ecercise 7
    exercises.exercise_07a_idempotence_closing_opening(
        i=1,
        img_path=cam_74_img_p,
        output_path=BASE_OUTPUT_DIR / "exercise_07a_ouput_01.txt",
    )
    exercises.exercise_07b_idempotence_opening_closing(
        i=1,
        img_path=cam_74_img_p,
        output_path=BASE_OUTPUT_DIR / "exercise_07b_ouput_01.txt",
    )

    # Exercise 8
    exercises.exercise_08a(img_path=utils.get_image_path("08a", "isn_256"), show=False)
