#https://pythonru.com/uroki/biblioteka-pygame-chast-1-vvedenie

import pygame
import random 

WIDTH = 360 #ширина игрового окна 
HEIGHT = 480 #высота игрового окна
FPS = 60 #частота кадров в секунду 


# Цвета (R , G , B)   
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255 )




#создаем игру и окно 
pygame.init()
pygame.mixer.init() #для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

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
   
screen.fill(BLACK)
# после отрисовки всего, переворачиваем экран 
pygame.display.flip()


pygame.quit()


   
    
    