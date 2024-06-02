import cv2
import os

amostra = 'aluno'
numeroAmostra = 20
id = input('Digite seu identificador: ')
largura, altura = 220, 220

classificadorFace = cv2.CascadeClassifier('content/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
count = 0

while count < numeroAmostra:
    conectado, frame = cap.read()
    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificadorFace.detectMultiScale(frameCinza)
    for (x, y, w, h) in facesDetectadas:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)

    if key == 27 and len(facesDetectadas) > 0:  # Pressione ESC para capturar a imagem
        for (x, y, w, h) in facesDetectadas:
            imagemFace = cv2.resize(frameCinza[y:y + h, x:x + w], (largura, altura))
            if not os.path.exists('imagens'):
                os.makedirs('imagens')
            cv2.imwrite(f"imagens/ra{id}.{amostra}.{count}.jpg", imagemFace)
            print(f"[Foto {count + 1} capturada com sucesso]")
            count += 1
            if count >= numeroAmostra:
                break

cap.release()
cv2.destroyAllWindows()
