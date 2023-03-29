import random 
import pygame
class LED:
    #usually classes go in their own file, one class per file 
    #functions are called methods when they are in a class
    #first parameter to any method is itself
   
    def __init__(self,x=0,y=0,color="red"): 
        self.on = True
        self.rect = pygame.Rect(abs(x),abs(y),5,5)
        self.color = color
        self.radius = 5 
    def change_color(self,new_color):
        
        new_color =[random.randint(0,255),random.randint(0,255),random.randint(0,255) ]
        self.color = new_color