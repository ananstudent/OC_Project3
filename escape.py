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
    

######HOME LOOP###############
    HOME_LOOP = True
    while HOME_LOOP:

        #play soundtrack
        SOUNDTRACK.play()

        #loop delay
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
                
                #######WELCOME TO THE GAME##########
                SOUNDTRACK.stop()
                window.blit(BACKGROUND, (0, 0))
                window.blit(WELCOME, (90, 120))
                pygame.display.flip()
                time.sleep(1)
                ####################################
                
                HOME_LOOP = False
                GAME_LOOP = True
  
                #Load the game's map
                FILE = "map/N1.txt"

    if FILE != "": #We make sure that the file really exists and is not empty
        
        #load the background
        window.blit(BACKGROUND, (0, 0))
        
        #generate the labyrinth
        labyrinth = Map(FILE)
        labyrinth.generate()
        labyrinth.display(window)

        #Get the items in the labyrinthe

        syringe = Elements("syringe", SYRINGE, labyrinth)
        syringe.locate_elements()
        syringe.pin_elements()

        ether = Elements("ether", ETHER, labyrinth)
        ether.locate_elements()
        ether.pin_elements()

        tube = Elements("tube", TUBE, labyrinth)
        tube.locate_elements()
        tube.pin_elements()

        #And God create an Heroe
        MacGyver = Heroe(labyrinth)
        
#########GAME_LOOP##############
    #Initialyse at every game_loop an empty list to put the elements inside
    TOOLS = []
    while  GAME_LOOP:

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
        
        #Display the game board
        window.blit(BACKGROUND, (0, 0))
        labyrinth.display(window)
        
        #Add MacGyver in the Labyrinth with his position
        window.blit(MG, (MacGyver.x, MacGyver.y))

        #Add conditionnal display of Element

        tube.display_elements(window, MacGyver, TOOLS)
        syringe.display_elements(window, MacGyver, TOOLS)
        ether.display_elements(window, MacGyver, TOOLS)
        pygame.display.flip()    


        if labyrinth.grid[MacGyver.sprite_x][MacGyver.sprite_y] == "a":

            #The gamer win if he has the tree elements
            if len(TOOLS) < 3:

                #####DISPLAY GAME OVER#####
                window.blit(GAMEOVER, (150, 150))
                pygame.display.flip()
                time.sleep(2)
                ###########################
                print("You loose")
                GAME_LOOP = False

            if len(TOOLS) == 3:
                ######DISPLAY YOU WIN#####        
                window.blit(WIN, (100, 150))
                pygame.display.flip()
                time.sleep(2)
                ##########################                
                print("You win!")
                GAME_LOOP = False
