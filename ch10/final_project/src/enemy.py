class Enemy:
    def __init__(self, x, y, img_file):
        """
        Initializes the enemy object
        args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
        """
        self.x = x
        self.y = y
        self.img_file = img_file
        self.health = 100
        self.speed = 2

    def move_right(self):
        """
        moves position right by the enemy's speed
        args: None
        return: None
        """
        self.x += self.speed

    def move_left(self):
        """
        moves position left by the enemy's speed
        args: None
        return: None
        """
        self.x -= self.speed

    def jump(self):
        """
        makes the enemy jump
        args: None
        return: None
        """
        # implementation for jump

    def attack(self, player):
        """
        attacks the player
        args:
            - player : Player - the player object to attack
        return: None
        """
        player.health -= 10

    def take_damage(self, damage):
        """
        reduces the enemy's health by the given amount
        args:
            - damage : int - the amount of damage to take
        return: None
        """
        self.health -= damage

    def is_dead(self):
        """
        checks if the enemy is dead
        args: None
        return: bool - True if the enemy is dead, False otherwise
        """
        return self.health <= 0
