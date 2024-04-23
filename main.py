import sys
import pygame
from pygame.locals import *
import subgame


def main():
    pygame.init()

    x = subgame.Subgame()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break
        pygame.display.update()
        x.draw_board(x.subgame_board)


main()
