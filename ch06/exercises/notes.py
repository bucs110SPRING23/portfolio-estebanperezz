#mananging complexies
#Unix - SLOC (1,000 ) Source Lines of Code
#Chrome - 10,000,000 SLOC 
#Windows has 100 million
##Complex Objects 
##Primtive: int, str, float, lists, dict, tuple 
## turtle:x(int),y,heading, color(color), pensize(int), shape(str)
#bundle data anf functions together 
#bundle data and functions together 
#state :current value of the data of the data in the object
#Behavior - the function that operate on the data in the object 
#point - object should do one thing 
#state:x, y color 
#behavior:change color,move 
#classes = type 
import turtle
print(type(turtle.Turtle()))
#classes are blueprints for objects
#fcts are stored algos, class as a stored data type
#classes are not exectable 
#don't put executables in global scope
#point class
#instance : object created from a specefic class
# t - turtle.Turtle() t is an instance of turtle 
# instance variable: an internal variable that is part of the instance 
# t,x,t.pos # x and pos are instance variables 
# interface: the functions and variables of an object 
# t.forward() part of the interface 
# point - make it a class ourselves
#class are named with TitleCase
import random,pygame
import point
from pygame import rect
def mainloop(display):
    points = []
    while True:
        for event in pygame.get():
            point_deleted = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for p in points:
                    if p.rect.collidepoint(event.center):
                        del p 
                        point_deleted = True 
                if not point_deleted:
                    p = point.Point(*event.pos)
                    points.append(p)
                    

            
        display.fill("white")
        for p in points:
            pygame.draw.circle(display,p.color,p.rect.center,p.rect/2)
        pygame.display.flip()
    
p1= point.Point() 
p1.x = 10 
p2 = point.Point()
p2.y = 5 
p1.color = "red"
points= []
for p in range(10):
    x = random.randint(0,100)
    y = random.randint(0,200)
    points.append(point.Point(x,y,"orange"))
t = turtle.Turtle()
for p in points:
    t.color(p.color)
    t.goto((p.x,p.y))

##MVC - Module View Controller - for gui projects - accumulator pattern 
##for GUI Programs - like the accumulator pattern - design patterns 
#Design patterns - language independent 
##View - displays things on the screen - pygame --turtle 
##Model is usually a class and contains data for the program 
def main():

    pygame.init()
    display = pygame.display.set_mode()
main()
p1 = point.LED(x=100,y=100)
pygame.draw.circle(display,p1.color,(p1.rect.x,p1.rect.y),p1.radius)
while True:
    pygame.display.flip()