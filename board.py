import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self):
        self.ground_pos = (0, 700)
        self.max_height = 279
        self._ground = "animals/ground.jpg"

    @property
    def get_ground(self):
        return self._ground
