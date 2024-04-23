import pygame
from abc import ABC


class Animal(ABC):
    def __init__(
        self,
        radius=None,
        point_value=None,
        sprite=None,
        position=None,
        speed=None,
        accel=None,
    ):
        self.radius = radius
        self.point_value = point_value
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.position = position
        self.speed = speed
        self.accel = accel


# Folder for visuals (.png files)
# Ensure that the 'animals' folder is in the same directory as this file and contains the .png files for each animal.


class Animal1(Animal):

    radius = 25
    point_value = 5
    sprite = "visuals/lizard.jpg"
    position = (20, 30)
    speed = 0

    def __init__(self, radius, point_value, sprite, position, speed):
        super().__init__(radius, point_value, sprite, position, speed)


class Animal2(Animal):
    def __init__(self):
        super().__init__(
            radius=30,
            point_value=10,
            sprite="animals/animal2.png",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class Animal3(Animal):
    def __init__(self):
        super().__init__(
            radius=35,
            point_value=20,
            sprite="animals/animal3.png",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class Animal4(Animal):
    def __init__(self):
        super().__init__(
            radius=40,
            point_value=40,
            sprite="animals/animal4.png",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class Animal5(Animal):
    def __init__(self):
        super().__init__(
            radius=45,
            point_value=80,
            sprite="animals/animal5.png",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class Animal6(Animal):
    def __init__(self):
        super().__init__(
            radius=50,
            point_value=160,
            sprite="animals/animal6.png",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )
