#INDICACIONES
#Debe tener la imagen de las figuras llamada 3colo.jpg
#   guardada en la carpeta predeterminada de python


#Histograma
from __future__ import division
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('3colo.jpg', cv2.IMREAD_GRAYSCALE)

ret,thresh4 = cv2.threshold(img,140,255,cv2.THRESH_TOZERO)
#Bajo un valor umbral muestra los grises originales
#y lo demas a 0
ret,thresh5 = cv2.threshold(thresh4,185,255,cv2.THRESH_TOZERO_INV)
#Valor umbral y tonalidad maxima
ret,thresh2 = cv2.threshold(thresh5,100,255,cv2.THRESH_BINARY_INV)
 
 #guardar y leer imagen
cv2.imwrite('umbralizada.jpg',thresh2)
img2 = cv2.imread('umbralizada.jpg')

#negro y mas negro
lower = (160,0,16)
upper = (160,0,0)

#bgr a hsv
frameHSV = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
#mask = cv2.inRange(frameHSV,azulClaro,azulOscuro)

# threshold on black in hsv
thresh = cv2.inRange(frameHSV, lower, upper)
result = np.zeros_like(thresh)

contornos,_=cv2.findContours(thresh5,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#retr_external: solo se queda con los contornos externos

#chain approx simple encierra al contorno en cuantro puntos
#variable contornos es vectorial
for c in contornos:
    area =  cv2.contourArea(c)
    if area > 4000:              #contourldx (0,-1), color, line tipe
        cv2.drawContours(result, [c], -1, 255, cv2.FILLED)
        area_total=area

cv2.imwrite('limpia.jpg',result)
not_noise = cv2.imread('limpia.jpg',0)
cv2.imshow('Sin ruido', not_noise)

area_total=0
for renglon in range(417):
    for columna in range(626):
        if not_noise[renglon,columna]==255:
            area_total+=1

print()
print(f'Total proximado de pixeles verdes: {area_total}')


hist = cv2.calcHist([img],[0],None,[256],[0,255])
#                    frame,canales,mask,size,range
plt.plot(hist,color='gray')
plt.xlabel('valor del gris')
plt.ylabel('cantidad de pixeles')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

