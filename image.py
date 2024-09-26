from google.colab import drive
import cv2
from matplotlib import pyplot as plt
drive.mount('/content/drive')
image = cv2.imread('/content/drive/MyDrive/rose.jpg')  # Correct the image path if needed
if image is None:
    print("Error: Could not read the image.")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')  # Turn off the axis
    plt.show()
