import random

import sys
import pygame
from pygame.locals import *

# import controller

from board import Board
import math
import animals


class Subgame:
    # this function is to define the characters of the screen of one player
    def __init__(self):
        self.dimensions = (500, 800)
        self.background_color = pygame.Color(227, 216, 152)
        self.subgame_board = Board()
        self.score = 0
        self.framerate = 30
        self.can_use_superpower = False
        self.drop_speed = 0.5  # drops per second
        self.current_animal = random.randrange(3) + 1  # random animal 1-4
        self.next_animal = random.randrange(3) + 1  # random animal 1-4
        self.timer = pygame.time.Clock()  #
        self.initialize_board()
        self.draw_board(self.subgame_board)

    def initialize_board(self):
        """Creates a blank screen on which the board is drawn."""
        # Draw blank board
        self.screen = pygame.display.set_mode(self.dimensions)
        self.screen.fill(self.background_color)
        pygame.display.set_caption("Animal Merger")

    def draw_board(self, board):
        """Draws the board."""
        # Draw ground
        self.screen.blit(pygame.image.load("visuals/ground.jpg"), board.ground_pos)
        # Draw failure line
        pygame.draw.rect(
            self.screen,
            pygame.Color(255, 0, 0),
            pygame.Rect(0, board.max_height, 500, 1),
        )

    def end_subgame(self):
        pass

    def pushes(self, button):
        pass

    def is_touching_animal(self, animal1, animal2):
        """
        Determines whether two animals, represented as circles, are touching or overlapping.

        Each animal is expected to have a 'position' attribute and a 'radius' attribute.
        The 'position' attribute should be a tuple representing the (x, y) coordinates of the animal's center.
        The 'radius' attribute should be a number representing the radius of the circle that outlines the animal.

        Parameters:
        - animal1 (object): The first animal object with attributes 'position' and 'radius'.
        - animal2 (object): The second animal object with attributes 'position' and 'radius'.

        Returns:
        - bool: True if the animals are touching or overlapping, otherwise False.
        """
        # Extract position and radius from both animals
        x1 = animal1.position[0]
        y1 = animal1.position[1]
        r1 = animal1.radius
        x2 = animal2.position[0]
        y2 = animal2.position[1]
        r2 = animal2.radius

        # Calculate the distance between the centers of the two animals
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # Calculate the sum of the radii
        radius_sum = r1 + r2

        # Check for collision
        if distance <= radius_sum:
            return True
        else:
            return False
