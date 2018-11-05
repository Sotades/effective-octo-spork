import cv2

def write_image_file(images):
    for img in images:
        output_file = cv2.imwrite('output_files/test_image.jpg', img)

        yield output_file