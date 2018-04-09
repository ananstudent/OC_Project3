#!/usr/bin/python3.5
# -*-coding:utf-8 -


import pygame
from pygame.locals import *

pygame.init()

#Constante pour boucle jeu et menu
continuer_principal = True
continuer_accueil = True
continuer_jeu = True

#Variable de choix du niveau
fichier = ""

#Structure de la fenêtre du jeu
nb_case = 15
sprit_size = 30
screen_size = (nb_case*sprit_size, nb_case*sprit_size)

fenetre = pygame.display.set_mode(screen_size)

titre_fenetre = "Jeu Pygame/DK"
icone = pygame.image.load("arrivee.png")

accueil = pygame.image.load("accueil.png").convert()
fond = pygame.image.load("fond.jpg").convert()


#Images DK

dk_gauche = pygame.image.load("dk_gauche.png").convert_alpha()
dk_droite = pygame.image.load("dk_droite.png").convert_alpha()
dk_bas = pygame.image.load("dk_bas.png").convert_alpha()
dk_haut = pygame.image.load("dk_haut.png").convert_alpha()

#Sprites

mur = pygame.image.load("mur.png")
arrivee = pygame.image.load("arrivee.png").convert_alpha()
depart = pygame.image.load("depart.png").convert()

#son

son = pygame.mixer.Sound("10620.wav")


