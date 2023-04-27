"""Initlializes the window object args:
x:how wide the window will be 
y: how tall the window will be
idbnum: identifies the window the user is in
img_file:path to images"""
import random
class Finalboss:
    def __init__(self,x,y,health,attackmode,image):
        self.x = x 
        self.y = y 
        self.health = health 
        self.image = random(0,3) ## Will choose out of three boss images everytime a boss level is reached
        self.attackmode = attackmode 
        self.difficultylevels = ["Almost dead","Weak","Moderate Health","Extremely Powerful"]
        self.attackmodes = ["easy", "medium", "hard"]
    def difficultylevel(self):
        if self.attackmode not in self.attackmodes:
            return "Boss mode not recongnized"
        elif self.health< 0:
            return "Boss likely dead"
        else:
            diffuculty_index = min(int(self.health//250),len(self.difficultylevels) - 1 )
            return self.difficultylevels(diffuculty_index)
        pass
        
