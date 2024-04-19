from abc import ABC


class Animal(ABC):
    def __init__(
        self, radius=None, point_value=None, sprite=None, position=None, speed=None
    ):
        self.radius = radius
        self.point_value = point_value
        self.sprite = sprite
        self.position = position
        self.speed = speed

    def disp(self):
        pass


class Giraffe(Animal):

    radius = 25
    point_value = 50
    sprite = "visuals/giraffe.png"
    position = (20, 30)
    speed = 0

    def __init__(self, radius, point_value, sprite, position, speed):
        super().__init__(radius, point_value, sprite, position, speed)
