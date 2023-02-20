import random 
x = 'a'
if x < 'y':
    print("yup")
elif x < 'm':
    print("more yup")
## events 
## operating systems habdles events 
## your program ----> OS: anything happening
##connect actions to algos
# ##connections actions to algos 
# ##simon says 
import pygame 
import random 
pygame.init() 
screen = pygame.display.set_mode()
colors = ["red","green","blue","yellow"]
usersequence = [] 
random.shuffle(colors)
for color in colors:
    screen.fill(color)
    pygame.display.flip() 
    pygame.time.wait(1000)
    screen.fill("black")
    pygame.time.wait(250)
message ="""
        Simon Says
        UP:RED
        DOWN:BLUE
        LEFT: GREEN
        RIGHT:YELLOW
        Click on the window, enter sequence, m then press enter"""
response = input(message)
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        
        if event.type==pygame.KEYUP:
            screen.fill("yellow")
            usersequence.append(color)
        if event.key==pygame.K_UP:
            screen.fill("blue")
            usersequence.append(color)
        elif event.key==pygame.K_LEFT:
            usersequence.append(color)
            screen.fill("red")
        elif event.key==pygame.K_RIGHT:
            usersequence.append(color)
            screen.fill("green")
        