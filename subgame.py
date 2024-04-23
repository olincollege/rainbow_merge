import random

import sys
import pygame
from pygame.locals import *

# import controller

from board import Board


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

    def pushes(button):
        pass
