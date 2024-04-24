import random

import sys
import pygame
from pygame.locals import *

# import controller

from board import Board
from controller import P1Controller
from controller import P2Controller


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

    def pushes(button):
        pass


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

    def draw_moving_animals(self, screen, animal_image):
        pos = self.animal_positions[self.player_position]
        screen.blit(animal_image, pos)
