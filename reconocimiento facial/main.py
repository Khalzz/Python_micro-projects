from cv2 import cv2 #importamos cv2 (recordar que en visual studio code debemos usar "from ... import ...")

trained_file = 'haarcascade_frontalface_default.xml' #cargamos el archivo pre entrenado

face_cascade = cv2.CascadeClassifier(trained_file) #activa el metodo de deteccion por cascada de opencv
webcam = cv2.VideoCapture(0) #asignamos la webcam (de opencv) a una variable

while True: 
    (_, im) = webcam.read() 
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y), (x+w, y+h), (255,0,0), 2) #la "forma que detecta nuestro rostro" sera un rectangulo

    cv2.imshow('OpenCV', im) #mostrar imagen en la camara de cv2
    key = cv2.waitKey(10) #espera 10 ms por la tecla a presionar

    if key == 27: #si la tecla n°27 (ESC) es presionada 
        break #cerrar programa