import cv2
import os

amostra = 'aluno'
numeroAmostra = 20
largura, altura = 220, 220

classificadorFace = cv2.CascadeClassifier('content/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
count = 0

# Dicionário para mapear IDs para nomes
id_para_nome = {}

# Função para cadastrar um novo aluno e associar um nome a ele
def cadastrar_novo_aluno():
    nome = input("Digite o nome do aluno: ")
    id_aluno = int(input("Digite o ID do aluno: "))
    id_para_nome[id_aluno] = nome

# Solicitar cadastro de novo aluno
cadastrar_novo_aluno()

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
            # Obtém o nome associado ao ID
            nome_aluno = id_para_nome.get(id, "Desconhecido")
            cv2.imwrite(f"imagens/ra{id}.{amostra}.{count}.jpg", imagemFace)
            print(f"[Foto {count + 1} capturada com sucesso para o aluno {nome_aluno}]")
            count += 1
            if count >= numeroAmostra:
                break

cap.release()
cv2.destroyAllWindows()

# Restante do seu código permanece o mesmo
