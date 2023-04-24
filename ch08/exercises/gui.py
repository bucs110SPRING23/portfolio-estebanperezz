import pygame
import random 
class Player:
    def __init__(self,pnum = 1 ):
        self.player_num = pnum 
        self.health = 10 
        self.forward = False 
class Landscape:
    def __init__(self):
        self.ismoving = True 
        self.powerblock = random.randint(0,3)
        self.clouds = random.randint(0,10)
class Enemy:
    def __init__(self):
        self.generate = random.randint(0,10)
        self.obstacle = False 
        self.isdead = False 