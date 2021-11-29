import pygame
import os
import math

# некоторые константы
WIDTH = 1200
HEIGHT = 900
BLACK = (0, 0, 0)


class Planet(pygame.sprite.Sprite):
    """Базовый класс всех планет"""
    def __init__(self, picture, velocity, start_angle, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.speed = velocity
        self.image = picture
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.angle = start_angle
        self.a = a
        self.b = b

    def update(self):
        # TODO: никак не пойму как это работает
        self.angle += self.speed
        if self.angle >= 360:
            self.angle = 0
        self.rect.centerx = self.a * math.cos(self.angle) + WIDTH / 2
        self.rect.centery = self.b * math.sin(self.angle) + HEIGHT / 2


# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("СПАЙС")

game_folder = os.path.dirname(__file__)
sprite_folder = os.path.join(game_folder, 'resources')
im1 = pygame.image.load(os.path.join(sprite_folder, '1.png')).convert()
im2 = pygame.image.load(os.path.join(sprite_folder, '2.png')).convert()
im3 = pygame.image.load(os.path.join(sprite_folder, '3.png')).convert()
im4 = pygame.image.load(os.path.join(sprite_folder, '4.png')).convert()
im5 = pygame.image.load(os.path.join(sprite_folder, '5.png')).convert()
im6 = pygame.image.load(os.path.join(sprite_folder, '6.png')).convert()
im7 = pygame.image.load(os.path.join(sprite_folder, '7.png')).convert()
im8 = pygame.image.load(os.path.join(sprite_folder, '8.png')).convert()
bg = pygame.image.load(os.path.join(sprite_folder, 'bg.jpg')).convert()

# нужно чтобы время на 1 один прогон цикла было постоянным
clock = pygame.time.Clock()

# объединяем все картинки в единую группу
all_sprites = pygame.sprite.Group()

# создание солнца в центре
sun = pygame.image.load(os.path.join(sprite_folder, '0.png')).convert()
sun.set_colorkey(BLACK)
sun_rect = sun.get_rect()
sun_rect.center = (WIDTH/2, HEIGHT/2)

# TODO: это все должно быть в циклах и списках
merkury = Planet(im1, 0.025, 270, 120, 60)
venus = Planet(im2, 0.025, 30, 120, 100)
earth = Planet(im3, 0.0025, 0, 160, 110)
mars = Planet(im4, 0.0255, 180, 200, 200)
jupiter = Planet(im5, 0.0025, 5, 240, 110)
saturn = Planet(im6, 0.0025, 320, 280, 110)
uranus = Planet(im7, 0.0025, 124, 320, 110)
neptune = Planet(im8, 0.0025, 90, 360, 110)
all_sprites.add(merkury)
all_sprites.add(venus)
all_sprites.add(earth)
all_sprites.add(mars)
all_sprites.add(jupiter)
all_sprites.add(saturn)
all_sprites.add(uranus)
all_sprites.add(neptune)

# Цикл игры
main_loop = True
while main_loop:
    clock.tick(60) # фпсссс!!0)1))!0!)))!
    for event in pygame.event.get():
        # закрыть окно по нажатию на крестик
        if event.type == pygame.QUIT:
            main_loop = False

    # Рендеринг нового кадра
    all_sprites.update()
    screen.blit(bg, (0, 0))
    screen.blit(sun, sun_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
