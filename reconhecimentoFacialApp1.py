import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Carregando o modelo treinado
model = load_model('/home/import_michael/Documentos/Backup/visaoComputacional/modeloReconhecimentoFacialIdentificacaoDeEmocoes.h5') 

# Inicializando a webcam
cap = cv2.VideoCapture(0)  # 0 representa a câmera padrão, mas pode variar dependendo do seu sistema

# Loop principal
while True:
    # Capturando o frame da webcam
    ret, frame = cap.read()

    # Detectando rostos no frame
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Processando cada rosto detectado
    for (x, y, w, h) in faces:
        # Pré-processamento da imagem para corresponder ao formato de entrada do modelo
        roi = frame[y:y + h, x:x + w]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(roi, (48, 48))
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        roi = preprocess_input(roi)

        # Fazendo previsões com o modelo
        prediction = model.predict(roi)

        # Convertendo a previsão em uma emoção
        emotion_labels = ["Emoção 1", "Emoção 2", "Emoção 3", "Emoção 4", "Emoção 5", "Emoção 6"]
        emotion = emotion_labels[np.argmax(prediction)]

        # Exibindo o resultado na janela da webcam
        cv2.putText(frame, f"Emoção: {emotion}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (36, 255, 12), 2)

    # Exibindo o frame na janela da webcam
    cv2.imshow('Webcam Emotion Detection', frame)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando os recursos
cap.release()
cv2.destroyAllWindows()
