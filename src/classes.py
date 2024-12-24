"""
    Project/classes
"""
from src.settings import *
class PLAYER:
    def __init__(self,x,y,speed):
        self.speed = speed
        self.image = pygame.Surface((TILE,TILE))
        self.image.fill("Yellow")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = "down"
        self.directions = [ "down", "up", "left", "right" ]
        self.moving = False      
    def Screen_Collision(self):
        if self.rect.left +self.dx < 0:
            self.dx = 0
            print("Collision detected on left side")
        if self.rect.right +self.dx > WIDTH:
            self.dx = 0
            print("Collision detected on right side")
        if self.rect.top + self.dy < 0:
            self.dy = 0
            print("Collision detected on top side")
        if self.rect.bottom + self.dy > HEIGHT:
            self.dy = 0
            print("Collision detected on butt side")
    def move(self):
        """
            we establish variables dx,dy as our delta X/Y position. Think about it like a Cartesian Coordinate System
            your player is a rectangle on a graph at position x & y, so if the conditions are met then the player's rect will
            move in the given direction at the given speed
            
        """
        self.dx, self.dy = 0,0
        if self.moving:
            if self.direction == "down":
                self.dy = self.speed
            elif self.direction == "up":
                self.dy =-self.speed
            elif self.direction == "left":
                self.dx = -self.speed
            elif self.direction == "right":
                self.dx = self.speed
        else:
            self.dx,self.dy = 0,0
        self.Screen_Collision() # Calling our method to prevent the player from going off of the screen
        # ^^^^ screen collision must be called prior to the actual rect movement or else won't work
        self.rect.x += self.dx  # this is what moves the rect at the value of the delta x 
        self.rect.y += self.dy # this is what moves the rect at the value of the delta y
    def update(self,surf):
        surf.blit(self.image,(self.rect))
