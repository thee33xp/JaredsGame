"""
    Project/injen
"""
from src.settings import *# importing all of our settings.py file to keep our code clean
from src.classes import PLAYER # importing our player class from our classes.py file
class Game_Engine: #The class called "Game_Engine" will manage our event loop and our event handler
    def __init__(self): # This is where the game engine is initialized and variables are set
        pygame.init() # This calls the pygame initalization method 
        self.ViewPort = pygame.display.set_mode((RES)) # This is the screen or viewing window our game will be displayed on
        self.Caption_and_Icon() # setting the window name and replacing the pygame logo with our own
        self.CLOCK = pygame.time.Clock() #This is our clock to manage our time.. w/o it will run as fast as the computer can
        self.ENABLED = True # This is a constant to control our game. If the engine is enabled, the game runs. else quits.
        self.bigpoppa = PLAYER(x=200,y=200,speed=5) # calling our player class, naming it big poppa, giving it x/y pos & speed
    def Caption_and_Icon(self):
        icon = pygame.image.load("src/img/icon.png") # loading the image of the "icon.png" under the name icon
        pygame.display.set_icon(icon) # setting the display icon with the loaded image
        pygame.display.set_caption("Jared's Game") # setting the display caption 
    def Write_Words(self):
        # Title on Screen
        txt = get_font(64).render("Jared's Game", True, WHITE) # calling our font method and rendering our desired text and color
        txt_rect = txt.get_rect(center=(WIDTH/2,32)) # setting the position of the rendered text 
        self.ViewPort.blit(txt,txt_rect) # drawing/"blitting" the rendered txt at the established rect location
        # Player Direction
        dir = get_font(24).render(f"Direction:{self.bigpoppa.direction}",True,WHITE)
        dir_rect = dir.get_rect(topleft=(TILE,TILE*3))
        self.ViewPort.blit(dir,dir_rect)
        # Player Moving True/False
        moving = get_font(24).render(f"Moving:{self.bigpoppa.moving}",True,WHITE)
        mov_rect = moving.get_rect(topleft=(TILE,TILE*6))
        self.ViewPort.blit(moving,mov_rect)
    def Event_Handler(self): # This is the event_handler, it'll handle all the key presses, mouse clicks, etc...
        for event in pygame.event.get(): # this is the general way to get events in pygame
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # getting the exit/escape event
                self.ENABLED = False # if the window is closed or escape key is pressed > our game is no longer enabled
                pygame.quit() # quits the pygame program
                sys.exit() # uses the system exit function to close the program
            elif event.type == pygame.KEYDOWN: # getting the event.type KEYDOWN    
                if event.key == pygame.K_LEFT:
                    self.bigpoppa.moving = True
                    self.bigpoppa.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    self.bigpoppa.moving = True
                    self.bigpoppa.direction = "right"
                elif event.key == pygame.K_UP:
                    self.bigpoppa.moving = True
                    self.bigpoppa.direction = "up"
                elif event.key == pygame.K_DOWN:
                    self.bigpoppa.moving = True
                    self.bigpoppa.direction = "down"
            elif event.type == pygame.KEYUP:  # getting the event.type KEYUP
                if event.key == pygame.K_LEFT:
                    self.bigpoppa.moving = False
                elif event.key == pygame.K_RIGHT:
                    self.bigpoppa.moving = False
                elif event.key == pygame.K_UP:
                    self.bigpoppa.moving = False
                elif event.key == pygame.K_DOWN:
                    self.bigpoppa.moving = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # getting the event.type mouse buttons clicked
                print(f"{event.button}")  
                # this is just printing which button you clicked.
    def Event_Loop(self): # This is the event_loop, it embodies and manages our game loop and events within it
        while self.ENABLED: # or while self.ENABLED == True:
            self.CLOCK.tick(FPS) # this makes our clock tick to our set FPS of 60
            self.ViewPort.fill(BLACK)
            self.Write_Words() # calling our method for writing on the screen
            self.bigpoppa.move() # calling the move method of the player class to ensure movement occurs properly
            self.Event_Handler() # Calling our event handler method within our game loop makes it active
            self.bigpoppa.update(surf=self.ViewPort) # Calling the method for drawing the player and entering the surface i want it drawn onto
            pygame.display.flip() # Update/Flip the display to actually see the frame changes