import pygame,sys
from pygame.locals import *

color = (0,140,60)

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("FlappyCondor")

while True:
    ventana.fill(color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
