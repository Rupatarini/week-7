import cv2
import numpy as np
from google.colab.patches import cv2_imshow
image = cv2.imread('/content/drive/MyDrive/rose.jpg')
cv2.line(image, (100, 100), (300, 300), (255, 0, 0), 3)
cv2.rectangle(image, (400, 100), (600, 300), (0, 255, 0), 2)
cv2.circle(image, (400, 100), 50, (0, 0, 255), 3)
cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
