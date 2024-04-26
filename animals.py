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
        self.state = "hanging"
        self.color = pygame.Color(255, 0, 0)

        # The physics components
        self.body = pymunk.Body(mass=1, moment=pymunk.moment_for_circle(1, 0, radius))
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.friction = 0.5
        self.shape.elasticity = 0.8
        self.position = int(position[0]), int(position[1])
        self.body.position = self.position

    def draw(self, window):
        # Function to create the sprite from this abstract animal class
        sprite_x, sprite_y = int(self.body.position.x), int(self.body.position.y)
        window.draw_lr(self.sprite, sprite_x, sprite_y, 0)

    def update_speed


# Make sure that the 'animals' folder is in the same directory as this file and contains the .png files for each animal.


class bee(Animal):

    radius = 25
    point_value = 5
    sprite = "animals/bee.jpg"
    position = (20, 30)
    speed = 0

    def __init__(self, radius, point_value, sprite, position, speed):
        super().__init__(radius, point_value, sprite, position, speed)


class chick(Animal):
    def __init__(self):
        super().__init__(
            radius=30,
            point_value=10,
            sprite="animals/chick.jpg",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class lizard(Animal):
    def __init__(self):
        super().__init__(
            radius=35,
            point_value=20,
            sprite="animals/lizard.jpg",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class sloth(Animal):
    def __init__(self):
        super().__init__(
            radius=40,
            point_value=40,
            sprite="animals/sloth.jpg",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class penguin(Animal):
    def __init__(self):
        super().__init__(
            radius=45,
            point_value=80,
            sprite="animals/penguin.jpg",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )


class pig(Animal):
    def __init__(self):
        super().__init__(
            radius=50,
            point_value=160,
            sprite="animals/sloth.jpg",
            position=(0, 0),
            speed=1,
            accel=0.1,
        )
