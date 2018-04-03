#!/usr/bin/python3.5
# -*-coding:utf-8 -

#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)


#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond,(0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)
#position_perso_x = 0
#position_perso_y = 0




#Raffraichissement de l'écran
pygame.display.flip()

#Boucle infinie
pygame.key.set_repeat(400, 30)
continuer = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				position_perso = position_perso.move(0,3)
			if event.key == K_UP:
				position_perso = position_perso.move(0,-3)
			if event.key == K_LEFT:
				position_perso = position_perso.move(-3,0)
			if event.key == K_RIGHT:
				position_perso = position_perso.move(3,0)		
		if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
			print("Zone dangereuse")
		if event.type == MOUSEMOTION and event.buttons[0] == 1:
			continuer = 0
		if event.type == MOUSEMOTION and event.buttons[1] == 1:



	#Re-collage
	fenetre.blit(fond,(0,0))
	fenetre.blit(perso, position_perso)
	#Raffraichissement
	pygame.display.flip()	