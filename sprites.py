import pygame as pg
from settings import *

vec = pg.math.Vector2

pos_saved = vec(40, HEIGHT-40)

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.pos = vec(40, HEIGHT-40)
        self.vel = vec(8,0)
        self.acc = vec(0,0)

    def jump(self):
#Verificacion si es que ha tocado el piso para que se le permita saltar denuevo
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        hitsSuelo = pg.sprite.spritecollide(self, self.game.piso, False)
        self.rect.x -= 1
        if hits or hitsSuelo:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # Se aplica la fricción
        #self.acc.x += self.vel * PLAYER_FRICTION
        #Ecuaciones para el movimiento
        self.vel += self.acc
        #self.pos += self.vel + 0.5 * self.acc
        self.pos += self.vel + 0.5 * self.acc

        global pos_saved
        pos_saved = self.pos
        #(x1,y1)= pos_saved
        #print (x1)
        #Para que no se salga de la pantalla
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x <0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Letter(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
