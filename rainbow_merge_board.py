import sys
import pygame
from pygame.locals import *


class Board:
    """
    Represents the game board in the game.
    """

    def __init__(self):
        """
        Initialize the Board object.
        """
        self.ground_pos = (0, 700)
        self.max_height = 279
        self._ground = "visuals/ground.jpg"

    @property
    def get_ground(self):
        """
        Get the path to the ground image.

        Returns:
            str: Path to the ground image.
        """
        return self._ground
