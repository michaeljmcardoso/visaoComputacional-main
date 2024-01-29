import cv2
import face_recognition

# Coordenadas iniciais do retângulo azul
area_azul = {
    "left": 20,
    "top": 55,
    "right": 105,
    "bottom": 215
}

# Inicializar o contador de visitantes
contador_de_visitantes = 0

# Inicializar a captura de vídeo
capturaDeVideo = cv2.VideoCapture(0)

# Reduzir a resolução da imagem para melhorar o desempenho
capturaDeVideo.set(3, 440)  # Largura
capturaDeVideo.set(4, 380)  # Altura

# Nome da janela de exibição
nomeDaJanela = "Contagem de Visitantes por Detecção de Rotos"

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

            # Verificar se o rosto está dentro da área azul
            if area_azul["left"] < left < area_azul["right"] and area_azul["top"] < top < area_azul["bottom"]:
                # Incrementar o contador de visitantes
                contador_de_visitantes += 1

        # Desenhar o retângulo azul
        cv2.rectangle(frame, (area_azul["left"], area_azul["top"]), (area_azul["right"], area_azul["bottom"]), (255, 0, 0), 2)

        # Exibir as coordenadas na tela
        coordenadas_texto = f"Coordenadas: ({area_azul['left']}, {area_azul['top']}, {area_azul['right']}, {area_azul['bottom']})"
        cv2.putText(frame, coordenadas_texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Exibir a mensagem com o número de visitantes
        mensagem = f"Visitantes: {contador_de_visitantes}"
        cv2.putText(frame, mensagem, (area_azul["right"] + 10, area_azul["top"] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Exibir o quadro resultante
        cv2.imshow(nomeDaJanela, frame)

        # Controle interativo para ajustar as coordenadas do retângulo
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('a'):
            area_azul["left"] -= 5
        elif key == ord('d'):
            area_azul["left"] += 5
        elif key == ord('w'):
            area_azul["top"] -= 5
        elif key == ord('s'):
            area_azul["top"] += 5
        elif key == ord('e'):
            area_azul["right"] += 5
        elif key == ord('c'):
            area_azul["right"] -= 5
        elif key == ord('x'):
            area_azul["bottom"] += 5
        elif key == ord('z'):
            area_azul["bottom"] -= 5

    except Exception as e:
        print(f"Erro: {e}")

# Liberar recursos 
capturaDeVideo.release()
cv2.destroyAllWindows()
