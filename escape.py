#!/usr/bin/python3.5
# -*-coding:utf-8 -

"""Program "Help MacGyver to escape!"""

from constant import*
from classes import*

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
                #GAME_LOOP = True
                #Load the game's map
                file = "map/N1.txt"

    if file != "" : #We make sure that the file really exists and not empty
        #load the background
        window.blit(BACKGROUND, (0, 0))
        #generate the labyrinth
        labyrinth = Map(file)
        labyrinth.generate()
        labyrinth.display(window)
        pygame.display.flip()


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
            #Quit the game and go back to home
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                GAME_LOOP = False
        pygame.display.flip()



