import pygame, sys
from pygame.locals import *
from settings import *

pygame.init()

ventana = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)


fondo1 = pygame.image.load(fondo1_path)
suelo1 = pygame.image.load(suelo1_path)

while True:
	ventana.blit(fondo1,(0,-40))
	ventana.blit(suelo1,(0,560))


	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
