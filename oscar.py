import cv2

# Cargar el clasificador de detección de caras pre-entrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iniciar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar el fotograma
    ret, frame = cap.read()
    
    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar caras en el fotograma
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Contador de caras
    num_faces = len(faces)
    
    # Dibujar un rectángulo alrededor de cada cara detectada
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, 'Cara', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
    
    # Mostrar el contador de caras en la esquina superior izquierda
    cv2.putText(frame, f'Caras: {num_faces}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Mostrar el fotograma con las caras detectadas
    cv2.imshow('Face Detection',frame)
    
    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
