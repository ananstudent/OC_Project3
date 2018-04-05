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
		#del structure[15] #je supprime le dernier indice : liste vide je ne sais pas pourquoi...
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






