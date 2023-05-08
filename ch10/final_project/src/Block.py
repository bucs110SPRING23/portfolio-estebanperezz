import pygame
import os 
"""is the block that makes up the objects one is supposed to avoid 
args:x,y
return:rect"""
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x 
        self.y = y 
        path = os.path.join('ch10/final_project/assets','block.jpg')
       
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.rect.width = 50 
        self.rect.height = 100
    def update(self,level): ## based on level , generate heights, move the rectangles. 
        self.rect.y -= 1 
    def draw(self,surface): ## draw sprite
        pygame.draw.rect(surface,(255,0,0),(self.x,self.y,self.rect.width,self.rect.height))
        surface.blit(self.image, (self.x, self.y))
        

        
        
