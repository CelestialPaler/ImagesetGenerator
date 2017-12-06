"""
########################################################################################################################
#                                              Image Dataset Generator                                                 #
#                                                 Celestial Tech Co.                                                   #
#                                               Copyright © 2015-2017                                                  #
#                                       For more check : www.tianshicangxie.com                                        #
########################################################################################################################
                        Before Using Please Read README File for tutorial and help
"""
# Code in UFT-8

import psutil
import numpy as np
from PIL import Image


# Read a single pixel data (RGB) from a image file
# Return : numpy.array(shape=[3])
def read_pixel_from_image(self, image_dir, x, y):
    if self.__ispath_valid(image_dir):
        with Image.open(image_dir) as tempimage:
            if self.__image_show is True:
                tempimage.show()
            if self.__image_reshape is True:
                tempimage = tempimage.resize(self.__image_std_shape)
            r, g, b = tempimage.getpixel((x, y))
            result = np.array([r, g, b])
            return result


# Read a single channel from a image file
# Return : numpy.matrix(shape=[imagelength, imagewidth])
def read_channel_from_image(self, image_dir, channel_name):
    if self.__ispath_valid(image_dir):
        with Image.open(image_dir) as tempimage:

            if self.__image_show is True:
                tempimage.show()
            if self.__image_reshape is True:
                tempimage = tempimage.resize(self.__image_std_shape)

            if channel_name in self.__channel_r_name:
                r, g, b = tempimage.split()
                data = np.matrix(r)
                return data
            elif channel_name in self.__channel_g_name:
                r, g, b = tempimage.split()
                data = np.matrix(g)
                return data
            elif channel_name in self.__channel_b_name:
                r, g, b = tempimage.split()
                data = np.matrix(b)
                return data
            else:
                raise Exception('ERROR : Invalid Image Channel Name!')


# Read image data from jpeg file
# Return : numpy.matrix(shape=[imagelength, imagewidth, 3])
def read_rgb_from_image(self, image_dir):
    if self.__ispath_valid(image_dir):
        with Image.open(image_dir) as tempimage:
            if self.__image_show is True:
                tempimage.show()
            if self.__image_reshape is True:
                tempimage = tempimage.resize(self.__image_std_shape)

            if self.__image_reshape is True:
                data = np.zeros(shape=[self.__image_std_length, self.__image_std_width, self.__image_std_channel])
                for x in range(self.__image_std_length):
                    for y in range(self.__image_std_width):
                        r, g, b = tempimage.getpixel((x, y))
                        data[x, y, 0] = r
                        data[x, y, 1] = g
                        data[x, y, 2] = b
                return data
            else:
                length, width = tempimage.size()
                data = np.zeros(shape=[length, width, 3])
                for x in range(length):
                    for y in range(width):
                        r, g, b = tempimage.getpixel((x, y))
                        data[x, y, 0] = r
                        data[x, y, 1] = g
                        data[x, y, 2] = b
                return data


# Close the window built by Image.show() method (Pillow package)
# Args : None
# Return : None
def kill_image_window(self):
    if self.__image_show is True:
        for proc in psutil.process_iter():
            if proc.name() == "display":
                proc.kill()













