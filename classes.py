#!/usr/bin/python3.5
# -*-coding:utf-8 -
"""Place where Classes are """
import random
from constant import*

class Map():
    """class object Map which define the labyrinth.
    It has one attribut : an empty grid.
    and takes as parameter the file.txt which contains the map.
    This class has two methods: one to generate the structure : a list of list
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
            num_sprite = 0 #we begin with the first square
            for sprite in line:
                X = num_sprite * SPRITE_SIZE
                Y = num_line * SPRITE_SIZE
                if sprite == "w":
                    window.blit(WALL, (X, Y)) #we load a wall picture over the window
                if  sprite == "a":
                    window.blit(ARRIVAL, (X, Y)) #we load a arrival picture over the window
                num_sprite += 1
            num_line += 1

class Elements():
    """Class which define the various elements. It take in parameter the labyrinth and the name of the element.
    Two methods: one to locate with random choice the position and one to write the grid in order to get the element later"""
    def __init__(self, name, labyrinth):
        #Position in pixel:
        self.x = 0
        self.y = 0
        #Position in square:
        self.sprite_x = 0
        self.sprite_y = 0
        #Name of the elements
        self.name = name
        #Labyrinth
        self.labyrinth = labyrinth


    def locate_elements(self):
        """To locate one element: we detecte empty cell. We catch the coodrinate in a list of tuple
        (y,x), we choice one pair of co-ordinates"""
        position = []
        coordinates = ()
        num_line = 0
        while num_line < len(self.labyrinth.grid):
            num_cell = 1 # We remove the first cell - the cell of departure
            while num_cell < len(self.labyrinth.grid[0]):#By default, the lenght of the first line
                if self.labyrinth.grid[num_line][num_cell] == "0":
                    coordinates = (num_line, num_cell)
                    position.append(coordinates)
                num_cell +=1
            num_line +=1       

        element_coordinates = random.choice(position)
        self.sprite_y = element_coordinates[0]
        self.sprite_x = element_coordinates[1]
        self.x = self.sprite_x * SPRITE_SIZE
        self.y = self.sprite_y * SPRITE_SIZE


    def pin_elements(self):
        """Pin the name of the element to help MacGyver to find it"""
        self.labyrinth.grid[self.sprite_y][self.sprite_x] = self.name


class Heroe():
    """ class which define a character to deplace with x and y position and motion
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
                if self.labyrinth.grid[self.sprite_y+1][self.sprite_x] != "w": #not to go to a wall
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


