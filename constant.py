#!/usr/bin/python3.5
# -*-coding:utf-8 -
"""Place where constants are"""

import pygame
from pygame.locals import *

pygame.init()

#Constant for loops
MAIN_LOOP = True
HOME_LOOP = True
GAME_LOOP = True

#Dimensions of game windows
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = (NB_SPRITE * SPRITE_SIZE, NB_SPRITE * SPRITE_SIZE)

#Display video of window game
window = pygame.display.set_mode(SCREEN_SIZE)
TITLE_WINDOW = "Help to Escape!"
ICONE = pygame.image.load("pictures/guardian.png").convert_alpha()

#Screen "home"
HOME = pygame.image.load("pictures/home.png").convert()

#Game background
BACKGROUND = pygame.image.load("pictures/background.jpg").convert()

#kind of sprite
WALL = pygame.image.load("pictures/wall.png")
ARRIVAL = pygame.image.load("pictures/guardian.png").convert_alpha()

#Display MacGyver
MG = pygame.image.load("pictures/MacGyver.png").convert_alpha()

#variable contain map
file = ""