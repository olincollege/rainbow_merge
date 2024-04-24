import sys
import pygame
from pygame.locals import *
import subgame
import controller


def main():
    pygame.init()

    x = subgame.Subgame()
    y = subgame.moving_animals(
        player_num=1
    )  # Assuming player_num is passed during initialization
    player1 = controller.P1Controller
    animals = pygame.image.load("visuals/bee.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                break

        player1_input = player1.get_user_input
        y.move_animal(player1_input)

        # Draw the game elements
        x.draw_board(x.subgame_board)
        y.draw_moving_animals(x.screen, animals)

        pygame.display.update()


main()
