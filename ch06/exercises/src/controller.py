import pygame
class Controller:
    def __init__(self):
        """initialization of models and any other data needed"""
        pygame.init() 
class Foo():
    def __init__(self) -> None:
        self.num = 5 
    def addone(self):
        self.num += 1 
class Bar(Foo):
    def addsub(self):
        self.num +=1 
b = Bar()
b.addone()
print (b) 
