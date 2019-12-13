import cv2
import numpy as np
 
cap = cv2.VideoCapture(1)

def nothing(x):
    pass

#Creamos una ventana llamada 'image' en la que habra todos los sliders
cv2.namedWindow('image')
cv2.createTrackbar('Hue Minimo','image',0,255,nothing)
cv2.createTrackbar('Hue Maximo','image',0,255,nothing)
cv2.createTrackbar('Saturation Minimo','image',0,255,nothing)
cv2.createTrackbar('Saturation Maximo','image',0,255,nothing)
cv2.createTrackbar('Value Minimo','image',0,255,nothing)
cv2.createTrackbar('Value Maximo','image',0,255,nothing)
 
while(1):
  _,frame = cap.read() #Leer un frame
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convertirlo a espacio de color HSV
 
  #Los valores maximo y minimo de H,S y V se guardan en funcion de la posicion de los sliders
  hMin = cv2.getTrackbarPos('Hue Minimo','image')
  hMax = cv2.getTrackbarPos('Hue Maximo','image')
  sMin = cv2.getTrackbarPos('Saturation Minimo','image')
  sMax = cv2.getTrackbarPos('Saturation Maximo','image')
  vMin = cv2.getTrackbarPos('Value Minimo','image')
  vMax = cv2.getTrackbarPos('Value Maximo','image')
 
  #Se crea un array con las posiciones minimas y maximas
  lower=np.array([hMin,sMin,vMin])
  upper=np.array([hMax,sMax,vMax])

  filter = cv2.inRange(hsv, lower, upper)

  filter = cv2.dilate(filter, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
  filter = cv2.erode(filter, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
  filter = cv2.erode(filter, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)

  result = cv2.bitwise_and(frame, frame, mask = filter)
 
  #Deteccion de colores
 
  #Mostrar los resultados y salir
  cv2.imshow('camara',frame)
  cv2.imshow('mask',result)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

