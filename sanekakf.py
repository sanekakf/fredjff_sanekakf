import pygame
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
        self.image = pygame.Surface((50,50))
        self.image.fill(gold)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > width:
            self.rect.right = 0
#запуск игры
pygame.init()
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