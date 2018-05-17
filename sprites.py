import pygame as pg
from settings import *

vec = pg.math.Vector2

pos_saved = vec(50, 540)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vec(50, 540)
        self.vel = vec(6,0)
        self.acc = vec(0,0)

    def update(self):
        self.acc = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # Se aplica la fricción
        self.acc += self.vel * PLAYER_FRICTION
        #Ecuaciones para el movimiento
        #self.vel += self.acc
        #self.pos += self.vel + 0.5 * self.acc
        self.pos += self.vel

        global pos_saved
        pos_saved = self.pos

        #Para que no se salga de la pantalla
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x <0:
            self.pos.x = WIDTH

        self.rect.center = self.pos
