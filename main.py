import sys
import pygame
from pygame.locals import *
from subgame import Subgame
from animals import moving_animals, Block
from controller import P1Controller


def main():
    pygame.init()

    controller = P1Controller()
    y = moving_animals(
        1, controller
    )  # Assuming player_num is passed during initialization

    player1 = P1Controller()
    subgame = Subgame()
    # blocks_list = [[" "] * 8] * 8
    blocks_list = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
    ]
    test_block = Block(800, 800)  # Animal to test class against

    while True:

        # draw background
        subgame.draw_board(subgame.subgame_board)

        # check for collisions with other animals

        # move dropped animals

        # move hanging animal

        # Draw the game elements
        y.draw_moving_animals(subgame.screen)

        for x_p in range(8):
            for y_p in range(8):
                if type(blocks_list[x_p][y_p]) == type(test_block):
                    blocks_list[x_p][y_p].draw(subgame.screen)

        # refresh window
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                player1_input = player1.get_user_input()
                y.move_animal(player1_input, blocks_list)


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
