import cv2
import numpy as np
import dlib
import matplotlib.pyplot as plt
import os

# Função para realizar o cálculo de distâncias euclidianas
from scipy.spatial import distance as dist

from io import BytesIO
from IPython.display import clear_output, Image, display
from PIL import Image as Img

base_path = os.path.abspath(os.path.dirname(__file__))
predictor_path = os.path.join(base_path, 'classifiers_dlib', 'shape_predictor_68_face_landmarks.dat')

if not os.path.exists(predictor_path):
    raise Exception("Arquivo não encontrado.")

# Adquirindo o detector de faces do dlib
face_detector = dlib.get_frontal_face_detector()

# Carrega o classificador pré-treinado de pontos de referência no rosto
#landmark_predictor = dlib.shape_predictor(predictor_path) #Não funciona

# Detecta o rosto e prevê a região dos marcos faciais (landmarks)
def get_landmarks(frame):
    faces = face_detector(frame, 1)

    if len(faces) == 0:
        return None
    
    landmarks = []

    # Laço de repetição caso seja encontrado mais de um rosto
    for face in faces:
        # Adquire os landmarks do rosto detectado
        #landmarks_face = landmark_predictor(frame, face) # Descomentar caso funcionar
        landmarks_face = []

        # Adquire todos os pontos da face da iteração atual e converte para uma matriz
        landmarks_face = np.matrix([[p.x, p.y] for p in landmarks_face.parts()])

        # Adiciona os pontos de referência no array
        landmarks.append(landmarks_face)
    
    return landmarks

# Anota os pontos (marcos faciais) na imagem
def anote_landmarks(frame, landmarks):
    for land in landmarks:
        index = 1
        for center in land:
            # center é um array bi dimensional [[x, y]] então precisamos selecionar cada valor (x e y) da seguinte forma:
            x = center[0,0] # linha 0 coluna 0
            y = center[0,1] # linha 0 coluna 1

            # Adiciona o circulo no ponto do marco facial
            cv2.circle(frame, (x, y),
                       radius=2,
                       color=(255,255,0),
                       thickness=3)
            index += 1
    
    return frame

# Desenha retângulo ao encontrar faces
def note_face(frame):
    rectangles = face_detector(frame, 1)

    if len(rectangles) == 0:
        return frame
    
    for k, d in enumerate(rectangles):
        cv2.rectangle(frame, (d.left(), d.top()),
                      (d.right(), d.bottom()),
                      (255,255,0),
                      2)
    
    return frame

# Abre a camera padrão
cam = cv2.VideoCapture(0)

while True:
    # Lê o retorno da câmera, no caso, status e o frame atual
    status, frame = cam.read()

    #landmarks = get_landmarks(frame)
    #frame = anote_landmarks(frame, landmarks)

    frame = note_face(frame)

    cv2.imshow('Camera', frame)

    # Caso status da leitura da camera for false ou a tecla apertada for a letra 'Q' irá parar a aplicação
    if not status or cv2.waitKey(1) == ord('q'):
        break

# Libera a câmera
cam.release()
cv2.destroyAllWindows()