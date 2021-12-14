import math
import os
from tkinter import *
from PIL import ImageTk, Image
import pygame
import info

# some constant
WIDTH = 1280
HEIGHT = 960
BLACK = (0, 0, 0)
game_folder = os.path.dirname(__file__)
sprite_folder = os.path.join(game_folder, "resources")


def info_win(number):
    """
    This module is responsible for information about the planets
    """
    tkwin = Tk()
    tkwin.geometry("810x600+300+300")
    tkwin.resizable(False, False)
    tkwin.title("About Planet")
    img = Image.open(os.path.join(sprite_folder, str(number) + "_.jpg"))
    resize_img = img.resize((450, 450))
    small_img = ImageTk.PhotoImage(resize_img)
    picture = Label(image=small_img)
    text = Label(tkwin, text=info.planet_info[number], fg="black", font="none 14 ", anchor=CENTER)
    text.pack()
    picture.pack()
    tkwin.mainloop()


class Planet(pygame.sprite.Sprite):
    """
    Base class of all planets
    args:
        number - planet number
        speed - planet speed
        image - planet image
        rect - the described square
        angle - starting angle of the planet
    """
    def __init__(self, number, velocity, start_pos, a, b):
        """
        planet construction
        """
        pygame.sprite.Sprite.__init__(self)
        self.number = number
        self.speed = velocity
        self.image = pygame.image.load(
            os.path.join(sprite_folder, str(number) + ".png")).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.angle = start_pos
        self.a = a
        self.b = b

    def update(self):
        """
        planet moving
        """
        if self.number == 2:
            self.angle += self.speed
        else:
            self.angle -= self.speed
        if self.angle >= 360:
            self.angle = 0
        self.rect.centerx = self.a * math.cos(self.angle) + WIDTH / 2
        self.rect.centery = self.b * math.sin(self.angle) + HEIGHT / 2


# Create win init application
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space")

bg = pygame.image.load(os.path.join(sprite_folder, "bg.jpg")).convert()

# hold one cycle time
clock = pygame.time.Clock()

# combine all the pictures into a single group
all_sprites = pygame.sprite.Group()

# make the sun
sun = pygame.image.load(os.path.join(sprite_folder, "0.png")).convert()
sun.set_colorkey(BLACK)
sun_rect = sun.get_rect()
sun_rect.center = (WIDTH / 2, HEIGHT / 2)

planet = [
    Planet(1, 0.00684, 235, 110, 65),
    Planet(2, 0.00348, 346, 150, 95),
    Planet(3, 0.00122, 56, 200, 130),
    Planet(4, 0.00049, 98, 240, 170),
    Planet(5, 0.0000758, 234, 310, 240),
    Planet(6, 0.0000415, 43, 430, 320),
    Planet(7, 0.0000256, 12, 520, 390),
    Planet(8, 0.0000100, 0, 600, 500),
]

# add all generated planet to sprite list
for i in planet:
    all_sprites.add(i)

# Main game cycle
main_loop = True
while main_loop:
    clock.tick(60)   # Fps!!0)1))!0!)))!
    # check all invents
    for event in pygame.event.get():
        # close the window by clicking on the cross
        if event.type == pygame.QUIT:
            main_loop = False
        # open information window when clicked on planet
        if event.type == pygame.MOUSEBUTTONDOWN:
            for obj in planet:
                if obj.rect.collidepoint(pygame.mouse.get_pos()):
                    info_win(obj.number)
    # rendering new frame
    all_sprites.update()
    screen.blit(bg, (0, 0))
    screen.blit(sun, sun_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
