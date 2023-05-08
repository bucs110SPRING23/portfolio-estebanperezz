import pygame
import time
import random 

from src.Block import Block
from src.player import Player
"""controls and starts all info neccessary to play the game
args:none
return:none"""
class Controller:
    def __init__(self):
        width = 800 
        height = 800
        self.x = 400 
        self.y = 400
        self.lives = 3
        self.screen = pygame.display.set_mode((width,height))
        self.rects= [] 
        self.num_rectangles = 10 
        self.new_x = 0 
        self.randstart = -100
        self.randend = 100
        self.new_y = 0 
        self.playergroup = pygame.sprite.Group()
        self.blockgroup = pygame.sprite.Group()
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.offset = 50 
        self.textdim = 10,10 
        self.player_speed = 50 
        self.level = 1 
        self.screendimensions = 800,800 
        self.fontdimensions1 = 10,10
        self.fontdimensions2 = 10,40 
        self.ybounds = 800
        self.xbounds = 800
        self.playerybounds = 600
        self.player_rect_y = 0 
        self.player_rect_x = 0 
        self.fontdimensions3 = 100,400
        self.menudimensions = 255,255,255
    def playgame(self):
        """is the main loop that is going to run the program
        args:none
        return :none"""
        pygame.init() 
        width = 800 
        screenheight = 600
        #screen = pygame.display.set_mode((width,height))
        rectheight = 50 

        
        screen = pygame.display.set_mode(self.screendimensions)

        # Define menu options
      
        
        blockheights = [random.randint(20, 100) for _ in range(self.num_rectangles)]
    
        print (blockheights)

        clock = pygame.time.Clock()

        
   
        while (True):
           

            clock.tick(5)
            for event in pygame.event.get():
                    ##check keys here for all events 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        break
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
            self.screen.fill("black")
            player1 = Player(self.player_rect_x,self.player_rect_y)
            font = pygame.font.Font(None, 36)
            lives_text = font.render(f"Lives: {self.lives}", True, self.green)
            level_text=font.render(f"Level: {self.level}", True, self.red)
            screen.blit(lives_text, self.fontdimensions1)
            screen.blit(level_text,self.fontdimensions2)
            player1.draw(self.screen)
            self.playergroup.add(player1)
        ##for loop 
            Rect_block = Block(0,400)
       # Rect_block.draw(self.screen) ## DRAW 1 
            self.blockgroup.add(Rect_block) #this can also be a variable instead of just True 
            
          
            for i in range(1,self.num_rectangles):
                if i % 2 == 0:
                    center_y = (screenheight - rectheight) / 2
                    random_offset = random.randint(self.randstart, self.randend)
                    recty = center_y + random_offset
                
                    #recty = screenheight -rectheight- (screenheight/random.randint(self.randstart,self.randend))
                    rect_x = i * (width / (self.num_rectangles) )
                    rectheight = blockheights[i]
                    Rect_block = Block(rect_x,recty)
                    Rect_block.draw(self.screen)
                    self.blockgroup.add(Rect_block) ## Draw 2 
 
             #   if pygame.sprite.groupcollide(self.blockgroup,self.playergroup, False, False):
                #    print("Block group collided with player group")
            keys = pygame.key.get_pressed()
            ###Player out of lives 
            gameover = False
     
            if self.lives> 0:
                gameover = False 

                if self.player_rect_y >= 0 and self.player_rect_y <= self.playerybounds:
                    if keys[pygame.K_UP]:
                        self.new_y = self.player_rect_y - self.player_speed
                        if self.new_y >= 0:
                            self.player_rect_y = self.new_y
                        else:

                            self.player_rect_y = self.offset
                    if keys[pygame.K_DOWN]:
                        self.new_y = self.player_rect_y + self.player_speed
                        if self.new_y <= self.ybounds:
                            self.player_rect_y = self.new_y
                        else:
                            gameover = True 
                            self.player_rect_y = self.ybounds
                if self.player_rect_x >= 0 and self.player_rect_x <= 750:
                    if keys[pygame.K_LEFT]:
                        self.new_x = self.player_rect_x - self.player_speed
                        if self.new_x >= 0:
                            self.player_rect_x = self.new_x
                        else:
                            player_rect_x = 0
                    if keys[pygame.K_RIGHT]:
                        self.new_x = self.player_rect_x + self.player_speed
                        if self.new_x <= 750:
                            self.player_rect_x = self.new_x
                        elif self.player_rect_x >= 650:
                            #self.player_rect_x = 0
                            self.randstart = self.randstart - 100
                            self.randend += 100 
                            self.level +=1 
                        

                for s in self.blockgroup:
                    collisions = pygame.sprite.spritecollide(s, self.playergroup, False)
                if collisions:
                   # self.player_rect_x = 0 
                    self.player_rect_y = 400

                    #time.sleep(3)
                   # self.lives = self.lives- 1 
                    if self.lives == 0:

                        break

            
         
                    

                
            else:
                gameover == True 
                endl_text=font.render(f"END GAME", True, self.red)
                screen.blit(lives_text, self.fontdimensions3)

                pass
                



          
           
        

            pygame.display.update()
            """controls when the game starts 
            args:none 
            return:none"""
    def mainloop(self):
        options = ["Start Game press return", "Exit press esc"]

        
        font = pygame.font.Font(None, 36)

        # Create menu s
        menu = pygame.Surface((300, 200))
        menu.fill(self.menudimensions)

        text_rects = []
        for i, option in enumerate(options):
            text = font.render(option, True, (0, 0, 0))
            rect = text.get_rect(center=(menu.get_width() // 2, 50 + 50 * i))
            text_rects.append(rect)
            menu.blit(text, rect)

     
        selected_option = 0
        selected_rect = pygame.Rect(0, 0, menu.get_width(), 50)
        selected_rect.center = text_rects[selected_option].center

        pygame.draw.rect(menu, (255, 0, 0), selected_rect, 3)

        # Display menu on screen
        menu_rect = menu.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(menu, menu_rect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                    ##check keys here for all events 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.playgame()
                        break
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            