import cv2
import numpy as np
from google.colab.patches import cv2_imshow
image = cv2.imread('/content/drive/MyDrive/rose.jpg')
cv2_imshow(image)
resized_nearest = cv2.resize(image, (300, 150), interpolation=cv2.INTER_NEAREST)
cv2_imshow(resized_nearest)
resized_linear = cv2.resize(image, (300, 150), interpolation=cv2.INTER_LINEAR)
cv2_imshow(resized_linear)
resized_cubic = cv2.resize(image, (300, 150), interpolation=cv2.INTER_CUBIC)
cv2_imshow(resized_cubic)
resized_area = cv2.resize(image, (300, 150), interpolation=cv2.INTER_AREA)
cv2_imshow(resized_area)
cv2.waitKey(0)
cv2.destroyAllWindows()
