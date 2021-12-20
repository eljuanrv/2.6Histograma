#Histograma

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('3colo.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('3colo.jpg',img)

hist = cv2.calcHist([img],[0],None,[256],[0,255])
#                    frame,canales,mask,size,range
plt.plot(hist,color='gray')
plt.xlabel('valor del gris')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()