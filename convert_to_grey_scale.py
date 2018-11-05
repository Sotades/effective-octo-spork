import cv2

def convert_to_grey_scale(images):
    for img in images:
        grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        yield grey_image;
