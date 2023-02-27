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
pygame.draw.circle(screen, color ="red",center=center,radius= center[0])
# pygame.draw.circle(screen, color ="black",center=(randomnx,randomy),radius=3)
pygame.draw.line(screen,color="blue",start_pos=(0,250), end_pos=[500,250])
pygame.draw.line(screen,color="blue",start_pos=(250,0),end_pos=(250,500)) 

pygame.display.flip()
for _ in range(10):
    randomnx = random.randrange(1,screen_size[0])
    randomy = random.randrange(1,screen_size[1])
    distance_from_center = math.hypot(randomnx -center[0],randomy- center[1]) 
    is_in_cirlce = (distance_from_center <=center[0])
    if is_in_cirlce == True:
         pygame.draw.circle(screen,"green",(randomnx,randomy),3)

    else:
         pygame.draw.circle(screen,"blue",(randomnx,randomy),3)
    pygame.display.flip()
input()

