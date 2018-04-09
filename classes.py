#!/usr/bin/python3.5
# -*-coding:utf-8 -
"""Place where Classes are """

from constant import*

class Map():
    """class object Map which define the labyrinth.
    It has one attribut : an empty grid.
    and takes as parameter the file.txt which contains the map.
    This class has two method: one to generate the structure : a list of list
    and one to display the grid over the pygame window."""

    def __init__(self, file):
        self.file = file
        self.grid = []

    def generate(self):
        """Method which generate the structure from the file.txt"""
        frame = []
        #let generate the list of lists
        with open(self.file, "r") as file:
            for line in file:
                line = line.strip() #be careful to cut the line break
                frame.append(list(line))
        self.grid = frame # we get the list of lists in the attribut

    def display(self, window):
        """from the grid we display each sprite match with a code : 
        "w" for picture of a wall , "a" for the guardian. Each sprite have
        x and y coordinates and a size in pixel."""
        num_line = 0 #we begin with the first list so the fist line
        for line in self.grid:
            num_sprite = 0 #we begin withe the first square
            for sprite in line:
                X = num_sprite * SPRITE_SIZE
                Y = num_line * SPRITE_SIZE
                if sprite == "w":
                    window.blit(WALL, (X, Y)) #we load a wall picture over the window
                if  sprite == "a":
                    window.blit(ARRIVAL, (X, Y)) #we load a arrival picture over the window
                num_sprite += 1
            num_line += 1
          