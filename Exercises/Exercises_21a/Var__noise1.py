####################
####################


import cv2  # some functions will be used
import numpy as np
from Simple_MNIST_NN_from_scratch_11 import *

# Creating and loading some sample images:
#   im1__4__
#   im2__9__
#   im3__0__
#   im4__3__
#   im5__5__


# Loading an image with label 4 :
im1__4__ = cv2.imread("im1__4__.pgm")
im1__4__ = im1__4__[:, :, 0]
im1__4__ = im1__4__.reshape(28 * 28)
# print(make_predictions(np.array([im1__4__]).T, W1, b1, W2, b2))


## # Loading a difficult image with label 9 :
## im2__9__ = cv2.imread('im2__9__.pgm')
## im2__9__ = im2__9__[:,:,0]
## im2__9__ = im2__9__.reshape(28*28)
## # print(make_predictions(np.array([im2__9__]).T, W1, b1, W2, b2))


# Loading an image with label 0 :
im3__0__ = cv2.imread("im3__0__.pgm")
im3__0__ = im3__0__[:, :, 0]
im3__0__ = im3__0__.reshape(28 * 28)
# print(make_predictions(np.array([im3__0__]).T, W1, b1, W2, b2))


## # Loading an image with label 0 :
## im4__3__ = cv2.imread('im4__3__.pgm')
## im4__3__ = im4__3__[:,:,0]
## im4__3__ = im4__3__.reshape(28*28)
## # print(make_predictions(np.array([im4__3__]).T, W1, b1, W2, b2))


# Loading an image with label 5 :
im5__5__ = cv2.imread("im5__5__.pgm")
im5__5__ = im5__5__[:, :, 0]
im5__5__ = im5__5__.reshape(28 * 28)
# print(make_predictions(np.array([im5__5__]).T, W1, b1, W2, b2))


####################
####################


# Auxiliary function to facilitate calling make_predictions.
def call__make_predictions(i_orig, if_show=False):
    i_orig = np.array(i_orig)
    # If argument if_show is True, the input image is shown:
    if if_show:
        plt.imshow(i_orig.reshape((28, 28)))
        plt.show()
    i_orig = i_orig / 255
    res = make_predictions(np.array([i_orig]).T, W1, b1, W2, b2)
    return res


def call__make_predictions__adding__noise(i_orig, noise_scale, if_show=False):
    import numpy.random

    i_orig = np.array(i_orig)
    i_orig = i_orig.reshape(i_orig.size)  # 1-D
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
    noise = np.random.normal(loc=0.0, scale=noise_scale, size=i_orig.size)
    # i_with_noise: i_orig with added noise and clipped to [0,255] range:
    i_with_noise = np.clip(np.abs(i_orig + noise), 0, 255)
    # If argument if_show is True, the noisy image is shown:
    if if_show:
        plt.imshow(i_with_noise.reshape((28, 28)))
        plt.show()
    i_orig = i_orig / 255
    i_with_noise = i_with_noise / 255
    print("Original: ", make_predictions(np.array([i_orig]).T, W1, b1, W2, b2))
    res = make_predictions(np.array([i_with_noise]).T, W1, b1, W2, b2)
    print("With noise added: ", res)
    return i_with_noise * 255, res


def call__make_predictions__with__filtering(i_orig, if_show=False, if_open=False):
    import cv2

    i_orig = np.array(i_orig)
    i_orig = i_orig.reshape(i_orig.size)  # 1-D
    in1_filtered1 = i_orig
    if if_open:
        in1_filtered1 = cv2.morphologyEx(
            in1_filtered1.reshape(28, 28).astype("uint8"),
            cv2.MORPH_OPEN,
            np.ones((2, 2), np.uint8),
        )
    else:
        in1_filtered1 = cv2.morphologyEx(
            in1_filtered1.reshape(28, 28).astype("uint8"),
            cv2.MORPH_OPEN,
            np.ones((2, 2), np.uint8),
        )
        in1_filtered1 = cv2.morphologyEx(
            in1_filtered1.reshape(28, 28).astype("uint8"),
            cv2.MORPH_CLOSE,
            np.ones((2, 2), np.uint8),
        )
    in1_filtered1 = in1_filtered1.reshape(in1_filtered1.size)
    # If argument if_show is True, the filtered image is shown:
    if if_show:
        plt.imshow(in1_filtered1.reshape((28, 28)))
        plt.show()
    i_orig = i_orig / 255
    in1_filtered1 = in1_filtered1 / 255
    print("Before filtering: ", make_predictions(np.array([i_orig]).T, W1, b1, W2, b2))
    res = make_predictions(np.array([in1_filtered1]).T, W1, b1, W2, b2)
    print("After filtering: ", res)
    return in1_filtered1 * 255, res


# Example of calling call__make_predictions__adding__noise with example image:
# i1 = im4__3__
# in1, _ = call__make_predictions__adding__noise(i1, 10.0)
# cv2.imwrite('in1.pgm', in.reshape((28, 28)))
