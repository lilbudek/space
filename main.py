import pygame
import os
import math

# некоторые константы
WIDTH = 1280
HEIGHT = 720
G = 6.67e-11
M = 5.97e24
R = 6371
BLACK = (0, 0, 0)


class Planet(pygame.sprite.Sprite):
    """тест"""
    def __init__(self, picture, velosity, start_angle, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.speed = velosity
        self.image = picture
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        # self.rect.center = (0, 0)
        self.angle = start_angle
        self.a = a
        self.b = b

    def update(self):
        self.angle += self.speed
        if self.angle >= 360:
            self.angle = 0
        self.rect.x = self.a * math.cos(self.angle) + WIDTH / 2
        self.rect.y = self.b * math.sin(self.angle) + HEIGHT / 2


# Создаем игру и окно
pygame.init()

# нужно чтобы был звук, не знаю пока понадобится ли
pygame.mixer.init()

# самая нужная вещь - вертикальная синхронизация
flags = pygame.SCALED
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, vsync=1)
pygame.display.set_caption("My Game")

game_folder = os.path.dirname(__file__)
sprite_folder = os.path.join(game_folder, 'resources')
sun = pygame.image.load(os.path.join(sprite_folder, '0.png')).convert()
im1 = pygame.image.load(os.path.join(sprite_folder, '1.png')).convert()
im2 = pygame.image.load(os.path.join(sprite_folder, '2.png')).convert()
im3 = pygame.image.load(os.path.join(sprite_folder, '3.png')).convert()
im4 = pygame.image.load(os.path.join(sprite_folder, '4.png')).convert()
bg = pygame.image.load(os.path.join(sprite_folder, 'bg.jpg')).convert()

# нужно чтобы время на 1 один прогон цикла было постоянным
clock = pygame.time.Clock()

# объединяем все картинки в единую группу
all_sprites = pygame.sprite.Group()
sun.set_colorkey(BLACK)
merkury = Planet(im1, 0.025, 90, 500, 300)
# venus = Planet(im2, 640, 480, 0)
earth = Planet(im3, 0.0025, 0, 600, 350)
# mars = Planet(im4, 420, 160, 0)
all_sprites.add(merkury)
# all_sprites.add(venus)
all_sprites.add(earth)
# all_sprites.add(mars)

# Цикл игры

main_loop = True
while main_loop:
    clock.tick(60)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            main_loop = False
    # Обновление
    all_sprites.update()
    # Рендеринг

    screen.blit(bg, (0, 0))
    screen.blit(sun, (WIDTH / 2 - 110, HEIGHT / 2 - 110))
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()
