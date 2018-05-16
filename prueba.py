import pygame, sys
from pygame.locals import *
from settings import *

colorFondo = (255,255,255)
color2= (120,120,120)

pygame.init()
ventana = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
pygame.draw.rect(ventana, color2, (0,540,1000,600))
fondo1 = pygame.image.load("imagenes\FONDO1.png")

while True:
	ventana.blit(fondo1,(0,-40))
	pygame.draw.rect(ventana, color2, (0,540,1000,600))


	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	