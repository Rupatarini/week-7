import cv2
import numpy as np
import matplotlib.pyplot as plt
image_bgr = cv2.imread(' /content/drive/MyDrive/rose.jpg')
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
image_lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB))
plt.title('Original BGR Image')
plt.subplot(2, 3, 2)
plt.imshow(image_gray, cmap='gray')
plt.title('Grayscale Image')
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(image_hsv, cv2.COLOR_RGB2HSV))
plt.title('HSV Color Space')
plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(image_lab, cv2.COLOR_RGB2LAB))
plt.title('LAB Color Space')
plt.tight_layout()
plt.show()

