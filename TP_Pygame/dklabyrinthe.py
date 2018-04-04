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

while continuer_principal:
	#chargement ecran d'accueil
	fenetre.blit(accueil,(0,0))

	#Raffraichissement
	pygame.display.flip()


	while continuer_accueil:
	#limitation de vitesse de la boucle :
		pygame.time.Clock().tick(30)


		for event in pygame.event.get():
		#Boucle Menu
		#Quitter
			if event.type == QUIT:
				continuer_principal = False
				continuer_accueil = False
				continuer_jeu = False
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_principal = False
				continuer_accueil = False
				continuer_jeu = False
				

		#Retour Menu 	
		
	
			if event.type == KEYDOWN:
				if event.key == K_F1:
					continuer_accueil = False
					fichier = "N1.txt"
				if event.key == K_F2:
					continuer_accueil = False
					fichier = "N2.txt"
		
	if fichier != 0: #On s'arrure que le fichier est bien présent pour charger la carte
		#chargement du fond
		fenetre.blit(fond,(0,0))


		niveau = Niveau(fichier)
		niveau.generation()
		niveau.afficher(fenetre)

		

		

		#Si le choix est N1 , je génére le Niveau 1 et je l'affiche





