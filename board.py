import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self):
        self.ground_pos = (0, 700)
        self.max_height = 100
        self._ground = "visuals/ground.jpg"

    @property
    def get_ground(self):
        return self._ground

    # def disp(self):  # do we need this? i dont think we do
    #     screen = pygame.display.set_mode((500,800))
    #     screen.fill(background_color)
    #     pygame.display.set_caption("Animal Merger")
    #     ground_surface = pygame.image.load("visuals/animals.jpg")
