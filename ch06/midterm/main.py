import turtle 
import random
def smallerpoly(poly,numpoly,sizeofpoly):
    '''
    draws a specified number of stars which each 
    star being smaller than the last one 
    '''
    numpoly = 10 
    sizeofpoly = 200
    tranform= (15,-20)
    poly.penup()
    poly.goto((-150,150))
    for _ in range(numpoly):
         sizeofpoly = sizeofpoly-30 
         if sizeofpoly > 0:
            poly.penup()
            poly.goto(poly.pos()+tranform)
            poly.pendown()
            createturtle(sizeofpoly,poly)
def setangle(sides):
    '''
    Specifies the angle of shape with a given number of sides
    '''
    angle = 360 /sides
    return angle     
def createturtle(sizebigstar,star):
    '''
    Creates a polygon object and sets a random color to it 
    '''
    colors = ["red","green","blue","purple","yellow","grey","orange","pink"]
    sides = 5 
    angle = setangle(sides)
    for _ in range(sides):
        star.forward(sizebigstar)
        star.pencolor(random.choice(colors))
        star.right(angle)
def main():    
    polygon = turtle.Turtle()
    smallerpoly(polygon,numpoly = 10,sizeofpoly = 200)
    turtle.done()
main()