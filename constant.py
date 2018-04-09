#!/usr/bin/python3.5
# -*-coding:utf-8 -
"""Place where constants are"""

import pygame
from pygame.locals import *

pygame.init()

#Constant for loops
MAIN_LOOP = True

#Dimensions of game windows
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = (NB_SPRITE * SPRITE_SIZE, NB_SPRITE * SPRITE_SIZE)

#Display video of window game

WINDOW = pygame.display.set_mode(SCREEN_SIZE)
TITLE_WINDOW = "Help to Escape!"
ICONE = pygame.image.load("pictures/guardian.png").convert_alpha()

#Screen "home"
HOME = pygame.image.load("pictures/home.png").convert()