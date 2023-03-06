import random 
import turtle 
window = turtle.Screen()
window.screensize(500,500)
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() 
michelangelo.shape('turtle')
michelangelo.speed(0)
michelangelo.up()
michelangelo.goto(250,250)
headsortails = random.randrange(0,2)
distance = 10 
angle = 90 
is_in_screen = True 
colors = ["red","green","blue","purple","red"]
print(headsortails)
def is_in_screen(w,m):
    # michelangelo.forward(distance)
    # turtleX = michelangelo.xcor()
    # turtleY = michelangelo.ycor()
    # x_range = window.window_height()/2
    # y_range = window.window_width() /2 
    # michelangelo.color(random.choice(colors))
    # if abs(turtleX) > x_range or abs(turtleY) > y_range:
    #     is_in_screen = False
    return True
while is_in_screen(window,michelangelo):
    headsortails = random.randrange(0,2)
    if headsortails == 0:
        michelangelo.right(angle)
    else:
        michelangelo.left(angle)

  
window.exitonclick() 

