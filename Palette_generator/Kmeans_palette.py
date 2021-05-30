import numpy as np
import webcolors
from PIL import Image
from sklearn.cluster import KMeans


def generate_Kmeans_palette(file_name, number_of_clusters=6, return_rgb=False):
    im = Image.open(file_name)
    Width, Height = im.size
    ratio = Height / Width
    im = im.resize((200, int(ratio * 200)))
    img_PIL = np.array(im)
    dataset = img_PIL.T.reshape(img_PIL.T.shape[0], (img_PIL.T.shape[1] * img_PIL.T.shape[2])).T
    kmeans = KMeans(
        init="random",
        n_clusters=number_of_clusters,
        n_init=10,
        max_iter=300,
        random_state=42
    )
    kmeans.fit(dataset)
    rgb_palette = kmeans.cluster_centers_
    hex_palette = []
    for color in rgb_palette:
        hex_palette.append(webcolors.rgb_to_hex(tuple([int(color[0]), int(color[1]), int(color[2])])))
    if return_rgb:
        return rgb_palette
    else:
        return hex_palette


def rgb_to_hex_palette(rgb_palette):
    hex_palette = []
    for color in rgb_palette:
        hex_palette.append(webcolors.rgb_to_hex(tuple([int(color[0]), int(color[1]), int(color[2])])))
    return hex_palette

