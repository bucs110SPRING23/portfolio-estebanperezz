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
class Point:
    #usually classes go in their own file, one class per file 
    def __init__(self):
        self.x = 0 
        self.y  =0  
        self.color = ""
        pass 
import point
p1= point.Point() 
p1.x = 10 
p2 = point.Point()
p2.y = 5 
p1.color = "red"