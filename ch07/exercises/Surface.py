from Rectangle import Rectangle
class Surface:
    """Takes the filename string as a parameter and saves it to 
    the self.image instance variable."""
    def __init__(self,filename,x,y,h,w):
        self.image = filename
        self.rect = Rectangle(x,y,h,w)
    def getRect(self):
        return self.rect