# %%
# %%
import matplotlib
import matplotlib.cm as mplcm
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
import PIL.ImageOps
from image_processing_exercises import utils
from PIL import Image

# %%
# S1a. Contour extraction using MM erosion or dilation
def s1a_contour_extraction(img: Image) -> Image:
    img = PIL.ImageOps.invert(img.convert("RGB"))
    erosion_img = utils.erosion(img, i=1, method="mask")
    return Image.fromarray(np.array(img) - np.array(erosion_img))


# %%
test_image = utils.get_image("segmentation", "hitchcock", "png")
s1a_contour_extraction(test_image)

# %%
def get_neighbors(img_arr, p, connectivity=8, size=1):
    i, j = p
    neighbors = set()

    if connectivity == 8:
        for x in range(max(i - size, 0), min(i + size, img_arr.shape[0] - 1) + 1):
            for y in range(max(j - size, 0), min(j + size, img_arr.shape[1] - 1) + 1):
                if x == i and y == j:
                    continue  # a pixel is not its own neighbor, in case of size = 0 an empty set is returned
                neighbors.add((x, y))

    elif connectivity == 4:
        for x in [-1, 1]:
            new_x = i + x
            if 0 <= new_x < img_arr.shape[0]:
                neighbors.add((new_x, j))
        for y in [-1, 1]:
            new_y = j + y
            if 0 <= (j + y) <= img_arr.shape[1]:
                neighbors.add((i, new_y))

    else:
        raise ValueError(f"Unknown connectivity value '{connectivity}'")

    return neighbors


# S1b.Grassfire propagation algorithm
def s1b_grassfire(img: Image) -> dict:

    img_arr = np.array(img)

    regions = {}
    counter = 0

    white_pixels_idx = np.transpose(np.nonzero(img_arr == 255))

    overall_to_check = set(tuple(p) for p in white_pixels_idx)

    while len(overall_to_check) > 0:

        to_check = [overall_to_check.pop()]
        region = set()

        # finds one region
        while len(to_check) > 0:
            p = to_check.pop(0)
            region.add(p)

            neighbors = {
                n for n in get_neighbors(img_arr, p) if img_arr[n] == img_arr[p]
            }

            to_check.extend(list(neighbors - (region.union(set(to_check)))))

        regions[counter] = region
        overall_to_check -= region
        counter += 1

    return regions


# %%
def _get_n_colors(num_colors):
    cm = plt.get_cmap("gist_rainbow")
    cNorm = colors.Normalize(vmin=0, vmax=num_colors - 1)
    scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)
    color_ls = [scalarMap.to_rgba(i)[:3] for i in range(num_colors)]
    return color_ls


# %%
def color_regions(img: Image) -> Image:

    img = test_image
    regions = s1b_grassfire(img)
    img_arr = np.array(img)
    colors_ls = _get_n_colors(max(regions.keys()) + 1)

    img_arr_rgb = np.array(img.convert("RGB"))
    for i, ls in regions.items():
        for p in ls:
            img_arr_rgb[p] = np.array(colors_ls[i]) * 255

    return Image.fromarray(img_arr_rgb)


# %%
test_image = utils.get_image("segmentation", "particles", "png").convert("L")

color_regions(test_image)


# %%
# check that image is binary
img_arr = np.array(test_image)
img_arr.shape


def get_mask(img_arr, i, j):
    return img_arr[
        max(i - 1, 0) : min(i + 1, img_arr.shape[0]) + 1,
        max(j - 1, 0) : min(j + 1, img_arr.shape[1]) + 1,
    ]


# %%


# %% import matplotlib.pyplot as plt
# %%
