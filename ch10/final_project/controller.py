import pygame
def mainloop(self):
    """is the main loop that is going to run the program"""
    while (True): #this can also be a variable instead of just True 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.flip()
            