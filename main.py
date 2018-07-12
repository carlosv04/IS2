import pygame as pg
import random
from settings import *
from sprites import *

pagina = 0
use_pos_saved = True

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

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.piso = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.letters = pg.sprite.Group()
        self.player = Player(self)
        global use_pos_saved
        global pos_saved
        global contMonedas
        contMonedas = 0
        global contLetras
        contLetras = 0
        global mapita
        if use_pos_saved:
            self.player.pos = pos_saved
        self.all_sprites.add(self.player)

        
        #print (mapita)

        global nMapa
        global nCoin
        global nLet

        if mapita == 1:

            for plat in PLATFORM_LIST:
                p = Platform(*plat)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for coin in COINS_LIST:
                c = Coin(*coin)
                self.all_sprites.add(c)
                self.coins.add(c)

            for letter in LETTERS_LIST:
                l = Letter(*letter)
                self.all_sprites.add(l)
                self.letters.add(l)
        elif mapita == 2:
            for plat in nMapa:
                (a,b) = plat
                p = Platform(a*10,b-10,30,30)
                #p = Platform(*plat)
                self.all_sprites.add(p)
                self.platforms.add(p)
            
            p = Platform(0, HEIGHT-40, WIDTH*10, 40)
            self.all_sprites.add(p)
            self.platforms.add(p)
            for coin in nCoin:
                (a,b)= coin
                c = Coin(a*10, b-10, 25, 25)
                self.all_sprites.add(c)
                self.coins.add(c)

            for letter in nLet:
                (a,b)=letter
                l = Letter(a*10, b-10, 25, 25)
                self.all_sprites.add(l)
                self.letters.add(l)

        suelo = Platform(*PISO)
        self.all_sprites.add(suelo)
        self.piso.add(suelo)
        #pg.mixer.Sound.play(pg.mixer.Sound(sonido_fondo))
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        #global pagina
        #pagina = 3

    def update(self):
        #global dato
        # Game Loop - Update
        self.all_sprites.update()
        pg.draw.rect(self.screen,(221, 221, 188),(100,10, 800 ,10))
        # Verificacion si el jugador ha tocado la plataform - solo mientras cae
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player.vel.y > 0:
            hitsPiso = pg.sprite.spritecollide(self.player, self.piso, False)
            if hitsPiso:
                self.player.pos.y = hitsPiso[0].rect.top
                self.player.vel.y = 0

        # Si el jugador alcanza 1/2 de la pantalla
        if self.player.rect.right >= WIDTH/4:
            self.player.pos.x -= abs(self.player.vel.x)
            for plat in self.all_sprites:
                #print(plat.rect.x)
                plat.rect.x -= abs(self.player.vel.x)
                if plat.rect.right <= 0:
                   pass
                   plat.kill()
            for i in self.platforms:
                dato = abs(i.rect.x)

            print(dato)

            pg.draw.rect(self.screen,(255, 0, 0),(100,10, dato*8/100 ,10))

        # Lógica cuando muere el jugador
        hitsLateral = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hitsLateral:
           #print(self.player.rect.right)
            #print(hitsLateral[0].rect.left)
            if hitsLateral[0].rect.left <= self.player.rect.right - 8 and hitsLateral[0].rect.left >= self.player.rect.right - 18:
                global pos_saved
                pos_saved = vec(40, HEIGHT-40)
                self.playing = False
                global pagina
                pagina = 5
                #print("Se chocó")

        #Generar más plataformas aleatoriamente
  #      while len(self.platforms) < 7:
   #         width = random.randrange(50, 100)
    #        p = Platform(random.randrange(WIDTH, WIDTH*2), random.randrange(HEIGHT*3/4, HEIGHT*3/4 + width), width, 20)
     #       self.platforms.add(p)
      #      self.all_sprites.add(p)

        hitsCoins = pg.sprite.spritecollide(self.player, self.coins, False)
        hitsLetters = pg.sprite.spritecollide(self.player, self.letters, False)
        #hitSalida = pg.sprite.spritecollide(self.player, self.salida, False)
        global contMonedas
        pg.draw.rect(self.screen,WHITE,(0,0, 100 ,20))
        self.draw_text("Monedas: {}/{}".format(contMonedas, len(self.coins)+ contMonedas), 16, BLACK, 40,0)

        if hitsCoins:
            hitsCoins[0].kill()
            contMonedas += 1
            print(contMonedas)
            pg.mixer.Sound.play(pg.mixer.Sound(sonido_coin))
        global contLetras
        pg.draw.rect(self.screen,WHITE,(905,0, 95 ,20))
        self.draw_text("Letras: {}/{}".format(contLetras, len(self.letters)+contLetras), 16, BLACK, 940,0)
        if hitsLetters:
            hitsLetters[0].kill()
            contLetras += 1
            print(contLetras)
            pg.mixer.Sound.play(pg.mixer.Sound(sonido_letter))

    def events(self):
        image_pausa = pg.image.load(boton_pausa)
        x1 = 930
        x2 = x1 + image_pausa.get_rect().width
        y1 = 70
        y2 = y1 + image_pausa.get_rect().height
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = pg.mouse.get_pos()
                    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                        self.playing = False
                        global pagina
                        pagina = 3
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        global pos_saved
        global monedas
        #global dato
        (xa,ya)= pos_saved
        # Game Loop - draw
        self.screen.blit(pg.image.load(fondo_mapa1),(0,20))
        self.screen.blit(pg.image.load(suelo1_path),(0,560))
        self.screen.blit(pg.image.load(boton_pausa),(930,70))
        #pg.draw.rect(self.screen,(221, 221, 188),(100,10, 800 ,10))
        #print(xa)
        if xa >800:
            xa=800
        #pg.draw.rect(self.screen,(255, 0, 0),(100,10, dato ,10))
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        #pg.draw.rect(self.screen,(4, 56, 255),(500,525, 25 ,25))
        #if player.pos.x > 500 && player.pos.x < 525 &&
        # *after* drawing everything, flip the display
        pg.display.flip()

    def on_pausa(self):
        if not self.running:
            return

        self.screen.blit(pg.image.load(fondo_mapa1),(0,0))
        self.draw_text("Menú de Pausa", 60, BLACK, 500,60)

        pg.draw.rect(self.screen,(255,93,85),(400,190, 200 ,50))
        self.draw_text("Resumen", 30, WHITE, 500,200)
        pg.draw.rect(self.screen,(255,93,85),(400,260, 200 ,50))
        self.draw_text("Reiniciar", 30, WHITE, 500,270)
        pg.draw.rect(self.screen,(255,93,85),(400,330, 200 ,50))
        self.draw_text("Menu Mapas", 30, WHITE, 500,340)
        pg.draw.rect(self.screen,(255,93,85),(400,400, 200 ,50))
        self.draw_text("Salir", 30, WHITE, 500,410)

        xmin=280
        ymin=435
        xmax=720
        ymax=500
        pg.display.flip()
        global pagina
        global use_pos_saved

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = pg.mouse.get_pos()
                    if x >= 400 and x <= 600 and y >= 190 and y <= 240:
                        #va a la pagina del juego
                        pagina = 2
                        use_pos_saved = True
                    elif x >= 400 and x <= 600 and y >= 260 and y <= 310:
                        #reinicia la partida
                        pagina = 2
                        use_pos_saved = False
                    elif x >= 400 and x <= 600 and y >= 330 and y <= 380:
                        #va al menu de mapas
                        pagina = 1
                    elif x >= 400 and x <= 600 and y >= 400 and y <= 450:
                        #sale del juego
                        self.running = False

    def show_start_screen(self):
        if not self.running:
            return

        global mapita
        mapita = 1
        global nMapa
        nMapa = None
        global nCoin
        nCoin = None
        global nLet
        nLet = None

        self.screen.blit(pg.image.load(fondo1_path),(0,0))
        #Logocondor_img
        self.screen.blit(pg.image.load(Logocondor_img),(200,0))
        #boton_inicio
        picture = pg.image.load(boton_inicio)
        picture = pg.transform.scale(picture, (440, 160))
        self.screen.blit(picture,(280,390))
        #pg.draw.rect(self.screen,(255,93,85),(280,435, 440 ,65))
        self.draw_text("Iniciar", 48, WHITE, 500,440)
        xmin=280
        ymin=435
        xmax=720
        ymax=500
        pg.display.flip()
        #self.pagina = 1
        self.coger_mouse(xmin,xmax,ymin,ymax)
        #solo podemos ir a la pagina Main Menu
        global pagina
        pagina = 1

    def pantalla_maker(self):
        if not self.running:
            return

        fondo_mapas = fondo_mapa1
        flechaR = flecha_Reg
        parar = clear_icon
        #self.screen.blit(pg.image.load(fondo_mapas),(0,0))
        pg.draw.rect(self.screen,(204,204,179),(0,0, WIDTH ,HEIGHT))
        pg.draw.rect(self.screen,(255,255,0),(0,560, WIDTH ,40))
        pg.draw.rect(self.screen,(0,0,0),(0,90, WIDTH ,5))

        picture = pg.image.load(ladrillo_img)
        picture = pg.transform.scale(picture, (60, 60))
        self.screen.blit(picture,(115,15))

        picture = pg.image.load(moneda_img)
        picture = pg.transform.scale(picture, (60, 60))
        self.screen.blit(picture,(215,15))

        picture = pg.image.load(letra_img)
        picture = pg.transform.scale(picture, (60, 60))
        self.screen.blit(picture,(315,15))

        self.screen.blit(pg.image.load(flechaR), (15,15))
        self.screen.blit(pg.image.load(parar), (415,15))

        #opciones para seleccionar
        #pg.draw.rect(self.screen,(255,255,0),(115,15, 60 ,60))
        #pg.draw.rect(self.screen,(255,0,0),(215,15, 60 ,60))
        #pg.draw.rect(self.screen,(0,0,255),(315,15, 60 ,60))
        #pg.display.flip()
        global pagina
        global nMapa
        global nCoin
        global nLet
        global obj
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = pg.mouse.get_pos()
                    dato = (x,y)
                    #obj = 0
                    if x>= 15 and x <=79 and y>=15 and y<=79:
                        pagina = 1
                    if x>= 115 and x<= 175 and y>=15 and y <=75:
                        obj = 1
                    if x>= 215 and x<= 275 and y>=15 and y <=75:
                        obj = 2
                    if x>= 315 and x<= 375 and y>=15 and y <=75:
                        obj = 3
                    if x>= 415 and x<= 475 and y>=15 and y <=75:
                        obj = 0

                    if x>= 0 and x<= WIDTH and y>=90 and y <=HEIGHT:
                        if obj == 1:
                            nMapa.append(dato)
                        if obj == 2:
                            nCoin.append(dato)                            
                        if obj == 3:
                            nLet.append(dato)                            
                    for m in nMapa:
                        #print (m)
                        a,b = m
                        picture = pg.image.load(ladrillo_img)
                        picture = pg.transform.scale(picture, (10, 10))
                        self.screen.blit(picture,(a,b))

                        #pg.draw.rect(self.screen,(255,255,0),(a,b, 10 ,10))
                    for m in nCoin:
                        a,b = m
                        picture = pg.image.load(moneda_img)
                        picture = pg.transform.scale(picture, (10, 10))
                        self.screen.blit(picture,(a,b))

                    for m in nLet:
                        a,b = m
                        picture = pg.image.load(letra_img)
                        picture = pg.transform.scale(picture, (10, 10))
                        self.screen.blit(picture,(a,b))

                    pg.display.flip()
    def show_main_menu(self):
        if not self.running:
            return
        fondo_mapas = fondo_mapa1
        posx = 1000
        tam = 780


        #self.screen.blit(pg.image.load(fondo_mapa1),(0,0))
        global mapita
        if mapita == 1:
            self.screen.blit(pg.image.load(fondo_mapa1),(0,0))
            pg.draw.rect(self.screen,(203,232,186),(100,100, 780 ,250))
            self.draw_text("Macchu Picchu", 48, WHITE, 490,120)
        elif mapita == 2:
            #mapa 2
            self.screen.blit(pg.image.load(fondo_mapa2),(0,0))
            pg.draw.rect(self.screen,(203,232,186),(100,100, 780 ,250))
            self.draw_text("Chan Chan", 48, WHITE, 490,120)
        #flechas
        self.screen.blit(pg.image.load(flecha_D),(920,180))
        self.screen.blit(pg.image.load(flecha_I),(15,180))
        #Maker
        picture = pg.image.load(boton_maker)
        picture = pg.transform.scale(picture, (300, 80))
        self.screen.blit(picture,(350,440))
        #pg.draw.rect(self.screen,(68, 204, 0),(350,450, 300 ,60))
        self.draw_text("Maker", 48, WHITE, 500,450)

        xmin=100
        ymin=100
        xmax=880
        ymax=350
        #pg.display.flip()
        sw= False
        global pagina
        global nMapa
        global nCoin
        global nLet
        global obj
        #cantidad de mapas
        totalmapas = 2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x,y = pg.mouse.get_pos()
                    if x >= 100 and x <= 880 and y >= 100 and y <= 350:
                        if nMapa == None:
                            nMapa = [(1000, 530)]
                        if nCoin == None:
                            nCoin = [(-10, 530)]
                        if nLet == None:
                            nLet = [(-10, 530)]
                        pagina = 2
                    elif x >= 350 and x <= 650 and y >= 450 and y <= 510:

                        nMapa = []
                        nCoin = []
                        nLet = []
                        obj = 0
                        pagina = 4
                    elif x >= 920 and x <= 984 and y >= 180 and y <= 244:
                        if mapita == totalmapas:
                            mapita = totalmapas
                        else:
                            mapita = mapita + 1
                    elif x >= 15 and x <= 79 and y >= 180 and y <= 244:
                        if mapita > 1:
                            mapita = mapita - 1
                        else:
                            mapita = 1
                        '''while sw:

                            fondo_mapas = fondo_mapa2
                            pg.draw.rect(self.screen,(203,232,186),(posx,100, tam ,250))
                            posx -= 5
                            tam -=5
                            print(posx)
                            if posx < 0:
                                sw = False
                            pg.display.update()'''

                    #self.coger_mouse(xmin,xmax,ymin,ymax)
                    #por el momento solo iremos a la pagina del juego

                    #pagina = 2
        #self.pagina = 2
        #self.coger_mouse(xmin,xmax,ymin,ymax)
        #por el momento solo iremos a la pagina del juego
        #global pagina
        #pagina = 2
        pg.display.flip()


    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(BLACK)
        self.draw_text("Estas Muerto :(", 48, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text("Presiona alguna tecla para empezar de nuevo", 22, WHITE, WIDTH/2, HEIGHT/2)
        pg.display.flip()
        self.wait_for_a_key()
        global pagina
        global use_pos_saved
        pagina = 2
        use_pos_saved = False

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
    if pagina == 1:
        g.show_main_menu()
    elif pagina == 2:
        g.new()
    elif pagina == 3:
        g.on_pausa()
    elif pagina == 4:
        g.pantalla_maker()
    elif pagina == 5:
        g.show_go_screen()
#    g.show_main_menu()
#    g.show_go_screen()



pg.quit()
