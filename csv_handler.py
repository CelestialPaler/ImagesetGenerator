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
import csv


# Save image to a csv file
def __image_to_csv(self, image_dir):
    data = self.__read_rgb_from_image(image_dir)
    with open(self.__csv_dir_root + '/' + str(123) + '.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        # Loop traverse all pixels


def __data_to_csv(self, data):
    with open(self.__csv_dir_root + '/' + str(123) + '.csv', 'w', newline=''):
        pass


