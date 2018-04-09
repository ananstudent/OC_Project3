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

class Heroe():
    """ class whitch define a character to deplace with x and y position and motion
    This character moves inside a labyrinth so the class take one parameter : labyrinth object """

    def __init__(self, labyrinth):
        #Position in pixel:
        self.x = 0
        self.y = 0
        #Position in square:
        self.sprite_x = 0
        self.sprite_y = 0
        #Labyrinth
        self.labyrinth = labyrinth

    def move(self, direction):
        """Method whitch allows to move the character. This method takes in parmeter 
        the direction where the heroes must go."""

        #Move to the right
        if direction == "right":
            if self.sprite_x < NB_SPRITE -1: #to avoid go out of the screen
                if self.labyrinth.grid[self.sprite_y][self.sprite_x+1] != "w": #not to go to a wall
                    #move of a sprite
                    self.sprite_x += 1
                    #Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE

        #Move to the left
        if direction == "left":
            if self.sprite_x > 0: #to avoid go out of the screen
                if self.labyrinth.grid[self.sprite_y][self.sprite_x-1] != "w": #not to go to a wall
                    #move of one sprite
                    self.sprite_x -= 1
                    #Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE            

        #Move to the bottom
        if direction == "bottom":
            if self.sprite_y < NB_SPRITE-1: #to avoid go out of the screen
                if self.labyrinth.grid[self.sprite_y+1][self.sprite_x] != "m": #not to go to a wall
                    #move on one sprite
                    self.sprite_y += 1
                    #Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE
            
       
        #Move to the top
        if direction == "up":
            if self.sprite_y > 0: #to avoid go out of the screen
                if self.labyrinth.grid[self.sprite_y-1][self.sprite_x] != "w": #not to go to a wall
                    #move on one sprite
                    self.sprite_y -= 1
                    #Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE