"""
File: stanCodoshop.py
Name: Chen, Wei Ting
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):  # The distance between one pixel and red_avg, green_avg, blue_avg
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    color_distance = math.sqrt((red - pixel.red) * (red - pixel.red) + (green - pixel.green) * (green - pixel.green) + (
            blue - pixel.blue) * (blue - pixel.blue))
    return color_distance


def get_average(pixels):  # pixels is a python list [(pixel_1.red,pixel_1.green,pixel_1.blue),(pixel_2.red,pixel_2.green,
    # pixel_2.blue),(pixel_3.red, pixel_3.green,pixel_3.blue),....]
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # return Python list:[red, green, blue]。
    n = len(pixels)  # n pics
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    for pixel in pixels:
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue
    avg_red = red_sum // n
    avg_green = green_sum // n
    avg_blue = blue_sum // n
    return [avg_red, avg_green, avg_blue]  # Are the factors of the Milestone1 get_pixel_dist's (red, green, blue)


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """

    avg_rgb = get_average(pixels)
    # avg_rgb[0] = avg_red
    # avg_rgb[1] = avg_green
    # avg_rgb[2] = avg_blue

    # index method
    # min_dist = 0
    # best_pixel = 0
    # for i in range(len(pixels)):
    #     if i == 0:  # first condition
    #         min_dist = get_pixel_dist(pixels[i], avg_rgb[0], avg_rgb[1], avg_rgb[2])
    #         best_pixel = pixels[i]
    #     else:  # other condition
    #         if min_dist > get_pixel_dist(pixels[i], avg_rgb[0], avg_rgb[1], avg_rgb[2]):
    #             min_dist = get_pixel_dist(pixels[i], avg_rgb[0], avg_rgb[1], avg_rgb[2])
    #             best_pixel = pixels[i]
    # return best_pixel

    # not a index method
    min_dist = float('inf')  # min_dist = float('inf') is infinite float
    best_pixel = 0
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_rgb[0], avg_rgb[1], avg_rgb[2])  # Find average and each distance
        if min_dist > dist:
            min_dist = dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)  # blank image

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    for x in range(width):
        for y in range(height):
            pixels = []
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)
            best_pixel = get_best_pixel(pixels)
            result.set_pixel(x, y, best_pixel)

    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.

    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
