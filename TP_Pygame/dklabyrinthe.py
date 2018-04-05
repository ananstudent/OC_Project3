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


pygame.init()

#Ouverture de la fenetre de jeu

pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)

continuer_principal = True

while continuer_principal:
	#chargement ecran d'accueil
	fenetre.blit(accueil,(0,0))

	#Raffraichissement
	pygame.display.flip()
	
	
	continuer_accueil = True

	while continuer_accueil:

		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
		#Boucle Menu
		#Quitter
			if event.type == QUIT:
				continuer_principal = False
				continuer_accueil = False
				
		
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_principal = False
				continuer_accueil = False
				
			
			if event.type == KEYDOWN:
				
				if event.key == K_F1:
					continuer_accueil = False
					
					fichier = "N1.txt"
					print("N1")
				if event.key == K_F2:
					continuer_accueil = False
					fichier = "N2.txt"
					print("N2")

	if fichier != "": #On s'arrure que le fichier est bien présent pour charger la carte
	#chargement du fond
		fenetre.blit(fond,(0,0))
		niveau = Niveau(fichier)
		niveau.generation()
		niveau.afficher(fenetre)
		pygame.display.flip()

	continuer_jeu = True
	while continuer_jeu:


		print("je suis là")
		pygame.display.flip()

		pygame.time.Clock().tick(30)
		for event in pygame.event.get():

			if event.type == QUIT:
				continuer_principal = False
				continuer_jeu = False
		
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_jeu = False
				continuer_principal = True
				continuer_accueil = True
	



