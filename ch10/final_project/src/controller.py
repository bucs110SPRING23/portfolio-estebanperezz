import pygame
import random 
#from src.Bullet import Bullet
#from src.enemy import Enemy

class Controller:
    def __init__(self):
        width = 800 
        height = 600
        x = 200 
        y = 300
        self.screen = pygame.display.set_mode((width,height))
      #  self.enemies = []
        #self.enemies.append(Enemy(x,y,"string"))

    def mainloop(self):
        """is the main loop that is going to run the program"""
        width = 800 
        height = 600
        #screen = pygame.display.set_mode((width,height))
        rectheight = 50 
        rectwidth = 80 
        rect_x = 0 
        
        num_rectangles = 10 
        heights = [random.randint(20, 100) for _ in range(num_rectangles)]
        
        print (heights)
        colors = [random.choice(("red","green","white","purple","yellow","pink")) for _ in range(num_rectangles)]
        while (True): #this can also be a variable instead of just True 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill("black")
            clock = pygame.time.Clock()
            for i in range(num_rectangles):
                clock.tick(60)
                recty = height -rectheight- (height/random.randint(1,10))
                rect_x = i * (width / (num_rectangles) )
                rectheight = heights[i]
                pygame.draw.rect(self.screen,colors[i],(rect_x,recty,rectwidth,rectheight))
            pygame.display.update()

            