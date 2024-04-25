import random

import sys
import pygame
from pygame.locals import *

# import controller

from board import Board
from controller import P1Controller
from controller import P2Controller
import math


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
        self.timer = pygame.time.Clock()  #
        self.initialize_board()
        self.draw_board(self.subgame_board)
        self.animal_positions = {
            0: (36, 50),
            1: (86, 50),
            2: (122, 50),
            3: (158, 50),
            4: (194, 50),
            5: (230, 50),
            6: (266, 50),
            7: (302, 50),
            8: (338, 50),
            9: (374, 50),
            10: (410, 50),
        }

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

    def is_touching_ground(self, animal, board):
        """
        Checks if the bottom of an animal, represented as a circle, is touching or below the ground.

        Parameters:
        - animal (object): Animal object with 'position' (x, y coordinates) and 'radius' attributes.

        Returns:
        - bool: True if the animal is touching or below the ground, False otherwise.
        """
        # Extract position and radius from the animal
        y = animal.position[1]
        radius = animal.radius

        # Calculate the y-coordinate of the bottom of the animal
        bottom_of_animal = y + radius

        # Ground level y-coordinate
        ground_level = board.ground_pos[1]

        # Check if the bottom of the animal is touching or below the ground
        if bottom_of_animal >= ground_level:
            return True
        else:
            return False


class moving_animals:
    animal_positions = {
        0: (36, 50),
        1: (86, 50),
        2: (122, 50),
        3: (158, 50),
        4: (194, 50),
        5: (230, 50),
        6: (266, 50),
        7: (302, 50),
        8: (338, 50),
        9: (374, 50),
        10: (410, 50),
    }

    def __init__(self, player_num):
        self.player_num = player_num
        if player_num == 1:
            self.controller = P1Controller()
        elif player_num == 2:
            self.controller = P2Controller()
        self.player_position = 6

    def move_animal(self, player_input):
        if player_input == "right":
            if self.player_position == 10:
                self.player_position = 0
            else:
                self.player_position += 1
        elif player_input == "left":
            if self.player_position == 0:
                self.player_position = 10
            else:
                self.player_position -= 1
        elif player_input == "drop":
            # Logic for dropping something
            pass

    def draw_moving_animals(self, screen, animal):
        pos = self.animal_positions[self.player_position]
        # screen.blit(animal_image, pos)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), pos, 10)
