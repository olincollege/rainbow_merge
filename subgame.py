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
        self.framerate = 30
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
        self.screen.blit(pygame.image.load("animals/ground.jpg"), board.ground_pos)
        # Draw failure line
        pygame.draw.rect(
            self.screen,
            pygame.Color(255, 0, 0),
            pygame.Rect(0, board.max_height, 500, 1),
        )

    def display_score(self, score, screen):
        """Draws the score on the board."""
        score_font = pygame.font.SysFont("Comic Sans MS", 30)
        text_surface = score_font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(text_surface, (400, 105))
