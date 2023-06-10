"""
File: blur.py
Name: Chen, Wei Ting
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage
BLUR = 10


def main():
    """
    Function: Blur the picture in 5 layers.
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """

    # show old image
    old_img = SimpleImage("images/smiley-face.png")  # Use SimpleImage to read file and transfer to image.
    old_img.show()

    # input old image and return new image
    # blurred_img = blur(old_img)

    # blur how many times and show it
    for i in range(BLUR):
        blurred_img = blur(old_img)
    blurred_img.show()


def blur(img):
    """
    :param img: Original image
    :return: Blurred image for one time
    """

    blurred = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):  # x coordinate
                for j in range(-1, 2, 1):  # y coordinate
                    pixel_x = x+i
                    pixel_y = y+j
                    if 0 <= pixel_x < img.width:  # pixel is include the picture
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)  # get pixel
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_pixel = img.get_pixel(x, y)
            new_pixel.red = r_sum/count
            new_pixel.green = g_sum/count
            new_pixel.blue = b_sum/count
    return img


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
