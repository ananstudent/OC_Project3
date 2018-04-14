Elaboration  du programme “Aider MacGyver à s’échapper”  
dépôt Github: https://github.com/horlas/OC_Project3.git

Programme écrit en Python3 grâce au module Pygame. Utilisation de Virtual Env et Git.

1- Préparation du projet :
Initialisation d’un environnement virtuel de développement : virtual env/
Initialisation d’un repo Github et initialisation d’un dépôt git en local 
Création d’un fichier requirements.txt qui contiendra les versions des bibliothèques utilisées par le programme, dans notre cas Pygame.
Creation de trois fichier .py : escape.py, classes.py, constant.py qui contiendront le programme, les classes, les constantes du programme.
Création de deux dossiers : Map qui contient les cartes du labyrinthe, Pictures les images utilisées.

2- Gestion des boucles du jeu avec l’affichage des fenêtres du jeu :
Boucle Main: Initialisation de la fenêtre Pygame.
Boucle Home: Fenêtre d’accueil du  jeu si on tape “ENTER” on rentre dans le jeu,  le fond d'écran utilisé est “HOME”
Boucle Game : Fenêtre affichant le labyrinthe, le fond d'écran utilisé est “BACKGROUND”
On peut basculer de la fenêtre affichant le labyrinthe vers la fenêtre d’accueil en appuyant sur ECHAP et une fois sur la fenêtre d’accueil : on peut entrer à nouveau dans le jeu en appuyant sur ENTER. Ceci a pour conséquence de relancer la partie depuis le départ.
On peut, à n’importe quel moment, fermer la fenêtre Pygame et quitter le programme, ceci interrompt toutes les boucles.

3- Génération de la structure du labyrinthe:

Le labyrinthe est généré à partir d’une carte sous format .txt , il contient 15 lignes de 15 caractères: "w" = wall, "" = case vide, "a" = arrivée.
Création de la classe Map qui a comme attribut une grille vide au début et qui prend en paramètre le fichier .txt.
La méthode “generate” génère une liste de listes à partir de la lecture du fichier .txt . Cette liste de listes est mise dans l’attribut “grid” qui sera la matrice du Labyrinthe.
Grâce à l’itération de “grid” , la méthode “display” affiche les sprites “mur” et “arrivée” selon si la cellule contient “w” ou “a” . Elle n’affiche rien pour les cases vides. L’affichage se fera grâce à un système de coordonnées x et y qui sera en pixel (SPRITE_SIZE) une case a une côte de 30*30.
La méthode “display” affiche le labyrinthe comme un calque apposé à “BACKGROUND”.
On affiche la photo du gardien sur la case “a”.
Au niveau du programme, le labyrinthe est affiché lors de l’entrée dans la boucle jeu 
4-Affichage et gestion des déplacements de Macgyver:

MacGyver est un objet de class Heroe . Il a comme attributs ses coordonnées en réel et en pixel pour permettre son affichage et prend en paramètre le labyrinthe pour récupérer la grille  .
Du programme: le joueur envoi des ordres de déplacement. Ces ordres sont rentrés en paramètre à la méthode “move” de la classe Heroe: pour chacune des directions on modifie les coordonnées de MacGyver. Dans le programme on affiche MacGyver avec ses nouvelles coordonnées.
Lorsque MacGyver arrive sur la case “a” on a gagné et on sort du jeu pour aller à l’accueil.



5- Positionnement aléatoire des objets dans les couloirs du Labyrinthe:

Création d’une classe Element avec comme attribut un nom, une surface (pour gérer l’affichage), des coordonnées reelles et pixel. 
La méthode “locate_elements” liste les coordonnées (cell, ligne) de toutes les cases vides du labyrinthe. Elle met cette liste de tuple dans “position”. Puis on tire au sort grâce à un random.choice , un couple de coordonnée XY qui seront les coordonnées de l’élément créé.
La méthode “pin_elements” vient écrire le nom de l’objet à son emplacement dans la matrice “grid” du labyrinthe.

6- Ramassage des éléments par MacGyver:

Lorsque MacGyver collecte un objet:
Il écrit à la place de la position de l’objet un  “0” à l’endroit où il y avait le nom de l’objet (pin_element).
On ajoute aussi le nom de l’objet à une liste vide TOOLS qui sert de compteur.
7- L’affichage des objets se fait donc de manière conditionnelle : “display_elements” , si il y a leur nom à leur emplacement on les affiche sinon non.

Pour faire les étapes 6 et 7 on passe en paramètre la méthode “display_element” MacGyver , pour avoir les coordonnées de ce dernier ainsi que la liste TOOLS (vidée à chaque entrée dans le jeu) pour inscrire le nom des éléments collectés par MacGyver.

J’ai des doutes quand à la logique et au choix algorithmique du code de cette partie … J’ai codé comme cela car au début j’ai voulu créé une fonction appliquant les mêmes actions pour tous les éléments . Mais je ne sais pas si en terme de performance , faire passer les coordonnées de MacGyver à chaque déplacement dans les trois éléments est une bonne chose. Mais le programme fonctionne.

8- Gagné ou Perdu ?:
Si MacGyver se présente sur “a” avec une liste d’objet TOOLS inférieur à 3 il a perdu sinon il a gagné.

9- Amélioration de l’affichage du  programme en enlevant les affichages en mode console. Ajout de la musique.

10- Ajout du Tableau de Score:
Modification des tailles des fenêtre pour permettre un affichage au dessus de la fenêtre de jeu.
A chaque fois que l’élément est attrapé il s’affiche sur le dessus . Ceci se fait par le contrôle de la liste TOOLS.
J’ai ajouté une condition à la méthode display_element .


Modifications possibles:
Ajout de niveaux possibles (cartes supplémentaires)
Ajout de nouveaux éléments
Possibilité de déplacer le Gardien en l’ instanciant comme un Héros.









