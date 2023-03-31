# Functions to build and update documentation
from shutil import copyfile


# HTML resources paths
def html_assets(parent):
    return '../assets/' if parent else 'assets/'


def html_images(parent):
    return '../images/' if parent else 'images/'


def write_files(texts, files):
    # Write documentation source files
    for text, file in zip(texts, files):
        f = open(file, "w")
        f.write(text)
        f.close()
