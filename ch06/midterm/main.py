import turtle 
import random
def smallerstars(numstars,sizebigstar,star):
    for _ in range(numstars):
         #NEXT STAR WILL BE SMALLER 
         sizebigstar = sizebigstar-30 
         if sizebigstar > 0:
            star.penup()
            star.goto(star.pos()+(15,-20))
            star.pendown()
            createturtle(sizebigstar,star)
def setangle(sides):
    angle = 360 /sides
    return angle     
def createturtle(sizebigstar,star):
    colors = ["red","green","blue","purple","yellow","grey","orange","pink"]
    sides = 5 
    angle = setangle(sides)
    for _ in range(sides):
        star.forward(sizebigstar)
        star.pencolor(random.choice(colors))
        star.right(angle)
def main():    
    star = turtle.Turtle()
    star.penup()
    star.goto((-150,150))
    numstar = 10 
    sizeofpolygon = 200
    smallerstars(numstar,sizeofpolygon,star)
    turtle.done()
main()