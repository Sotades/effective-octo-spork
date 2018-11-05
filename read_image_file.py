import cv2

def read_image_file(files):
    for file in files:
        img = cv2.imread(file, flags=cv2.IMREAD_COLOR)

        yield img
