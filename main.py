import pygame
import os
import math

# некоторые константы
WIDTH = 1200
HEIGHT = 900
BLACK = (0, 0, 0)
game_folder = os.path.dirname(__file__)
sprite_folder = os.path.join(game_folder, 'resources')


class Planet(pygame.sprite.Sprite):
    """Базовый класс всех планет"""

    def __init__(self, number, velocity, start_pos, a, b):
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.speed = velocity
        self.image = pygame.image.load(os.path.join(sprite_folder, str(number) + '.png')).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.angle = start_pos
        self.a = a
        self.b = b

    def update(self):
        if self.number == 2:
            self.angle += self.speed
        else:
            self.angle -= self.speed
        if self.angle >= 360:
            self.angle = 0
        self.rect.centerx = self.a * math.cos(self.angle) + WIDTH / 2
        self.rect.centery = self.b * math.sin(self.angle) + HEIGHT / 2


# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("СПАЙС")

bg = pygame.image.load(os.path.join(sprite_folder, 'bg.jpg')).convert()

# нужно чтобы время на 1 один прогон цикла было постоянным
clock = pygame.time.Clock()

# объединяем все картинки в единую группу
all_sprites = pygame.sprite.Group()

# создание солнца в центре
sun = pygame.image.load(os.path.join(sprite_folder, '0.png')).convert()
sun.set_colorkey(BLACK)
sun_rect = sun.get_rect()
sun_rect.center = (WIDTH / 2, HEIGHT / 2)

planet = [
    Planet(1, 0.0025, 270, 120, 60),
    Planet(2, 0.0025, 30, 120, 100),
    Planet(3, 0.0025, 0, 160, 110),
    Planet(4, 0.0255, 180, 200, 200),
    Planet(5, 0.0025, 5, 240, 110),
    Planet(6, 0.0025, 320, 280, 110),
    Planet(7, 0.0025, 124, 320, 110),
    Planet(8, 0.0025, 90, 360, 110)
]

for i in planet:
    all_sprites.add(i)

# Цикл игры
main_loop = True
while main_loop:
    clock.tick(60)  # фпсссс!!0)1))!0!)))!
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
