import os

# Configuraciones del juego
TITLE = "Condor Dash"
WIDTH = 1000
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
# Propiedades del jugador
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 1.5

#Obstaculos
#,(1000, 520, 30, 40)
#,(1000, 480, 30, 100)
# Plataformas iniciales
PLATFORM_LIST = [(10040, 0, 40, 600)
				#,(300, HEIGHT*3/4, 100, 20)                
                ,(300, 520, 30, 40)
                ,(450, 480, 30, 100)
                ,(600, 440, 30, 140)
                ,(700, HEIGHT*3/4-100, 100, 30)
                ,(900, HEIGHT*3/4, 100, 30)
                ,(1100, 350, 30, 250)
                ,(1400, 520, 30, 40)
                ,(1550, 480, 30, 80)
                ,(1700, 520, 30, 40)
                ,(1850, 480, 30, 80)
                ,(2000, 520, 30, 40)
                ,(2150, 480, 30, 80)
                ,(2300, 520, 30, 40)
                ,(2450, 480, 30, 80)
                ,(2600, 520, 30, 40)
                ,(2800, HEIGHT*3/4, 100, 30)
                ,(3000, HEIGHT*3/4-100, 100, 30)
                ,(3200, HEIGHT*3/4-200, 100, 30)
                ,(3400, HEIGHT*3/4-150, 100, 30)
                ,(2900, 520, 30, 40)
                ,(3000, 520, 30, 40)
                ,(3100, 520, 30, 40)
                ,(3200, 520, 30, 40)
                ,(3300, 520, 30, 40)
                ,(3400, 520, 30, 40)
                ,(3500, 520, 30, 40)
                ,(3600, 520, 30, 40)
                ,(4000, HEIGHT*3/4, 100, 30)
                ,(4200, HEIGHT*3/4-100, 100, 30)
                ,(4400, HEIGHT*3/4-200, 100, 30)
                ,(4600, HEIGHT*3/4-200, 100, 30)
                ,(4800, HEIGHT*3/4-200, 100, 30)
                ,(5000, HEIGHT*3/4-100, 100, 30)
                ,(5200, HEIGHT*3/4-200, 100, 30)

                #,(600, HEIGHT*3/4-200, 100, 20)
                #,(1500, HEIGHT*3/4-200, 100, 20)
                #,(9000, HEIGHT*3/4-200, 100, 20)
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
