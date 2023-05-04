import pygame
import random 
#from src.Bullet import Bullet
#from src.enemy import Enemy
from src.player import Player

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
        screenheight = 600
        #screen = pygame.display.set_mode((width,height))
        rectheight = 50 
        rectwidth = 80 
        rect_x = 0 
        player_rect_x = 25 
        player_speed = 50 
        num_rectangles = 10 
        x = 0 
        heights = [random.randint(20, 75) for _ in range(num_rectangles)]
        #playery = heights[0]-50 
        #player1 = Player(0,playery)
        print (heights)
        colors = [random.choice(("red","green","white","purple","yellow","pink")) for _ in range(num_rectangles)]
        clock = pygame.time.Clock()
        #player_rect_y = (height - (height/random.randint(1,10)))-50
        #pygame.draw.rect(self.screen,colors[0],(0,player_rect_y,rectwidth,heights[0]))
        while (True): #this can also be a variable instead of just True 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill("black")
            player_rect_y =50 #(screenheight -rectheight- (screenheight/random.randint(4,10)))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_rect_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_rect_x += player_speed
                
            pygame.draw.rect(self.screen,colors[0],(0,player_rect_y,rectwidth,heights[0]))
            
            for i in range(1,num_rectangles):
                clock.tick(10)
                if i ==1:
                    
                    player1 = Player(player_rect_x,player_rect_y-50)

                recty = screenheight -rectheight- (screenheight/random.randint(5,10))
                rect_x = i * (width / (num_rectangles) )
                rectheight = heights[i]
                pygame.draw.rect(self.screen,colors[i],(rect_x,recty,rectwidth,rectheight))
            player1.draw(self.screen)
            
            pygame.display.update()

            