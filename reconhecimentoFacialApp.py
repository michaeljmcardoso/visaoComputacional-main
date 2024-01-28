import cv2
import face_recognition
from playsound import playsound

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)

# Reduzir a resolução da imagem para melhorar o desempenho
cap.set(3, 340)  # Largura
cap.set(4, 280)  # Altura

# Loop Principal
while True:
    # Ler um quadro do vídeo
    ret, frame = cap.read()

    try:
        # Encontrar todas os rostos no quadro
        face_locations = face_recognition.face_locations(frame)
        face_landmarks = face_recognition.face_landmarks(frame)

        # Iterar sobre os rostos detectados
        for face_location, landmarks in zip(face_locations, face_landmarks):
            # Extrair os pontos chave para os olhos e a boca
            left_eye = landmarks['left_eye']
            right_eye = landmarks['right_eye']
            mouth = landmarks['bottom_lip']

            # Calcular a diferença de altura entre os olhos e a boca
            eye_avg_y = (left_eye[1][1] + right_eye[4][1]) / 2
            mouth_avg_y = (mouth[0][1] + mouth[6][1]) / 2

            diff_y = eye_avg_y - mouth_avg_y

            # Identificação da Expressão Facial
            threshold_happy = -115
            threshold_sad = -95

            if diff_y < threshold_happy:
                emotion = "Feliz"
                #playsound("happy_alert.mp3")
            elif diff_y > threshold_sad:
                emotion = "Triste"
                #playsound("sad_alert.mp3")
            else:
                emotion = "Serio"

            # Desenhar um retângulo ao redor do rosto e mostrar a emoção
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f"Emocao: {emotion}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    except Exception as e:
        print(f"Erro: {e}")

    # Exibir o quadro resultante
    cv2.imshow("Reconhecimento Facial", frame)

    # Encerrar o programa ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos 
cap.release()
cv2.destroyAllWindows()
