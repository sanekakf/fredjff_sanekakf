import pygame
import random
import os

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
#НАЧАЛЬНЫЙ ЗАПУСК
pygame.init()

#папка игры
ff=os.path.dirname(__file__)
pimg=pygame.image.load(os.path.join(ff, 'jplayer.png'))
#создание всего нужного
width = 800
height = 600
fps=60

#цвета
purple_haze=(160,0,200)
gold = (255,190,0)

#класс
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pimg
        # self.image.fill(gold)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

    #обнова картинки, и движения
    def update(self):
        self.speedx=0
        self.speedy=0
        key = pygame.key.get_pressed()

        #выступы-заскоки
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > height:
            self.rect.top = height
        if self.rect.bottom < 0:
            self.rect.bottom = 0
        #движение
        if key[K_LEFT]:
            self.speedx = -8
        if key[K_RIGHT]:
            self.speedx = 8
        if key[K_UP]:
            self.speedy = 8
        if key[K_DOWN]: 
            self.speedy = -8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
#запуск игры
pygame.mixer.init()
screen= pygame.display.set_mode((width, height))
pygame.display.set_caption('Tokyo Аттак')
clock = pygame.time.Clock()
s= pygame.sprite.Group()
player=Player()
s.add(player)


#игра
g_run = True
while g_run:
    clock.tick(fps)
    s.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g_run=False
    screen.fill(purple_haze)
    s.draw(screen)
    pygame.display.flip()

pygame.quit()