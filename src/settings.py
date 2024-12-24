"""
    Project/Settings
"""
import pygame #pygame is the python module we're creating the game with, so you must import it into the program
import sys # importing the python module "sys" to handle system functions like closing the program cleanly


# Screen constants
WIDTH = 640
HEIGHT = 512
RES = (WIDTH,HEIGHT)

# Frames Per Sec
FPS = 60

# Tile size, not super important for this project but helpful for larger engines
TILE = 16

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


 # defining a method that returns the default font style with the variable size we'll enter later
def get_font(size):
    return pygame.font.Font(None,size)