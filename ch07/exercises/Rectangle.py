import random
class Rectangle:
    def __init__(self,x,y,h,w):

        """A Class to be a rectangle object
    x:int --> Cordinates 
    y: int --> Cordinates starting at upper left
     h: int height of the rectangle 
      w:int: the width of the rectangle  """
        self.x = abs(x)
        self.y = abs(y)
        self.h =abs(h)
        self.w = abs(w)
    def __str__(self):
        """Returns a string x,y,width, height """
        return f"(x:{self.x},y:{self.y}), width:{self.width}, height:{self.height} "
        