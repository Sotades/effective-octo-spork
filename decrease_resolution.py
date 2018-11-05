import cv2

def decrease_resolution(images):
    for img in images:
        resized_image = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
        yield resized_image