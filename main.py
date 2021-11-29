import pygame
import os
import math

# некоторые константы
WIDTH = 1152
HEIGHT = 864
G = 6.67e-11
M = 5.97e24
R = 6371
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Planet(pygame.sprite.Sprite):
    """тест"""

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
        self.rect.x = self.a * math.cos(self.angle) + WIDTH // 2 - 10
        self.rect.y = self.a * math.sin(self.angle) + HEIGHT // 2 - 10


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
im5 = pygame.image.load(os.path.join(sprite_folder, '5.png')).convert()
im6 = pygame.image.load(os.path.join(sprite_folder, '6.png')).convert()
im7 = pygame.image.load(os.path.join(sprite_folder, '7.png')).convert()
im8 = pygame.image.load(os.path.join(sprite_folder, '8.png')).convert()
bg = pygame.image.load(os.path.join(sprite_folder, 'bg.jpg')).convert()

# нужно чтобы время на 1 один прогон цикла было постоянным
clock = pygame.time.Clock()

# объединяем все картинки в единую группу
all_sprites = pygame.sprite.Group()
sun.set_colorkey(BLACK)
merkury = Planet(im1, 0.025, 270, 80, 90)
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
    clock.tick(60)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            main_loop = False
    # Обновление
    all_sprites.update()
    # Рендеринг

    # screen.blit(bg, (0, 0))
    screen.fill(BLACK)
    screen.blit(sun, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

    # debug
    # pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 50)
    # x, y = pygame.mouse.get_pos()
    # print(x, y)

    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()
