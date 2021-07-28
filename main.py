#https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie

import pygame
import random 

WIDTH = 560 #ширина игрового окна 
HEIGHT = 480 #высота игрового окна
FPS = 60 #частота кадров в секунду 


# Цвета (R , G , B)   
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (160, 0, 200)

#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ#Я ХАВАТЬ
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0



#создаем игру и окно 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()


   
    
    