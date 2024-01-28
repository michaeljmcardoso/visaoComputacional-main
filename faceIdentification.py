import cv2
import face_recognition

# Inicializar a captura de vídeo
capturaDeVideo = cv2.VideoCapture(0)

# Reduzir a resolução da imagem para melhorar o desempenho
capturaDeVideo.set(3, 440)  # Largura
capturaDeVideo.set(4, 380)  # Altura

# Nome da janela de exibição
nomeDaJanela = "Detecção de Rosto"

# Criar a janela de exibição
cv2.namedWindow(nomeDaJanela, cv2.WINDOW_NORMAL)

# Loop Principal
while True:
    # Ler um quadro do vídeo
    ret, frame = capturaDeVideo.read()

    try:
        # Encontrar todas os rostos no quadro
        face_locations = face_recognition.face_locations(frame)

        # Iterar sobre os rostos detectados
        for face_location in face_locations:
            # Desenhar um retângulo ao redor do rosto
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Exibir a mensagem "Rosto Detectado"
            cv2.putText(frame, "Rosto Detectado", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Exibir o quadro resultante
        cv2.imshow(nomeDaJanela, frame)

    except Exception as e:
        print(f"Erro: {e}")

    # Encerrar o programa ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos 
capturaDeVideo.release()
cv2.destroyAllWindows()
