import pygame
import random 
#from src.Bullet import Bullet
#from src.enemy import Enemy
from src.player import Player

class Controller:
    def __init__(self):
        width = 800 
        height = 600
        self.x = 200 
        self.y = 300
        self.screen = pygame.display.set_mode((width,height))
        self.rects= [] 
        self.num_rectangles = 10 
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
        
        
        heights = [random.randint(20, 75) for _ in range(self.num_rectangles)]
        #playery = heights[0]-50 
        #player1 = Player(0,playery)
        print (heights)
        colors = [random.choice(("red","green","white","purple","yellow","pink")) for _ in range(self.num_rectangles)]
        clock = pygame.time.Clock()
        player_rect_y = (screenheight - (screenheight/random.randint(5,10)))-50
        first_rect = player_rect_y
        player1 = Player(0,player_rect_y)
        
        #pygame.draw.rect(self.screen,colors[0],(0,player_rect_y,rectwidth,heights[0]))
        while (True): #this can also be a variable instead of just True 
            clock.tick(10)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                        #player1.update(boolblock=#(player1.y+player1.height)>=player_rect_y)
                        #print("PLAYER JUMP")
            self.screen.fill("black")
            # #(screenheight -rectheight- (screenheight/random.randint(4,10)))
            keys = pygame.key.get_pressed()
            if player_rect_y > 0 and player_rect_y < 800:
                if keys[pygame.K_UP]:
                    player_rect_y -= player_speed
                if keys[pygame.K_DOWN]:
                    player_rect_y+= player_speed
            if keys[pygame.K_LEFT]:
                player_rect_x -= player_speed
            if keys[pygame.K_RIGHT]:
                player_rect_x += player_speed
                
            pygame.draw.rect(self.screen,colors[0],(0,first_rect,rectwidth,heights[0]))
           # player1.update(boolblock=(player1.y+player1.height)>=player_rect_y)
            for i in range(1,self.num_rectangles):
               
                
                if i ==1:
                    pass   
                
                player1 = Player(player_rect_x,player_rect_y-50)
                player1.update(boolblock=(player1.y+player1.width)>=player_rect_y)
                player1.draw(self.screen)

                recty = screenheight -rectheight- (screenheight/random.randint(5,10))
                rect_x = i * (width / (self.num_rectangles) )
                rectheight = heights[i]
                #set equal to block 
                pygame.draw.rect(self.screen,colors[i],(rect_x,recty,rectwidth,rectheight)) ##
               # if player1.rect.colliderect(block):
                  #  player1.isjumping(False)

            player1.draw(self.screen)
            
            pygame.display.update()

            