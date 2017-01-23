import renpygame
import renpygame as pygame
from renpygame.locals import *
import renpy.store as store
import renpy.exports as renpy
import sys
import time
from random import randint

class Ball(pygame.sprite.Sprite):
    def __init__(self, x0, x1):
        super(Ball, self).__init__()
        self.images = []
        self.images.append(pygame.image.load("img/01.png"))
        self.images.append(pygame.image.load("img/02.png"))
        self.images.append(pygame.image.load("img/03.png"))
        self.images.append(pygame.image.load("img/04.png"))
        self.images.append(pygame.image.load("img/05.png"))
        self.images.append(pygame.image.load("img/06.png"))
        self.images.append(pygame.image.load("img/07.png"))
        self.images.append(pygame.image.load("img/08.png"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect((x0, x1), (240, 240))

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


def rando_cord():
    x = [90, 150, 175, 190, 600, 550, 290, 900, 560, 400, 350, 710]
    y = [90, 100, 120, 130, 200, 400, 230, 380, 260, 190, 320, 80, 170]

    rx = x[randint(0, 11)]
    ry = y[randint(0, 12)]
    #print("X" + str(rx))
    #print("Y" + str(ry))
    return (rx, ry)


def main():
    pygame.init()

    REFRESH_RATE = 0.08
    size = 1280, 720
    screen = pygame.display.set_mode(size)
    myfont = pygame.font.Font("src/fm.otf", 50)
    pygame.mixer.init()
    startt = pygame.mixer.Sound("sound/start.wav")
    sounda = pygame.mixer.Sound("sound/mini_game.wav")
    soundo = pygame.mixer.Sound("sound/push.wav")

    to_rerender = True  # Rerender another Wave
    successo = False
    timeleft = 100
    passed = 0
    miss = 0
    onscreen = 0
    FAIL_THRES = 15
    startt.play().set_volume(0.8)
    sounda.play().set_volume(0.6)
    bg = pygame.image.load("bg.png")
    brain = pygame.image.load("brain.png")

    while True:

        label = myfont.render("TIME LEFT: " + str(timeleft / 10), 1, (153, 0, 0))

        if passed > 0 and passed < 6:
            brain = pygame.image.load("brain" + str(passed) + ".png")

        if to_rerender:
            k = rando_cord()
            sprite = Ball(k[0], k[1])
            sprites = pygame.sprite.Group(sprite)
            to_rerender = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
                # print(len(clicked_sprites))
                if len(clicked_sprites) == 1:
                    to_rerender = True
                    passed += 1
                    onscreen = 0
                    soundo.play().set_volume(0.7)
                if len(clicked_sprites) == 0:
                    miss +=1

        screen.blit(bg, (0, 0))
        sprites.update()
        screen.blit(label, (800, 50))
        screen.blit(brain, (10, 10))
        sprites.draw(screen)
        pygame.display.flip()
        if onscreen > FAIL_THRES:
            to_rerender = True
            onscreen = 0
            miss += 1
        if timeleft == 0:
            sounda.stop()
            if passed < 6 and miss > 3:
                successo = False
            else:
                successo = True
            break
        else:
            timeleft -= 1
            onscreen += 1

        time.sleep(REFRESH_RATE)
    return successo