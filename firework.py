import pygame
import warnings
import math
import random
from pygame import mixer

pygame.init()
warnings.filterwarnings("ignore", category=DeprecationWarning)

# set display size
screen = pygame.display.set_mode((800, 700))

# constants
wh = (255, 255, 255)
a = 150
length = 90
run = True
blast_sound = mixer.Sound("fire_blast.wav")
whistle_sound = mixer.Sound("fire_whistle.wav")

# color list
colors = [(244, 119, 34), (18, 126, 189), (24, 158, 73), (233, 36, 38), (251, 229, 11)]
types = ["f1", "f2", "f3"]

# create a background
background = pygame.image.load("sky.jpg")


# class for firework
class fireWork:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.blast = False
        self.fire = False
        self.name = name

    # drawing the fire work
    def draw_fire(self):
        pygame.draw.polygon(screen, (255, 0, 0), [(self.x, self.y - 10), (self.x - 2, self.y), (self.x + 2, self.y)])
        pygame.draw.polygon(screen, (255, 180, 0), [(self.x + 2, self.y), (self.x - 2, self.y), (self.x, self.y + 20)])

    # launching the firework
    def go_up(self):
        if self.y >= 150:
            self.y -= 5
        else:
            self.y = 670
            self.fire = False
            f1.blast = False
            f2.blast = False
            f3.blast = False
            f4.blast = False
            self.blast = True
        if self.y <= 400:
            f1.blast = False
            f2.blast = False
            f3.blast = False
            f4.blast = False

    # drawing the blast
    def draw_line(self, c, an, f_type):
        n = random.randint(10, 90)
        x = int(self.x + math.cos(math.radians(an)) * n)
        y = int(150 + math.sin(math.radians(an)) * n)
        if f_type == "f1":
            pygame.draw.line(screen, c, (gt_cos(self.x, 0), gt_sin(a, 0)), (gt_cos(self.x, 180), gt_sin(a, 180)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 15), gt_sin(a, 15)), (gt_cos(self.x, 195), gt_sin(a, 195)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 30), gt_sin(a, 30)), (gt_cos(self.x, 210), gt_sin(a, 210)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 45), gt_sin(a, 45)), (gt_cos(self.x, 225), gt_sin(a, 225)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 60), gt_sin(a, 60)), (gt_cos(self.x, 240), gt_sin(a, 240)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 75), gt_sin(a, 75)), (gt_cos(self.x, 255), gt_sin(a, 250)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 90), gt_sin(a, 90)), (gt_cos(self.x, 270), gt_sin(a, 270)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 105), gt_sin(a, 105)), (gt_cos(self.x, 285), gt_sin(a, 285)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 120), gt_sin(a, 120)), (gt_cos(self.x, 300), gt_sin(a, 300)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 135), gt_sin(a, 135)), (gt_cos(self.x, 315), gt_sin(a, 315)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 150), gt_sin(a, 150)), (gt_cos(self.x, 330), gt_sin(a, 330)), 2)
            pygame.draw.line(screen, c, (gt_cos(self.x, 165), gt_sin(a, 165)), (gt_cos(self.x, 345), gt_sin(a, 345)), 2)
        elif f_type == "f2":
            pygame.draw.line(screen, c, (self.x, 150), (x, y), 2)
        elif f_type == "f3":
            pygame.draw.line(screen, c, (self.x, 150), (x, y), 2)
            pygame.draw.circle(screen, c, (x, y), 5, 0)


# cosine function
def gt_cos(x, angle):
    return x + math.cos(math.radians(angle)) * length


# sin function
def gt_sin(y, angle):
    return y + math.sin(math.radians(angle)) * length


def cl_line(f):
    blast_sound.play()
    t = random.choice(types)
    for i in range(0, 360, 15):
        f.draw_line(random.choice(colors), i, t)


# initialising the objects
f1 = fireWork(150, 670, "f1")
f2 = fireWork(310, 670, "f2")
f3 = fireWork(480, 670, "f3")
f4 = fireWork(650, 670, "f4")
# make first firework fire True
f1.fire = True

while run:
    # fill the screen with black color
    screen.fill((0, 0, 0))

    # blit the background
    screen.blit(background, (0, 0))

    # make firework move
    if f1.fire:
        whistle_sound.play()
        f1.draw_fire()
        f1.go_up()
    elif f2.fire:
        whistle_sound.play()
        f2.draw_fire()
        f2.go_up()
    elif f3.fire:
        whistle_sound.play()
        f3.draw_fire()
        f3.go_up()
    elif f4.fire:
        whistle_sound.play()
        f4.draw_fire()
        f4.go_up()

    # make the fire work blast
    if f1.blast:
        cl_line(f1)
        f3.fire = True
    elif f2.blast:
        cl_line(f2)
        f4.fire = True
    elif f3.blast:
        cl_line(f3)
        f2.fire = True
    elif f4.blast:
        cl_line(f4)
        f1.fire = True

    # check for the event happen in pygame
    for event in pygame.event.get():
        # check if exit key is pressed
        if event.type == pygame.QUIT:
            run = False

    # update the display
    pygame.display.update()
