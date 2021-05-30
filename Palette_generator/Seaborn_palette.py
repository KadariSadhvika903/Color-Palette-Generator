import seaborn as sns
import webcolors

def get_general_palette():
    palette = sns.color_palette()
    hex_palette = []
    for rgb in palette:
        hex_palette.append(webcolors.rgb_to_hex(tuple([int(255*x) for x in rgb])))
    return hex_palette

def get_light_palette(color):
    palette = sns.light_palette(color, 10)
    hex_palette = []
    for rgb in palette:
        hex_palette.append(webcolors.rgb_to_hex(tuple([int(255 * x) for x in rgb])))
    return hex_palette

def get_dark_palette(color):
    palette = sns.dark_palette(color, 10)
    hex_palette = []
    for rgb in palette:
        hex_palette.append(webcolors.rgb_to_hex(tuple([int(255 * x) for x in rgb])))
    return hex_palette