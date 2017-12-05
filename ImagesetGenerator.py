########################################################################################################################
#                                              Image Dataset Generator                                                 #
#                                                 Celestial Tech Co.                                                   #
#                                               Copyright © 2015-2017                                                  #
#                                       For more check : www.tianshicangxie.com                                        #
########################################################################################################################
# Code in UFT-8 #
# Before Using Please Read README File for toturial and help

import numpy as np
import os
import csv
import psutil
from PIL import Image


class TrainsetGenerator:
    def __init__(self):
        pass


class ImagesetGenerator(TrainsetGenerator):
    # To show image or not while processing the imagefile
    __image_show = True
    # To reshape image or not
    __image_reshape = True
    # New shape of Reshaping
    __image_std_length = 256
    __image_std_width = 256
    __image_std_channel = 3
    __image_std_shape = (__image_std_length, __image_std_width)
    # Num of Image to build dataset
    __image_num = 1000

    # File diractions
    __image_dir_root = str()
    __image_dir_ref = str()
    __csv_dir_root = str()

    # Record all the folders detected
    __classes_name = list()

    # Some WTF
    __channel_r_name = ['R', 'r', 'RED', 'Red']
    __channel_g_name = ['G', 'g', 'GREEN', 'Green']
    __channel_b_name = ['B', 'b', 'BLUE', 'Blue']

    def __int__(self):
        pass

    ####################################################################################################################
    ''' User functions '''
    # Set the image root diraction
    # Return : None
    def set_image_root_dir(self, image_dir):
        if self.__isvalid_path(image_dir):
            self.__image_dir_root = image_dir
        return None

    # Set the standard shape in the image reshaping process
    # Return : None
    def set_image_std(self, length, width, channel):
        if length > 0 and width > 0 and channel >= 1:
            self.__image_std_length = length
            self.__image_std_width = width
            self.__image_std_channel = channel
        else:
            raise Exception('ERROR : Invalid Standard Image Shape!')

    ####################################################################################################################
    ''' Inner-work functions '''
    # Read a single pixel data (RGB) from a image file
    # Return : numpy.array(shape=[3])
    def __read_pixel_from_image(self, image_dir, x, y):
        if self.__isvalid_path(image_dir):
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
    def __read_channel_from_image(self, image_dir, channel_name):
        if self.__isvalid_path(image_dir):
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
    def __read_rgb_from_image(self, image_dir):
        if self.__isvalid_path(image_dir):
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

    def __image_to_csv(self, image_dir):
        data = self.__read_rgb_from_image(image_dir)
        with open(self.__csv_dir_root + '/' + str(index) + '.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            # Loop traverse all pixels
            for x in range(norm_length):
                for y in range(norm_length):
                    csvwriter.writerow(image_data[x][y][:])



    ####################################################################################################################
    ''' Inner-tool functions '''
    # Check if it is a valid path
    # Return : Boolean
    @staticmethod
    def __isvalid_path(path):
        if os.path.exists(path):
            return True
        else:
            raise Exception('ERROR : Invalid Image Diration!')

    # Get all the folder in the root folder
    # Return : None
    def __get_all_folder(self):
        root = self.__image_dir_root
        dir_list = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
        self.__classes_name = dir_list

    # Close the window built by Image.show() method (Pillow package)
    # Return : None
    def __kill_image_window(self):
        if self.__image_show is True:
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()


# Debug Script
if __name__ == '__main__':
    ImagesetGen = ImagesetGenerator()
    ImagesetGen.set_image_root_dir('/home/celestial/PythonProject/TFTest')
    ImagesetGen.read_channel_from_image()