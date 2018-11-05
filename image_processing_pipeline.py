import os
import cv2
import tubo
from os import listdir
from os.path import isfile, join
from read_image_file import read_image_file
from convert_to_grey_scale import convert_to_grey_scale
from decrease_resolution import decrease_resolution


input_folder = 'input_files/'
directory = os.fsencode(input_folder)

# Generate list of files to process
files = [(input_folder + f) for f in listdir(input_folder) if isfile(join(input_folder, f))]

# Pipeline to process all files in directory in a sequential manner
output = tubo.pipeline(
    files,
    read_image_file,
    convert_to_grey_scale,
    decrease_resolution,
)

filenum = 0

# 'output' is a generator - very efficient memory usage
for output_image in output:
    filenum += 1
    file_name = 'output_files/file_' + str(filenum) + '.jpg'
    output_file = cv2.imwrite(file_name, output_image)



