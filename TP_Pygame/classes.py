#!/usr/bin/python3.5
# -*-coding:utf-8 -

from constantes import*


class Niveau():
	"""avec deux méthodes, une qui génère un niveau à partir d'un fichier
	dans un attribut grille, l'autre qui l'affiche à l'écran."""
	

	def __init__(self, fichier):
		self.fichier = fichier
		self.grille =[]

	def generation(self):
		structure = []

		with open(self.fichier, "r") as fichier:
			for line in fichier:
				line = line.strip()#je coupe le saut de ligne
				structure.append(list(line))

		self.grille = structure	#je mets la structure dans un attribut grille

	def afficher(self,fenetre):

		num_ligne = 0
		for line in self.grille:
			num_case = 0
			for sprit in line:
				x = num_case * sprit_size
				y = num_ligne * sprit_size
				if sprit == "d":
					fenetre.blit(depart,(x,y))
				if sprit == "m":
					fenetre.blit(mur,(x,y))
				if sprit == "a":
					fenetre.blit(arrivee,(x,y))
				num_case += 1
				
			num_ligne += 1		

class Monkey():

	def __init__(self, niveau):
		#Images de mouvement de DK:
		self.droite = dk_droite
		self.gauche = dk_gauche
		self.bas = dk_bas
		self.haut = dk_haut

		#Position en pixel:
		self.x = 0
		self.y = 0

		#Position en case:
		self.sprite_x = 0
		self.sprite_y = 0

		#Direction par défaut
		self.direction = dk_bas

		#Niveau
		self.niveau = niveau

	def deplacement(self, direction):
		"""Methode permettant de deplacer le personnage"""

		#deplacement à droite
		if direction == "droite":
			if self.sprite_x < nb_case -1: #empecher de sortir de l'écran
				if self.niveau.grille[self.sprite_y][self.sprite_x+1] != "m": #si la case 
					#deplacement d'une case
					self.sprite_x += 1
					#Position réelle après deplacement
					self.x = self.sprite_x * sprit_size

			self.direction = self.droite #On affiche le singe dans la position
		
		#deplacement gauche
		if direction == "gauche":
			if self.sprite_x > 0: #empecher de sortir de l'écran
				if self.niveau.grille[self.sprite_y][self.sprite_x-1] != "m":
					self.sprite_x -= 1
					self.x = self.sprite_x * sprit_size
			self.direction = self.gauche
			
		#deplacement bas
		if direction == "en bas":
			if self.sprite_y < nb_case-1: #empecher de sortir de l'écran
				if self.niveau.grille[self.sprite_y+1][self.sprite_x] != "m":
					self.sprite_y += 1
					self.y = self.sprite_y * sprit_size
			self.direction = self.bas

		#deplacement haut
		if direction == "en haut":
			if self.sprite_y > 0: #empecher de sortir de l'écran
				if self.niveau.grille[self.sprite_y-1][self.sprite_x] != "m":
					self.sprite_y -= 1
					self.y = self.sprite_y * sprit_size

			self.direction = self.haut



					



			
							



