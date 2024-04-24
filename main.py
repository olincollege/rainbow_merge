import sys
import pygame
from pygame.locals import *
<<<<<<< HEAD
import subgame
import controller
=======
from subgame import Subgame
from controller import P1Controller
>>>>>>> 17a13b673e67cd8179e4a11ea7b8307baae516d4


def main():
    pygame.init()

<<<<<<< HEAD
    x = subgame.Subgame()
    y = subgame.moving_animals(
        player_num=1
    )  # Assuming player_num is passed during initialization
    player1 = controller.P1Controller
    animals = pygame.image.load("visuals/bee.jpg")
=======
    subgame = Subgame()
    controller = P1Controller()
>>>>>>> 17a13b673e67cd8179e4a11ea7b8307baae516d4

    while True:

        pygame.display.update()

        # draw background
        subgame.draw_board(subgame.subgame_board)

        # draw all animals

        # check for collisions with other animals

        # move dropped animals

        # move hanging animal

        # refresh window
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
<<<<<<< HEAD
                break

        player1_input = player1.get_user_input
        y.move_animal(player1_input)

        # Draw the game elements
        x.draw_board(x.subgame_board)
        y.draw_moving_animals(x.screen, animals)

        pygame.display.update()
=======
>>>>>>> 17a13b673e67cd8179e4a11ea7b8307baae516d4


main()


"""
while True:
        # pygame management
        clock.tick(60)
        events = pygame.event.get()

        # draw features of level
        game.draw_level_background(board)
        game.draw_board(board)
        if gates:
            game.draw_gates(gates)
        game.draw_doors(doors)

        # draw player
        game.draw_player([magma_boy, hydro_girl])

        # move player
        arrows_controller.control_player(events, magma_boy)
        wasd_controller.control_player(events, hydro_girl)

        game.move_player(board, gates, [magma_boy, hydro_girl])

        # check for player at special location
        game.check_for_death(board, [magma_boy, hydro_girl])

        game.check_for_gate_press(gates, [magma_boy, hydro_girl])

        game.check_for_door_open(fire_door, magma_boy)
        game.check_for_door_open(water_door, hydro_girl)

        # refresh window
        game.refresh_window()

        # special events
        if hydro_girl.is_dead() or magma_boy.is_dead():
            show_death_screen(game, controller, level)

        if game.level_is_done(doors):
            show_win_screen(game, controller)

        if controller.press_key(events, K_ESCAPE):
            show_level_screen(game, controller)

        # close window is player clicks on [x]
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
"""
