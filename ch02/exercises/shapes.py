import pygame
pygame.init()
screen= pygame.display.set_mode()
dimensions = pygame.display.get_window_size()
print (dimensions)
starting_point = [dimensions[0]//2,dimensions[0]//2-200]
# pygame.draw.circle(screen,"red",[500,190],35)
# pygame.draw.circle(screen,"green",[500,260],45)
# pygame.draw.circle(screen,"blue",[500,350],55)
radius = 50 
for _ in range(3):
    pygame.draw.circle(screen,"red",starting_point,radius)
    starting_point[1]=starting_point[1]-radius
    radius = radius //2
    starting_point[1]=starting_point[1]-radius
pygame.display.flip()
input()