import os

# Configuraciones del juego
TITLE = "Condor Dash"
WIDTH = 1000
HEIGHT = 600
FPS = 120
FONT_NAME = 'arial'
# Propiedades del jugador
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 1.5

# Plataformas iniciales
PISO = (0, HEIGHT-40, WIDTH*10, 40)

PLATFORM_LIST = [(300, HEIGHT*3/4, 100, 20)
                ,(10040, 0, 40, 600)
                ,(450, HEIGHT*3/4-100, 100, 20)
                ,(600, HEIGHT*3/4-200, 100, 20)
                ,(1500, HEIGHT*3/4-200, 100, 20)
                ,(9000, HEIGHT*3/4-200, 100, 20)
                ,(0, HEIGHT-40, WIDTH*10, 40)
                ]

COINS_LIST = [(500, 525, 25, 25),
			(700, 525, 25, 25)]

LETTERS_LIST = [(600, 525, 25, 25)]

# Path de los recursos
current_path  = os.path.dirname(__file__) # Path de donde esta ubicado el settings.py
imagenes_path = os.path.join(current_path, "imagenes") # Path de la carpeta "imagenes"
sound_path = os.path.join(current_path, "sounds")
fondo1_path   = os.path.join(imagenes_path, "FONDO1.png")# Path del fondo1
fondo_mapa1   = os.path.join(imagenes_path, "mapa1.png")
fondo_mapa2   = os.path.join(imagenes_path, "mapa2.png")
boton_pausa   = os.path.join(imagenes_path, "pause.png")
flecha_D      = os.path.join(imagenes_path, "flechaD.png")
flecha_I     = os.path.join(imagenes_path, "flechaI.png")
suelo1_path   = os.path.join(imagenes_path, "suelo.png") # Path del suelo
sonido_coin = os.path.join(sound_path, "soundCoin.wav")
sonido_letter = os.path.join(sound_path, "soundLetter.wav")
#sonido_fondo = os.path.join(sound_path, "mp.wav")
moneda_img   = os.path.join(imagenes_path, "moneda1.jpg")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
