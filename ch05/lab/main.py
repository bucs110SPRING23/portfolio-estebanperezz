import pygame
import time
def threenp1(n):
    count = 0 
    while n > 1.0:
       count = count +1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count
def threenp1range(upper_limit):
  objs_in_sequence = {}
  
  for _ in range(2,upper_limit+1):
        iter = threenp1(_)
        objs_in_sequence[_] = iter
  return objs_in_sequence
def graph_cordinates(threenplus1_iters_dict,screen):
   cordinates = []
   max_so_far = 0 
   transform = 15 
   print(screen)
   for key,value in threenplus1_iters_dict.items():
        cordinates.append((key*transform,value*transform))
        
        if value > max_so_far:
           max_so_far = value
        if len(cordinates)>=2:
           pygame.draw.line(screen, (0, 255, 0), cordinates[-2], cordinates[-1], 2)
           
          
           
           
   pygame.display.update()
   return max_so_far
   
   
def initscreen():
   pygame.init() 
   
   width = 500
   height = 400
   screen= pygame.display.set_mode((width,height))
   screen.fill((255,255,255))
   pygame.display.flip()
   print (screen)
   return screen
def main(): 
   screen = initscreen()
   while True:
        graph_cordinates(threenp1range(20),screen)
        for event in pygame.event.get():
           if event.type==pygame.quit():
                pygame.quit()
                return
        time.sleep(0.1) 
pygame.quit()


main()

      
        
