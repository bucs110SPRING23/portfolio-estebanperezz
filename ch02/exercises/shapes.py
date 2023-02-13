import pygame
pygame.init()
screen= pygame.display.set_mode()
pygame.draw.circle(screen,"red",[200,190],30)
pygame.draw.circle(screen,"green",[200,260],40)
pygame.draw.circle(screen,"blue",[200,350],50)
pygame.display.flip()
input()