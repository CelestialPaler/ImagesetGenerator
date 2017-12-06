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


# Check if it is a valid path
# Return : Boolean
def __ispath_valid(path):
    if os.path.exists(path):
        return True
    else:
        raise Exception('ERROR : Invalid Image Diration!')


# Get all the folder in the root folder
# Args : None
# Return : None
def __get_all_folder(self):
    root = self.__image_dir_root
    dir_list = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
    self.__classes_names = dir_list


# Get all image files in the folder
# Args : None
# Return : None
def __get_all_image(self):
    print(self.__classes_names.__sizeof__())
