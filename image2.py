# A program to read the pixel of a given folder of pictures into an array using img.shape
# A new image file is passed to the program at command line.
# The program extract the pixel of the new image and compare it to the pixels of the images in the array.
# The program then print correct if the pixel of the new mage matches to any of the pixels in the array.

# Importing libraries
from skimage import io
import argparse
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import matplotlib

# path = "Users\study\Desktop\image\imfile"


def show_image(image, is_pixel=True):
    try:
        if is_pixel:
            plt.imshow(image)
        else:
            img_pixels = io.imread(image) 
            plt.imshow(img_pixels)
        plt.show()
    except FileNotFoundError:
        print("Image not found")  
        exit(0)    


# Comparing a given image to images in array
def compare(path, img):
    try:
        imagesList = listdir(path)
        test_img = io.imread(img)
        test_img_shape = test_img.shape
        is_found = False

        for image in imagesList:
            image = path + '/' + image
            image = io.imread(image)
            image_shape = image.shape
            if image_shape == test_img_shape:
                is_found = True
        return is_found
    except FileNotFoundError:
        print("Image not found")  
        exit(0)    


# Argument parser for receival of new image file
def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("compare", help="classifier compare- c")
    parser.add_argument('file', help='the test file')
    parser = parser.parse_args()

    return parser


# Taking argument on command line using test question
def main():
    path = "imfile"
    args = argument()
    comp = args.compare
    file = args.file
    
    if comp.lower() == 'compare':
        is_img = compare(path, file)
        print(is_img)
    else:
        print('operation not supported. Enter compare')

    show_image(file, is_pixel=False)


if __name__ == "__main__":
    main()

# Command line test case
# python image2.py  compare gsl.jpg

# pixel is true
# raw image is false