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
# Return : True or Error
def is_path_valid(path):
    if os.path.exists(path):
        return True
    else:
        raise Exception('ERROR : Invalid Directory!')


# Get all the sub folder`s name in a root folder
# Args : folder_dir = a abspath to the target folder
# Return : list()
def get_all_folder(folder_dir):
    temp_list = [item for item in os.listdir(folder_dir)
                 if os.path.isdir(os.path.join(folder_dir, item))]
    return temp_list


# Get all image files in the folder1
# Args : folder_dir = a abspath to the target folder
# Return : list()
def get_all_image(folder_dir):
    temp_list = list()
    for file in os.listdir(folder_dir):
        if file.endswith(".jpg"):
            temp_list.append(file)
    return temp_list


# Get all the image files in the folder
# Args : folder_dir = a abspath to the target folder
# Return : dict()
def get_all_image_dicts(folder_dir):
    temp_dict = dict()
    names = get_all_folder(folder_dir)
    for name in names:
        href_dir = '/' + str(name)
        templist = sorted(get_all_image(root_dir + href_dir))
        temp_dict.update({name: templist})
    return temp_dict


# Create target folders to contain the csv files of each classes
def create_target_folders(folder_dir):
    if os.path.exists(folder_dir):
        names = get_all_folder(root_dir)
        for name in names:
            href_dir = '/' + str(name)
            try:
                os.makedirs(folder_dir + href_dir)
            except OSError:
                pass
                # raise Exception('ERROR : Target Directory Already Exits!')
    else:
        raise Exception('ERROR : Invalid Target Directory!')


# Debug Script
if __name__ == '__main__':
    root_dir = '/home/celestial/Documents/PythonProject/ImagesetGenerator/TestImages'
    target_dir = '/home/celestial/Documents/PythonProject/ImagesetGenerator/TestCSV'
    images = get_all_image_dicts(root_dir)
    create_target_folders(target_dir)
    print(images)
