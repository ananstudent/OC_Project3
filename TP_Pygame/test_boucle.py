#!/usr/bin/python3.5
# -*-coding:utf-8 -

grille = []

with open("N1.txt","r") as fichier:
	for line in fichier:
		line = line.strip()
		grille.append(list(line))

print(grille)


num_ligne=0
for line in grille:
	num_case=0
	for sprit in line:
		x = num_case
		y = num_ligne
		if sprit == "m":
			print(x,y)
		num_case += 1

	num_ligne +=1








