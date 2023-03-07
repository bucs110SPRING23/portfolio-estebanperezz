import pygame 
import math 
import random 
pygame.init() 
screen= pygame.display.set_mode((500,500))
screen_size = pygame.display.get_window_size()
center = [screen_size[0]//2,screen_size[1]//2]
print(center)
print(screen_size)

#starting_point = [dimensions[0]//2,dimensions[0]//2-200]
# distance_from_center = math.hypot(randomnx -center[0],randomy- center[1]) 
# is_in_cirlce = (distance_from_center <=center[0])
# print(is_in_cirlce)

            
# pygame.draw.circle(screen, color ="red",center=center,radius= center[0])
# # pygame.draw.circle(screen, color ="black",center=(randomnx,randomy),radius=3)
# pygame.draw.line(screen,color="blue",start_pos=(0,250), end_pos=[500,250])
# pygame.draw.line(screen,color="blue",start_pos=(250,0),end_pos=(250,500)) 
rect1 = pygame.draw.rect(screen,"yellow",[0,0,100,100])
rect2 = pygame.draw.rect(screen,"green",[400,0,100,100])
font= pygame.font.Font(None,18)
text1= font.render("Bet Player 1",True,"black")
text2= font.render("Bet Player 2",True,"black")
screen.blit(text1, (0,0))
screen.blit(text2, (400,0))
pygame.display.flip()
play1bet = False 
play2bet = False
player1 = 0 
player2 = 0 
events = True
def drawBoard():
     pygame.draw.circle(screen, color ="red",center=center,radius= center[0])
# pygame.draw.circle(screen, color ="black",center=(randomnx,randomy),radius=3)
     pygame.draw.line(screen,color="blue",start_pos=(0,250), end_pos=[500,250])
     pygame.draw.line(screen,color="blue",start_pos=(250,0),end_pos=(250,500)) 
def randcordinates():
    randomnx = random.randrange(1,screen_size[0])
    randomy = random.randrange(1,screen_size[1])
    return (randomnx,randomy)
def checkdistance(randx,randy):
     distance_from_center = math.hypot(randx -center[0],randy- center[1]) 
     is_in_cirlce = (distance_from_center <=center[0])
     print(is_in_cirlce)
     return is_in_cirlce
def checkWinner():
     if player1> player2:
         text = font.render("Player 1 Won",True,"white")
         screen.blit(text, (150,0))
         if play1bet == True:
            text2 = font.render("Your bet was right",True,"white")
            screen.blit(text2,(150,50))
         elif play2bet == True:
            text2 = font.render("Your bet was wrong",True,"white")
            screen.blit(text2,(150,100))
     elif player2> player1:
            text = font.render("Player 2 Won",True,"white")
            screen.blit(text, (150, 0))
            if play1bet == True:
                text2 = font.render("Your bet was Wrong",True,"white")
                screen.blit(text2,(150,200))
            elif play2bet == True:
                text2 = font.render("Your bet was Right",True,"white")
                screen.blit(text2,(150,250))
     else:
        text = font.render("Player No One Won",True,"white")
        screen.blit(text, (150, 0))
     pygame.display.flip()

def dartGame():
     player1 = 0 
     player2 = 0 
     for _ in range(10):
        xcord1,ycord1 = randcordinates()
        xcord2,ycord2 = randcordinates()
    # distance_from_center = math.hypot(xcord -center[0],ycord- center[1]) 
        distanceCenter1 = checkdistance(xcord1,ycord1)
        distanceCenter2 = checkdistance(xcord2,ycord2)
    # is_in_cirlce1 = (distanceCenter <=center[0])
    # is_in_cirlce2 =(distanceCenter <=center[0])
        print(distanceCenter1)
        print(distanceCenter2)
    # print(xcord1,xcord2,ycord1,ycord2)
        if distanceCenter1 == True:
         pygame.draw.circle(screen,"blue",(xcord1,ycord1),5)
         player1+=1 

        else:
             pygame.draw.circle(screen,"green",(xcord1,ycord1),5)
        if distanceCenter2 == True:
             pygame.draw.circle(screen,"black",(xcord2,ycord2),5)
             player2+=1 

        else:
             pygame.draw.circle(screen,"yellow",(xcord2,ycord2),5)
     pygame.display.flip()
events = True 
while events:
     for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                 drawBoard()
                 if rect1.collidepoint(event.pos):
                        play1bet = True 
                        # drawBoard()
                        
                        dartGame()
                        
                        checkWinner()
                        pygame.display.flip()
                        
                        
       
                 elif rect2.collidepoint(event.pos):
                        play2bet = True 
                       # drawBoard() 
                        dartGame()
                        
                        checkWinner()
                        pygame.display.flip()
                        
                        
                        
                 


pygame.display.flip()
# for _ in range(10):
#     xcord1,ycord1 = randcordinates()
#     xcord2,ycord2 = randcordinates()
#     # distance_from_center = math.hypot(xcord -center[0],ycord- center[1]) 
#     distanceCenter1 = checkdistance(xcord1,ycord1)
#     distanceCenter2 = checkdistance(xcord2,ycord2)
#     # is_in_cirlce1 = (distanceCenter <=center[0])
#     # is_in_cirlce2 =(distanceCenter <=center[0])
#     print(distanceCenter1)
#     print(distanceCenter2)
#     # print(xcord1,xcord2,ycord1,ycord2)
#     if distanceCenter1 == True:
#          pygame.draw.circle(screen,"blue",(xcord1,ycord1),5)
#          player1+=1 

#     else:
#          pygame.draw.circle(screen,"green",(xcord1,ycord1),5)
#     if distanceCenter2 == True:
#          pygame.draw.circle(screen,"black",(xcord2,ycord2),5)
#          player2+=1 

#     else:
#          pygame.draw.circle(screen,"yellow",(xcord2,ycord2),5)
#     pygame.display.flip()
# font = pygame.font.Font(None,48)
if player1> player2:
     text = font.render("Player 1 Won",True,"white")
     screen.blit(text, (150,0))
     if play1bet == True:
            text2 = font.render("Your bet was right",True,"white")
            screen.blit(text2,(150,50))
     elif play2bet == True:
            text2 = font.render("Your bet was wrong",True,"white")
            screen.blit(text2,(150,50))
elif player2> player1:
     text = font.render("Player 2 Won",True,"white")
     screen.blit(text, (150, 0))
     if play1bet == True:
            text2 = font.render("Your bet was Wrong",True,"white")
            screen.blit(text2,(150,50))
     elif play2bet == True:
            text2 = font.render("Your bet was Right",True,"white")
            screen.blit(text2,(150,50))
else:
     text = font.render("Player No One Won",True,"white")
     screen.blit(text, (150, 0))

pygame.display.flip()
input()

#functions can access variables in global scope 
#collisions are when u have two variables of the same name 

