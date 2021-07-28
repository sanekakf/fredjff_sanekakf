#https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie

import pygame
import random 

WIDTH = 480 #ширина игрового окна 
HEIGHT = 480 #высота игрового окна
FPS = 60 #частота кадров в секунду 


# Цвета (R , G , B)   
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (160, 0, 200)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)




#создаем игру и окно 
pygame.init()
pygame.mixer.init() #для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

#цикл игры
running = True 
while running:
    # держим цикл на правильной скорости 
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

# обновление 
all_sprites.update()





screen.fill(BLACK)
all_sprites.draw(screen)
# после отрисовки всего, переворачиваем экран 
pygame.display.flip()


pygame.quit()


   
    
    