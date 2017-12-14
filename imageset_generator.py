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

import os
import csv_handler as csv
import image_process as ip
import toolfuncs as tool


class DatasetGenerator:
    def __init__(self):
        pass

class ImagesetGenerator(DatasetGenerator):
    # Boolean Variables
    # To show image or not while processing the imagefile
    __image_show = True
    # To reshape image or not
    __image_reshape = True

    # Reshaping Configurations
    __image_std_length = 256
    __image_std_width = 256
    __image_std_channel = 3
    __image_std_shape = (__image_std_length, __image_std_width)

    # File directory
    __image_dir_root = str()
    __csv_dir_root = str()

    # Record all the class names
    __classes_names = list()

    # Inner-work Variables
    __channel_r_name = ['R', 'r', 'RED', 'Red']
    __channel_g_name = ['G', 'g', 'GREEN', 'Green']
    __channel_b_name = ['B', 'b', 'BLUE', 'Blue']

    __subfolder_name = list()
    __subfolder_file = dict(map=[str(), list()])

    def __int__(self):
        pass

    # Directory Setting #
    # Set the image root directory
    # Args : image_dir = a abspath to define where is your root folder of all image files
    # Return : None
    def set_image_root_dir(self, image_dir):
        if tool.__ispath_valid(image_dir):
            self.__image_dir_root = image_dir
        return None

    # Set the csv output root directory
    # Args : dataset_dir = a abspath to define where is your root folder of csv output target folder
    # Return : None
    def set_csv_root_dir(self, dataset_dir):
        if tool.__ispath_valid(dataset_dir):
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

    # Set to show image or not while processing the imagefile
    # Args : boolean = True or False
    # REturn : None
    def set_show_image(self, boolean):
        if type(boolean) == bool:
            self.__image_show = boolean
        else:
            raise Exception('ERROR : Invalid Booleans!')

    # Set to reshape the image into standard shape or not while processing the imagefile
    # Args : boolean = True or False
    # REturn : None
    def set_reshape_image(self, boolean):
        if type(boolean) == bool:
            self.__image_reshape = boolean
        else:
            raise Exception('ERROR : Invalid Booleans!')

    # Main process of the generator
    # Args : None
    # REturn : None
    def generate(self):
        if self.__isconfig_valid() is True:
            tool.get_all_folder()
            tool.get_all_image()
            print(self.__classes_names)
            try:
                os.makedirs(self.__csv_dir_root)
            except FileExistsError:
                print('INFO : CSV Folder already exit. Continue.')
            for class_name in self.__classes_names:
                try:
                    os.makedirs(self.__csv_dir_root + '/' + class_name)
                except FileExistsError:
                    print('INFO : CSV sub folder already exit. Continue.')
                for image_name in self.__classes_images[class_name]:
                    image_dir_ref = '/' + class_name + '/' + image_name + '.jpg'
                    data = self.__read_rgb_from_image(self.__image_dir_root + image_dir_ref)
                    self.__data_to_csv(data)

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


# Debug Script
if __name__ == '__main__':
    ImagesetGen = ImagesetGenerator()
    ImagesetGen.set_image_root_dir('/home/celestial/Documents/PythonProject/ImagesetGenerator/TestImages')
    ImagesetGen.set_csv_root_dir('/home/celestial/Documents/PythonProject/ImagesetGenerator/TestCSV')

    ImagesetGen.set_show_image(True)
    ImagesetGen.set_reshape_image(True)
    ImagesetGen.set_image_std(256, 256, 3)

    ImagesetGen.generate()
