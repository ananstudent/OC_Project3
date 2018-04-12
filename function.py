#!/usr/bin/python3.5
# -*-coding:utf-8 -
"""Place where functions are """

import random 
from constant import*
if labyrinth.grid[tube.sprite_y][tube.sprite_x] == "t":
    tube.display_elements(window)

if labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] == "t":
    print("Yeah! You caught the tube!")
    labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
    TOOLS.append("tube")
    print(TOOLS)


        #Add conditionnal display of Element
        if labyrinth.grid[tube.sprite_y][tube.sprite_x] == "t":
            tube.display_elements(window)

        if labyrinth.grid[syringe.sprite_y][syringe.sprite_x] == "s":
            syringe.display_elements(window)

        if labyrinth.grid[ether.sprite_y][ether.sprite_x] == "e":
            ether.display_elements(window)     
        
        if labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] == "t":
            print("Yeah! You caught the tube!")
            labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
            TOOLS.append("tube")
            print(TOOLS)

        if labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] == "s":
            print("Yeah! You caught the syringe!")
            labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
            TOOLS.append("syringe")
            print(TOOLS)


        if labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] == "e":
            print("Yeah! You caught the ether!")
            labyrinth.grid[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
            TOOLS.append("ether")
            print(TOOLS)

    