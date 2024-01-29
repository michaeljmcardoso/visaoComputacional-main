import cv2
import face_recognition

# Inicializar a captura de vídeo
capturaDeVideo = cv2.VideoCapture(0)

# Reduzir a resolução da imagem para melhorar o desempenho
capturaDeVideo.set(3, 540)  # Largura
capturaDeVideo.set(4, 380)  # Altura

# Nome da janela de exibição
nomeDaJanela = "__Contagem de Visitantes__"

# Criar a janela de exibição
cv2.namedWindow(nomeDaJanela, cv2.WINDOW_NORMAL)

# Coordenadas do retângulo azul (ajustar conforme for necessário)
areaAzul = {
    "top": 100,
    "right": 300,
    "bottom": 300,
    "left": 100
}

# Inicializar o contador de visitantes
contadorDeVisitantes = 0

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

            # Verificar se o rosto está dentro da área azul
            if areaAzul["left"] < left < areaAzul["right"] and areaAzul["top"] < top < areaAzul["bottom"]:
                # Incrementar o contador de visitantes
                contadorDeVisitantes += 1

        # Desenhar o retângulo azul
        cv2.rectangle(frame, (areaAzul["left"], areaAzul["top"]), (areaAzul["right"], areaAzul["bottom"]), (255, 0, 0), 2)

        # Exibir a mensagem com o número de visitantes
        mensagem = f"Visitantes: {contadorDeVisitantes}"
        cv2.putText(frame, mensagem, (areaAzul["right"] + 10, areaAzul["top"] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Exibir o quadro resultante
        cv2.imshow(nomeDaJanela, frame)

    except Exception as e:
        print(f"Erro: {e}")

    # Encerrar o programa ao pressionar a tecla 's' de sair
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Liberar recursos 
capturaDeVideo.release()
cv2.destroyAllWindows()
