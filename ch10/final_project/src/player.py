import pygame
import os
""""
makes up the mario omage that we see on the screen
args:x ,y 
return:sprite """
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x = x ## start ,x , y 
        self.y = y 
        self.width = 50 
        self.height = 50 

        self.lives = 3 
        super().__init__()
        self.velocity = 0 
        self.isjumping = False
        self.jump_speed = 10
        self.fall_speed = 5 
        path = os.path.join('ch10/final_project/assets','mario.jpeg')
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
    def jump (self,status=True):
        self.isjumping = self.status
        if self.velocity == 0:
            self.velocity = -self.jump_speed
    def update(self,boolblock): ## 10 frames for the jump 
        if boolblock:
            self.velocity = 0
        else:
            self.velocity+=self.fall_speed
        self.y += self.velocity 
        
    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),(self.x,self.y,self.width,self.height))
        surface.blit(self.image, (self.x, self.y))
    def reset_position(self,x,y):
        self.x = x 
        self.y = y 
        self.rect.x = x 
        self.rect.y = y 
        