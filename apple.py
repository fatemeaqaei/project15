import arcade
import random

class Pear(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__("pear.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

class Apple(arcade.Sprite):
    def __init__ (self,width,height):
        super().__init__("Apple.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

class Rock(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__("bomb.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

