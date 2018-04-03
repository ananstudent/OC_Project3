#!/usr/bin/python3.5
# -*-coding:utf-8 -

"""

Jeu Donkey Kong Labyrinthe

Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.


Script Python

Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images

"""

#import pygame
#from pygame.locals import *

from constantes import*
from classes import*

#pygame.init()


pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)
fenetre.blit(accueil,(0,0))
#fenetre.blit(mur,(0,sprit_size)) essai de remplissage
pygame.display.flip()



while continuer:
	pygame.time.Clock().tick(30)
	for event in pygame.event.get():
		#Boucle Menu
		if event.type == KEYDOWN and event.key == K_ESCAPE:
				fenetre.blit(accueil,(0,0))
				pygame.display.flip()
				print("Menu")

		#Boucle Jeu
		if event.type == KEYDOWN:
			if event.key == K_F1:
				#generer le niveau à partier du fichier
				fenetre.blit(fond,(0,0)) #A venir methode de class Niveau1
				pygame.display.flip()
				print("Niveau1")
			if event.key == K_F2:
				fenetre.blit(fond,(0,0)) #A venir methode de class Niveau2
				pygame.display.flip()
				print("Niveau2")
		#Quitter
		if event.type == QUIT:
			continuer = False		



