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

#chargement son
son.play(loops=-1, maxtime=0, fade_ms=0)


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
				print("Ciao")
				continuer_principal = False
				continuer_accueil = False
				continuer_jeu = False
				
		
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_principal = False
				continuer_accueil = False
				continuer_jeu = False
				
			
			if event.type == KEYDOWN:
				
				if event.key == K_F1:
					continuer_accueil = False
					fichier = "N1.txt"
					print("N1")
				
				if event.key == K_F2:
					continuer_accueil = False
					fichier = "N2.txt"
					print("N2")

	if fichier != "": #On s'assure que le fichier est bien présent pour charger la carte
	#chargement du fond
		fenetre.blit(fond,(0,0))
		
		#génération d'un niveau à partir d'un fichier
		niveau = Niveau(fichier)
		niveau.generation()
		niveau.afficher(fenetre)

		
		#Creation d'un personnage
		dk = Monkey(niveau)


	#Boucle jeu	

	continuer_jeu = True
	while continuer_jeu:


		
		print("je suis là")

		pygame.time.Clock().tick(30)
		for event in pygame.event.get():

			if event.type == QUIT:
				continuer_principal = False
				continuer_jeu = False


			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					continuer_jeu = False
				#deplacement du singe	
				if event.key == K_RIGHT:
					print("droite")
					dk.deplacement("droite")
					
				if event.key == K_LEFT:
					print("gauche")
					dk.deplacement("gauche")
					
				if event.key == K_DOWN:
					print("bas")
					dk.deplacement("en bas")
					
				if event.key == K_UP:
					print("haut")
					dk.deplacement("en haut")
							




		
		fenetre.blit(fond,(0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction,(dk.x,dk.y))
		pygame.display.flip()
		print("je suis ici")
		print(dk.sprite_x,dk.sprite_y)
		print(dk.x,dk.y)

		if niveau.grille[dk.sprite_y][dk.sprite_x] == "a":
			print("Gagné!")
			continuer_jeu = False