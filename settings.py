import os

# Configuraciones del juego
TITLE = "Juan el Condor"
WIDTH = 1000
HEIGHT = 600
FPS = 30

# Path de los recursos
current_path  = os.path.dirname(__file__) # Path de donde esta ubicado el settings.py
imagenes_path = os.path.join(current_path, "imagenes") # Path de la carpeta "imagenes"
fondo1_path   = os.path.join(imagenes_path, "FONDO1.png") # Path del fondo1
suelo1_path   = os.path.join(imagenes_path, "suelo.png") # Path del suelo

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
