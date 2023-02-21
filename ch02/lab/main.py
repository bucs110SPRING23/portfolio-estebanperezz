import turtle #1. import modules
import random
import pygame
import math 

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
randmove= random.randrange(1,1000)
michelangelo.forward(randmove)
randmove2= random.randrange(1,1000)
leonardo.forward(randmove2)
michelangelo.goto(-100,20)
leonardo.goto(-100,20)

for _ in range(0,50):
    newrandom1 = random.randrange(1,10)
    newrandom2 = random.randrange(1,10)
    leonardo.forward(newrandom1)
    michelangelo.forward(newrandom2)
window.exitonclick()



# PART B - complete part B here

pygame.init()
window= pygame.display.set_mode()

points = []
numsides = [6,20,100,360]
side_length = 50 
xpos = 400
ypos = 300
for i in range(4):
    window.fill("cyan")
    pygame.display.flip()
    tempside= numsides[i]
    for i in range(tempside):

        angle=360/tempside
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
    pygame.draw.polygon(window,"green",points)
    points = [] 
    pygame.display.flip()
    pygame.time.wait(1000)
window.exitonclick()
