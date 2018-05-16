import pygame, sys
from pygame.locals import *
colorFondo = (255,255,255)

pygame.init()
ventana = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Jueguito Grupo 6")

fondo1 = pygame.image.load("imagenes\FONDO1.png")
suelo1 = pygame.image.load("imagenes\suelo.png")
while True:
	ventana.blit(fondo1,(0,-40))
	ventana.blit(suelo1,(0,560))


	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	