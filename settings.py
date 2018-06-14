import os

# Configuraciones del juego
TITLE = "Juan el Condor"
WIDTH = 1000
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
# Propiedades del jugador
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 1.5

# Path de los recursos
current_path  = os.path.dirname(__file__) # Path de donde esta ubicado el settings.py
imagenes_path = os.path.join(current_path, "imagenes") # Path de la carpeta "imagenes"
fondo1_path   = os.path.join(imagenes_path, "FONDO1.png")# Path del fondo1
fondo_mapa1   = os.path.join(imagenes_path, "mapa1.png")
fondo_mapa2   = os.path.join(imagenes_path, "mapa2.png")
boton_pausa   = os.path.join(imagenes_path, "pause.png")
flecha_D      = os.path.join(imagenes_path, "flechaD.png")
flecha_I     = os.path.join(imagenes_path, "flechaI.png")
suelo1_path   = os.path.join(imagenes_path, "suelo.png") # Path del suelo

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
