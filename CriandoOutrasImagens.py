import numpy as np
import cv2
import random

# Definindo as dimensões da imagem
width, height = 200, 200

# Criando uma imagem preta (fundo)
imagem = np.zeros((height, width, 3), dtype=np.uint8)

# Gerando estrelas aleatórias
num_stars = 30
for _ in range(num_stars):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    cv2.circle(imagem, (x, y), 2, (255, 255, 255), -1)  # Desenha um ponto branco

top_left = (70, 120)
bottom_right = (72, 100)
cv2.rectangle(imagem, top_left, bottom_right, color=(54, 54, 255), thickness=-1)
top_left = (128, 120)
bottom_right = (130, 100)
cv2.rectangle(imagem, top_left, bottom_right, color=(54, 54, 255), thickness=-1)

# Coordenadas dos vértices do triângulo (você pode ajustar esses valores)
vertices = []
vertices.append((90, 90))
vertices.append((60, 130))
vertices.append((90, 120))

vertices = np.array(vertices, np.int32)
vertices = vertices.reshape((-1, 1, 2))

# Desenhando o triângulo
cv2.polylines(imagem, [vertices], isClosed=True, color=(255, 255, 255), thickness=1)
cv2.fillPoly(imagem, [vertices], color=(207, 130, 48))

center_x = width // 2
center_y = height // 2

# Calculando a diferença entre o centro e as coordenadas dos vértices para espelhar
difference = center_x - vertices[:, 0, 0]
mirrored_vertices = vertices.copy()
mirrored_vertices[:, 0, 0] = center_x + difference

# Desenhando o triângulo espelhado
cv2.polylines(imagem, [mirrored_vertices], isClosed=True, color=(255, 255, 255), thickness=1)
cv2.fillPoly(imagem, [mirrored_vertices], color=(207, 130, 48))

# Desenhando o retângulo
top_left = (90, 60)
bottom_right = (110, 120)
cv2.rectangle(imagem, top_left, bottom_right, color=(255, 54, 164), thickness=-1)

top_left = (93, 120)
bottom_right = (95, 130)
cv2.rectangle(imagem, top_left, bottom_right, color=(0, 153, 255), thickness=-1)
top_left = (105, 120)
bottom_right = (107, 130)
cv2.rectangle(imagem, top_left, bottom_right, color=(0, 153, 255), thickness=-1)

# Rastro do jato
cv2.line(imagem, (93, 140), (93, 200), color=(163, 163, 163), thickness=2)
cv2.line(imagem, (107, 140), (107, 200), color=(163, 163, 163), thickness=2)

# Coordenadas dos vértices do triângulo (você pode ajustar esses valores)
vertices = []
vertices.append((100, 40))
vertices.append((90, 60))
vertices.append((110, 60))

vertices = np.array(vertices, np.int32)
vertices = vertices.reshape((-1, 1, 2))

# Desenhando o triângulo
cv2.polylines(imagem, [vertices], isClosed=True, color=(255, 255, 255), thickness=1)
cv2.fillPoly(imagem, [vertices], color=(207, 130, 48))  # Vermelho

cv2.imshow("Nave", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()