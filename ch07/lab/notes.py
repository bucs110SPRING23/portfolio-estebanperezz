import pygame
class Snowman(pygame.sprite.Sprite):

    def __init__(self,x,y,img="assets/snowman.png")->None:
        super().__init__() 
        self.image = pygame.image.load(img) 