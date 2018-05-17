import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.pagina = 0

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        if not self.running:
            return

        self.screen.blit(pg.image.load(fondo1_path),(0,0))
        pg.draw.rect(self.screen,(255,93,85),(280,435, 440 ,65))
        self.draw_text("Iniciar", 48, WHITE, 500,440)
        xmin=280
        ymin=435
        xmax=720
        ymax=500
        pg.display.flip()
        self.pagina = 2
        self.coger_mouse(xmin,xmax,ymin,ymax)

    def show_main_menu(self):
        if not self.running:
            return

        self.screen.blit(pg.image.load(fondo_mapa1),(0,0))
        pg.draw.rect(self.screen,(203,232,186),(100,100, 780 ,250))
        self.draw_text("Macchu Picchu", 48, WHITE, 490,120)
        xmin=100
        ymin=100
        xmax=880
        ymax=350
        pg.display.flip()
        self.pagina = 3
        self.coger_mouse(xmin,xmax,ymin,ymax)

    def show_go_screen(self):
        # game over/continue
        pass

    def wait_for_a_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def coger_mouse(self,x1,x2,y1,y2):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x,y = pg.mouse.get_pos()
                        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                            waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.show_main_menu()
    g.new()
    g.show_go_screen()

pg.quit()
