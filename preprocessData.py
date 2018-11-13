import cv2
import os
import numpy as np
import bottle_functions as bf
import datetime
from tqdm import tqdm_gui
import random

# Parameters for pre-processing data
iterations = 1  # How many rounds of random iterations per image (besides the original)
target_size = 100  # target image size in % of original image
make_blur = 25  # probability of blur
set_blur = 5  # max blur to apply
make_rotate = 25  # probability of blur
set_rotate = 1  # degrees of rotation from 0
make_contrast = 25  # probability of contrast adjustment
set_contrast = 8  # amount of adjustment in %
slice_size = 70  # What is the size of the final image in percents

log = None  # None for no logging, and 1 for logging
number = 1
start_time = datetime.datetime.now()
input_folder = ['Dataset2/OK', 'Dataset2/NOK']
f = open("output_log.txt", "w")
f.write("number;filename;classification\n")

for folder in range(len(input_folder)):
    images = [img for img in os.listdir(input_folder[folder]) if img.endswith(".JPG")]
    pbar = tqdm_gui(total=len(images) * (iterations + 1), desc='processing ' + str(input_folder[folder]))

    for image in images:
        frame = cv2.imread(os.path.join(input_folder[folder], image))
        w = np.size(frame, 1)
        h = np.size(frame, 0)
        cv2.imwrite("output/" + str(input_folder[folder]) + "/" + "org_" + str(image), frame)
        f.write(str(number) + ";" + str(image) + ";" + str(input_folder[folder]) + "\n")
        number += 1
        pbar.update(1)

        for i in range(iterations):
            # Resize image
            result = bf.resize(frame, width=None, height=int(h * (target_size / 100)), inter=cv2.INTER_AREA, debug=None)

            # random transformations
            if make_rotate > random.randint(0, 100):
                result = bf.rotate(result, random.randint(set_rotate * -1, set_rotate), center=None, scale=1.0)
                # print("frame number " + str(number) + " / " + image + " done")

            if make_contrast > random.randint(0, 100):
                result = bf.adjust_gamma(result, gamma=random.randint(100 - set_contrast, 100 + set_contrast) / 100)

            if make_blur > random.randint(0, 100):
                blur = random.randint(1, set_blur)
                result = cv2.blur(result, (blur, blur))

            # Take a vertical slice from the middle
            scale = int(w / 100)
            result = bf.crop(result, 0, h, (w / 2) - (slice_size / 2 * scale), (w / 2) + (slice_size / 2 * scale),
                             debug=None)

            # Write Output and end
            cv2.imwrite("output/" + str(input_folder[folder]) + "/" + str(i) + "_" + str(image), result)
            f.write(str(number) + ";" + str(image) + ";" + str(input_folder[folder]) + "\n")
            number += 1
            pbar.update(1)
    pbar.close()

pbar.close()
f.close()
end_time = datetime.datetime.now()
print("execution time: " + str(end_time - start_time))
