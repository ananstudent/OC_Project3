########## Journal de développement du Projet 3: "Aider Mac Gyver à s'echapper"######

9 avril 2018 : 1er jour
Objectifs : préparation du projet 
			affichage d'un ecran d'accueil et du  labyrinthe
			affichage de Mac Gyver




1- Preparation du projet
	Modification du dossier P3 pour préparation du projet 
	Modification .gitignore de manière à ne plus versionné TP_Pygame contenu dans le dossier
	Creation d'un repertoire Pictures contenant les images du projet
	Creation du Readme.md dans l'optique de s'en servir comme un journal pour la redaction future du document lié  du projet
	Creation d'un rpertoire Map qui contiendra les cartes du labyrinthe
	Creation des fichiers  escape.py function.py classes.py constant.py

2- Je fais le choix de commencer à utiliser Py Game pour afficher une première fenêtre de jeu : Ecran d'accueil et coder le fait de rentrer dans le jeu et de pouvoir en sortir en fermant la fenêtre.
###Fait premier commit###

3- (Pygame est à mon sens plus facile à utliser que le mode console car il fonctionne par calque et cela évite de gérer les deplacements en manipulation de liste) 

Première étape: Gestion des boucles du jeu :Une boucle principale permettant de renter dans l'interface.
A l'intérieur:
Une boucle Accueil (Home loop) permettant de renter sur l'ecran d'accueil et d'en sortir pour enter dans le jeu (cela permettra par la suite de chatger plusieurs niveau)
Une Boucle jeu permettant de lancer la partie avec le choix de la carte.
###Fait deuxième commit###

Deuxième étape:

Génération de la structure du labyrinthe : je crée un document .txt avec 15 lignes de 15 cellules chacune: 
"w" = wall
"" = case vide
"a" = arrivée
Ce document sera la matrice du labyrinthe.
Je créé une class Map qui a comme attribut une grille vide au début et qui prend en parmètre le fichier .txt.
Cette classe a deux methodes

Une qui génére le labyrinthe à partir de la matrice :
A chaque symbole ("w" "a") correspond une image.
La liste de liste comporte des cases auquel je donne une taille de 30 * 30 pixel.

L'autre qui affiche le "calque" du labyrinthe. 

Dans le programme principal:
Je charge dans la fenêtre le fond.
Je créé un objet "labyrinth" de type Map et je lance les deux fonctions (generate et display ).
Je raffiche le fond + calque du labyrinthe.

####Fait 3 ème commit###

3 - Affichage et déplacements de MacGyver
On traite MacGyver comme un objet que l'on déplace :

Je crée une classe Heroe avec une position en x et y réelle et une position en x et y en pixel. Cette classe prend en paramètre le labyrinth puisque que le personnage se déplace dans la grille du labyrinthe.

Cette classe comprend une methode: Move qui définie les nouvelles positions suite aux différents demande de déplacement envoyer par des event.key du programme principal.

###Fait 4 ème commit###

10 avril 2018 : 2ème jour

Objectif: Coder le placement aléatoire des objets et leur affichage.

Après quelques tatonnements , j'ai décidé de faire une class Element,
La classe comporte deux methodes:
La première qui consiste à positionner l'objet: on commence par repérer les cases vides , on les listes puis on tire au sort les coordonnées en x et y.
La deuxième va venir consigner ces coordonnées dans la grille du labyrinthe sous forme de nom de l'objet. J'ai pensé que ceci serai pratique lors de l'étape du ramassage des objets . C'est à dire l'ajout d'une lettre dans la matrice du labyrinthe.
Je ne suis pas satisfaite totalment car si on rajoute des objets par la suite l'adaptation du programme peut-être fastidieuse.

####Fait 5 ème commit####



11 avril 2018 : 3ème jour

Objectif : 

Coder le ramassage des objets par MacGyver :

Lorsque Mac Gyver sera sur la case où se trouve l'objet il faudra que l'objet disparaisse de l'affichage, soit consigné dans une nouvelle liste par exemple "tool" donc apparaitre dans un deuxième temps dans cette fenêtre.
ce qui veut dire interaction entre les classes element et heroe ?

Changer la fin du jeu : on gagne si on a tous les éléments sinon on perd.

1- ajout d'une methode display_elements à la classe element

2- ajout d'une methode / propriété de classe ? à la classe element : 
affichant une seconde fenêtre de collecte avec comme matrice une liste vide....
Ah j'aurai aimé afficher une seconde fenêtre avec Pygame mais ceci n'est pas possible à priori ...

2bis- Changement de stratégie :

Je passe en console :
A chaque ajout d'un élément, une lettre s'inscrit dans labyrinth.grid  à la position de l'élément (methode pin_elements de la classe Element)
Donc lorsque la position de Macgyver correspond à cette lettre c'est qu'il "ramasse" l'objet.
Lorsqu'il "ramasse" l'objet je remplace la lettre symbolisant l'objet par "0".
L'affichage de l'objet est conditionnel à la présence de sa lettre témoin sur ses coordonnées. Donc l'objet ne s'affiche plus lorsque la lettre témoin n'est plus.

Je crée une liste tools vide . Elle symbolise le ramassage. Chaque élément ramassé vient s'ajouter à la liste.

Cette liste doit faire une longueur de 3 . Si ce n'est pas le cas et si MacGyver se positionne sur "a" c'est à dire l'arrivée sans ses trois objets , il perd. Sinon il gagne.

Les fonctionnalités du jeu sont remplies cependant je me demande toujours si je ne pourrais pas coder une fonction ou une methode evitant d'écrire les mêmes lignes pour chacun des trois objets.


####Fait 6 ème commit####

12 avril 2018 : 4 ème jour

Ajout de la methode display_element à la classe Element de manière à gérer l'affichage des objets si MG est sur la case ou non? Cette methode fait l'ajout aussi dans la liste TOOLS.
Ceci est l'idée que j'avais en tête pour gérer de la même manière tous les objets . Cpendant je me dis si le code est plus libilble ainsi ...

Je passe à l'aspect décoratif:
ajout de son et d'images supplémentaire (passer le texte en console à l'affichage)

