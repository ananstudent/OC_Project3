#!/usr/bin/python3.5
# -*-coding:utf-8 -

"""Program "Help MacGyver to escape!"""

from constant import*
from classes import*
from function import*

#Open game window
pygame.display.set_icon(ICONE)
pygame.display.set_caption(TITLE_WINDOW)


######MAIN_LOOP############
MAIN_LOOP = True
while MAIN_LOOP:
    #Load home screen
    window.blit(HOME, (0, 0))
    #Reload display
    pygame.display.flip()
    #loop delay

######HOME LOOP###############
    HOME_LOOP = True
    while HOME_LOOP:

        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            #Quit the program
            if event.type == QUIT:
                print("Bye bye!")
                MAIN_LOOP = False
                HOME_LOOP = False
                GAME_LOOP = False

            #Quit home loop to enter in game loop
            if event.type == KEYDOWN and event.key == K_RETURN:
                print("Welcome to the game")
                HOME_LOOP = False
                GAME_LOOP = True
                #Load the game's map
                file = "map/N1.txt"

    if file != "": #We make sure that the file really exists and is not empty
        
        #load the background
        window.blit(BACKGROUND, (0, 0))
        
        #generate the labyrinth
        labyrinth = Map(file)
        labyrinth.generate()
        labyrinth.display(window)

        #Get the items in the labyrinthe
        syringue = Elements("s",labyrinth)
        syringue.locate_elements()
        syringue.pin_elements()
        print(syringue.sprite_x,syringue.sprite_y)
        print(labyrinth.grid)

        #And God create an Heroe
        MacGyver = Heroe(labyrinth)
        

#########GAME_LOOP##############
    while  GAME_LOOP:
        print("Je suis là")
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            
            #Quit the program
            if event.type == QUIT:
                print("Bye bye!")
                MAIN_LOOP = False
                GAME_LOOP = False
            
            if event.type == KEYDOWN:
                
                #Quit the game and go back Home
                if event.key == K_ESCAPE:
                    GAME_LOOP = False
                
                #Move our heroe!
                if event.key == K_RIGHT:
                    MacGyver.move("right")
                if event.key == K_LEFT:
                    MacGyver.move("left")
                if event.key == K_DOWN:
                    MacGyver.move("bottom")
                if event.key == K_UP:
                    MacGyver.move("up")                
        
        window.blit(BACKGROUND, (0, 0))
        labyrinth.display(window)
        #Add MacGyver in the Labyrinth with his position
        window.blit(MG, (MacGyver.x, MacGyver.y))
        #Add Element in the Labyrinth
        window.blit(SYRINGE, (syringue.x, syringue.y))



        pygame.display.flip()

        if labyrinth.grid[MacGyver.sprite_x][MacGyver.sprite_y] == "a":
            print("You win!")
            GAME_LOOP = False
