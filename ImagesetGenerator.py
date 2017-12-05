########################################################################################################################
#                                              Image Dataset Generator                                                 #
#                                                 Celestial Tech Co.                                                   #
#                                               Copyright © 2015-2017                                                  #
#                                       For more check : www.tianshicangxie.com                                        #
########################################################################################################################

""" Image Dataset Generator
    Before Using Please Read README File for toturial and help
    Code in UFT-8
"""

import numpy as np
import os
import csv
import psutil
from PIL import Image


class TrainsetGenerator:
    def __init__(self):
        pass


class ImagesetGenerator(TrainsetGenerator):
    # Booleans Variables
    # To show image or not while processing the imagefile
    __image_show = True
    # To reshape image or not
    __image_reshape = True

    # Reshaping Configurations
    # New shape of Reshaping
    __image_std_length = 256
    __image_std_width = 256
    __image_std_channel = 3
    __image_std_shape = (__image_std_length, __image_std_width)

    # File directory
    __image_dir_root = str()
    __image_dir_ref = str()
    __csv_dir_root = str()

    # Record all the folders detected
    __classes_names = list()
    # Record all the image files detected in the folder
    __classes_images = dict()

    # Inner-work Variables
    __channel_r_name = ['R', 'r', 'RED', 'Red']
    __channel_g_name = ['G', 'g', 'GREEN', 'Green']
    __channel_b_name = ['B', 'b', 'BLUE', 'Blue']

    def __int__(self):
        pass

    ####################################################################################################################
    ''' User functions '''
    # Directory Setting #
    # Set the image root directory
    # Args : image_dir = a abspath to define where is your root folder of all image files
    # Return : None
    def set_image_root_dir(self, image_dir):
        if self.__ispath_valid(image_dir):
            self.__image_dir_root = image_dir
        return None

    # Set the csv output root directory
    # Args : dataset_dir = a abspath to define where is your root folder of csv output target folder
    # Return : None
    def set_csv_root_dir(self, dataset_dir):
        if self.__ispath_valid(dataset_dir):
            self.__csv_dir_root = dataset_dir
        return None

    # Set the standard shape in the image reshaping process
    # Args : length = the length of the image
    #        width = the width of the image
    #        channel = the number of color channel
    # Return : None
    def set_image_std(self, length, width, channel):
        if length > 0 and width > 0 and channel >= 1:
            self.__image_std_length = length
            self.__image_std_width = width
            self.__image_std_channel = channel
        else:
            raise Exception('ERROR : Invalid Standard Image Shape!')

    # Main process of the generator
    # Args : None
    # REturn : None
    def generate(self):
        if self.__isconfig_valid() is True:

            self.__get_all_folder()
            print(self.__classes_names)
            try:
                os.makedirs(self.__csv_dir_root)
            except FileExistsError:
                print('INFO : CSV Folder already exit. Continue.')
            for class_name in self.__classes_names:
                print(class_name)
                try:
                    os.makedirs(self.__csv_dir_root + '/' + class_name)
                except FileExistsError:
                    print('INFO : CSV Folder already exit. Continue.')
                '''
                for image_name in self.__classes_images[class_name]:
                    self.__image_dir_ref = '/' + class_name + '/' + image_name + '.jpg'
                    data = self.__read_rgb_from_image(self.__image_dir_root + self.__image_dir_ref)
                    self.__data_to_csv(data)
                    '''


    ####################################################################################################################
    ''' Inner-work functions '''
    # Read a single pixel data (RGB) from a image file
    # Return : numpy.array(shape=[3])
    def __read_pixel_from_image(self, image_dir, x, y):
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
    def __read_channel_from_image(self, image_dir, channel_name):
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
    def __read_rgb_from_image(self, image_dir):
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

    # Save image to a csv file
    def __image_to_csv(self, image_dir):
        data = self.__read_rgb_from_image(image_dir)
        with open(self.__csv_dir_root + '/' + str(123) + '.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            # Loop traverse all pixels

    def __data_to_csv(self, data):
        with open(self.__csv_dir_root + '/' + str(123) + '.csv', 'w', newline=''):
            pass



    ####################################################################################################################
    ''' Inner-tool functions '''
    # Check if it is a valid path
    # Return : Boolean
    @staticmethod
    def __ispath_valid(path):
        if os.path.exists(path):
            return True
        else:
            raise Exception('ERROR : Invalid Image Diration!')

    # Check if all configurations have been set correctly
    # Args : None
    # Return : None
    def __isconfig_valid(self):
        if self.__image_dir_root is str():
            raise Exception('ERROR : Directory remain unset! : Image root directory')
        elif self.__csv_dir_root is str():
            raise Exception('ERROR : Directory remain unset! : CSV root directory')
        else:
            return True

    # Get all the folder in the root folder
    # Args : None
    # Return : None
    def __get_all_folder(self):
        root = self.__image_dir_root
        dir_list = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
        print(dir_list)
        self.__classes_name = dir_list

    # Get all image files in the folder
    # Args : None
    # Return : None
    def __get_all_image(self):
        root = self.__image_dir_root

    # Close the window built by Image.show() method (Pillow package)
    # Args : None
    # Return : None
    def __kill_image_window(self):
        if self.__image_show is True:
            for proc in psutil.process_iter():
                if proc.name() == "display":
                    proc.kill()


# Debug Script
if __name__ == '__main__':
    ImagesetGen = ImagesetGenerator()
    ImagesetGen.set_image_root_dir('/home/celestial/Documents/PythonProject/ImagesetGenerator/TestImages')
    ImagesetGen.set_csv_root_dir('/home/celestial/Documents/PythonProject/ImagesetGenerator/TestCSV')
    ImagesetGen.set_image_std(256, 256, 3)
    ImagesetGen.generate()








