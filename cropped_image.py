import cv2
from google.colab.patches import cv2_imshow
image = cv2.imread('/content/drive/MyDrive/rose.jpg')
cv2_imshow(image)
height, width = image.shape[:2]
crop_top_left = image[0:height // 2, 0:width // 2]
crop_top_right = image[0:height // 2, width // 2:width]
crop_bottom_left = image[height // 2:height, 0:width // 2]
crop_bottom_right = image[height // 2:height, width // 2:width]
crop_center = image[height // 4:3 * height // 4, width // 4:3 * width // 4]
cv2_imshow(crop_top_left)
cv2_imshow(crop_top_right)
cv2_imshow(crop_bottom_left)
cv2_imshow(crop_bottom_right)
cv2_imshow(crop_center)
