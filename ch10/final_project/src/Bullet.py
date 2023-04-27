
class Bullet:
    def __init__(self, x, y):
        """
        Initializes the bullet object
        args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
        """
        self.x = x
        self.y = y

    def move(self):
        """
        moves the bullet object up by a random ammount when close to player.

        args: none
        return: random int between 0 and player height 
        """
        # implementation for move
