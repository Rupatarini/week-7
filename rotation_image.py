import cv2
import numpy as np
from google.colab.patches import cv2_imshow
def rotate_image(image, angle):
    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_CUBIC)
    return rotated_image
image = cv2.imread('/content/drive/MyDrive/rose.jpg')
if image is None:
    print("Error: Could not read the image.")
else:
    # Rotate the image by different angles
    rotated_30 = rotate_image(image, 30)
    rotated_45 = rotate_image(image, 45)
    rotated_90 = rotate_image(image, 90)
    cv2_imshow(image)         # Original image
    cv2_imshow(rotated_30)    # Image rotated by 30 degrees
    cv2_imshow(rotated_45)    # Image rotated by 45 degrees
    cv2_imshow(rotated_90)    # Image rotated by 90 degrees
