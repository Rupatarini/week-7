import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("/content/drive/MyDrive/chess.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)
harris_corners = cv2.cornerHarris(gray_img, blockSize=2, ksize=3, k=0.04)
harris_corners = cv2.dilate(harris_corners, None)
img[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]
plt.figure(figsize=(10, 5))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Harris Corners')
plt.axis('off')

