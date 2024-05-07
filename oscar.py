import cv2
import pygame
import numpy as np

# Inicializar pygame
pygame.init()

# Establecer el tamaño de la ventana
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Detección de caras")

# Cargar el clasificador de detección de caras preentrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar un frame de la cámara
    ret, frame = cap.read()
    
    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar caras en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Dibujar un rectángulo alrededor de cada cara detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Convertir la imagen de OpenCV a una superficie de pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    
    # Mostrar el frame con las caras detectadas
    window.blit(frame, (0, 0))
    pygame.display.update()
    
    # Salir del bucle si se presiona la tecla 'q'
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                cap.release()
                cv2.destroyAllWindows()
                pygame.quit()
                quit()
