import pygame
import os
import math

# некоторые константы
WIDTH = 1280
HEIGHT = 720
FPS = 60
BLACK = (0, 0, 0)


class Planet(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)
        self.image = picture
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.rect.center = (640, 160)
        self.angle = 0
        self.radius_orbit = 20

    def update(self):
        # pygame.time.delay(100)
        self.angle += 0.1
        if self.angle >= 360:
            self.angle = 0
        x = self.radius_orbit * math.cos(self.angle)
        y = self.radius_orbit * math.sin(self.angle)
        self.rect.move_ip(x, y)


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
pc1 = pygame.image.load(os.path.join(sprite_folder, 'test.png')).convert()
pc2 = pygame.image.load(os.path.join(sprite_folder, 'test2.png')).convert()
bg = pygame.image.load(os.path.join(sprite_folder, 'bg.jpg')).convert()

# нужно чтобы время на 1 один прогон цикла было постоянным
clock = pygame.time.Clock()

# объединяем все картинки в единую группу
all_sprites = pygame.sprite.Group()

earth = Planet(pc1)
# merkury = Planet(pc2)
all_sprites.add(earth)
# all_sprites.add(merkury)

# Цикл игры
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
    screen.blit(bg, (0, 0))
    # Рендеринг
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
