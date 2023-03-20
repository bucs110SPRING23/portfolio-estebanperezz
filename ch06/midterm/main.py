import turtle 
import random
def smallerstars(numstars,sizebigstar):
    for _ in range(numstars):
         sizebigstar = sizebigstar-30 
         if sizebigstar > 0:
            star.penup()
            star.goto(star.pos()+(15,-20))
            star.pendown()
            createturtle(sizebigstar)
def setangle(sides):
    angle = 360 /sides
    return angle     
def createturtle(sizebigstar):
    colors = ["red","green","blue","purple","yellow","grey","orange","pink"]
    sides = 5 
    angle = setangle(sides)
    for _ in range(sides):
        
        star.forward(sizebigstar)
        star.pencolor(random.choice(colors))
        star.right(angle)
    
star = turtle.Turtle()
star.penup()
star.goto((-150,150))
smallerstars(10,200)
turtle.done()