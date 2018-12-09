import cv2
import matplotlib.pyplot as plt
import numpy as np

def show(image,cmap = None):
    plt.imshow(image,cmap = cmap)
    plt.axis('off')
    plt.show()
    
def imread(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image