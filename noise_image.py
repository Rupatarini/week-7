import cv2
from google.colab.patches import cv2_imshow
image = cv2.imread('/content/flower-picture.jpg')
gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)
median_blur = cv2.medianBlur(image, 7)
average_blur = cv2.blur(image, (7, 7))
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)
cv2_imshow(image)
cv2_imshow(gaussian_blur)
cv2_imshow(median_blur)
cv2_imshow(average_blur)
cv2_imshow(bilateral_blur
