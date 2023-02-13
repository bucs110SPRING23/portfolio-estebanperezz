import turtle 

sides = int(input("Enter the number of sides"))
length = int(input("Enter the number of sides"))
pen = turtle.Turtle() 
pen.color("Orange")
window = turtle.Screen()
for s in sides:
    print(s)
    pen.forward(length)
    pen.right(360/sides)
window.exitonclick() 
