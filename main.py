import cv2
import os

amostra = 'aluno'
numeroAmostra = 20
largura, altura = 220, 220

classificadorFace = cv2.CascadeClassifier('content/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
count = 0

# Leer los datos del formulario desde el archivo
with open("dados_aluno.txt", "r") as f:
    ra = f.readline().strip()
    nombre = f.readline().strip()
    professor = f.readline().strip()
    senha = f.readline().strip()

# Dicionário para mapear IDs para nomes
id_para_nome = {int(ra): nombre}

# Función para cadastrar un novo aluno y associar un nome a él
def cadastrar_novo_aluno():
    return int(ra)

# Solicitar cadastro de novo aluno
id_aluno = cadastrar_novo_aluno()

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
            nome_aluno = id_para_nome.get(id_aluno, "Desconhecido")
            cv2.imwrite(f"imagens/ra{id_aluno}.{amostra}.{count}.jpg", imagemFace)
            print(f"[Foto {count + 1} capturada com sucesso para o aluno {nome_aluno}]")
            count += 1
            if count >= numeroAmostra:
                break

# Señal de éxito
with open("captura_exitosa.txt", "w") as f:
    f.write("Captura de fotos exitosa")

cap.release()
cv2.destroyAllWindows()
