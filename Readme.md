########## Journal de développement du Projet 3: "Aider Mac Gyver à s'echapper"######

9 avril 2018 : 1er jour
Objectifs : préparation du projet 
			affichage d'un ecran d'accueil et du  labyrinthe
			affichage de Mac Guyver




1- Preparation du projet
	Modification du dossier P3 pour préparation du projet 
	Modification .gitignore de manière à ne plus versionné TP_Pygame contenu dans le dossier
	Creation d'un repertoire Pictures contenant les images du projet
	Creation du Readme.md dans l'optique de s'en servir comme un journal pour la redaction future du document lié  du projet
	Creation d'un rpertoire Map qui contiendra les cartes du labyrinthe
	Creation des fichiers  escape.py function.py classes.py constant.py

2- Je fais le choix de commencer à utiliser Py Game pour afficher une première fenêtre de jeu : Ecran d'accueil et coder le fait de rentrer dans le jeu et de pouvoir en sortir en fermant la fenêtre --- Fait premier commit.

3- (Pygame est à mon sens plus facile à utliser que le mode console car il fonctionne par calque et cela évite de gérer les deplacements en manipulation de liste) 

Première étape: Gestion des boucles du jeu :Une boucle principale permettant de renter dans l'interface.
A l'intérieur:
Une boucle Accueil (Home loop) permettant de renter sur l'ecran d'accueil et d'en sortir pour enter dans le jeu (cela permettra par la suite de chatger plusieurs niveau)
Une Boucle jeu permettant de lancer la partie avec le choix de la carte.
Fait deuxième commit.

Deuxième étape:

Génération de la structure du labyrinthe : je crée un document .txt avec 15 lignes de 15 cellules chacune: 
"w" = wall
"" = case vide
"a" = arrivée
ce fichier sera la carte permattant de générer le labyrinthe . Le traitement sera celui d'une liste de liste .




