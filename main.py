import sys
import pygame
from pygame.locals import *
from subgame import Subgame
from animals import MovingAnimal, Block
from controller import P1Controller
import copy


def main():
    pygame.init()

    controller = P1Controller()
    moving_animal = MovingAnimal(
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
    ]  # list containing all instances of blocks and their positions. each list represents an x-position, and each entry in a sublist represents a y-position.
    test_block = Block(800, 800)  # Animal to test class against

    while True:

        # draw background
        subgame.draw_board(subgame.subgame_board)

        # check for collisions with other animals

        # move dropped animals

        # move hanging animal

        # Draw the game elements
        moving_animal.draw_moving_animals(subgame.screen)

        # Handle vertical merges
        while True:
            pre_list = copy.deepcopy(
                blocks_list
            )  # set this to check if any merges occurred
            # check list for Block instances
            broke = False
            for x_p in range(8):
                for y_p in range(8):
                    # if there is a block at any point, perform any applicable merges
                    if isinstance(blocks_list[x_p][y_p], Block):
                        a = blocks_list[x_p][y_p].vertical_merge(x_p, y_p, blocks_list)
                        if a:
                            broke = True  # use this statement to ensure we break out of both for loops
                            break
                if broke is True:  # break out of second for loop
                    break

            structure_changed = False  # variable to check whether any merges occurred
            for x_p in range(8):
                for y_p in range(8):
                    if type(pre_list[x_p][y_p]) != type(
                        blocks_list[x_p][y_p]
                    ):  # have to use type check instead of equality because block ID is not the same every time
                        structure_changed = True

            if structure_changed == False:
                break  # if no merges occurred, we are good to continue on

            print(
                "abc"
            )  # check to see if it the pre_list and post_list are not the same

        # Handle Horizontal Merges
        while True:
            pre_list = copy.deepcopy(
                blocks_list
            )  # set this to check if any merges occurred
            # check list for Block instances
            for x_p in range(8):
                for y_p in range(8):
                    # if there is a block at any point, perform any applicable merges
                    if isinstance(blocks_list[x_p][y_p], Block):
                        b = blocks_list[x_p][y_p].horizontal_merge(
                            x_p, y_p, blocks_list
                        )
                        if b:
                            broke = True  # use this statement to ensure we break out of both for loops
                            break
                if broke is True:  # break out of second for loop
                    break

            structure_changed = False  # variable to check whether any merges occurred
            for x_p in range(8):
                for y_p in range(8):
                    if type(pre_list[x_p][y_p]) != type(
                        blocks_list[x_p][y_p]
                    ):  # have to use type check instead of equality because block ID is not the same every time
                        structure_changed = True

            if structure_changed == False:
                break  # if no merges occurred, we are good to continue on
            print("horiz")

        # draw elements
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
                moving_animal.move_animal(player1_input, blocks_list)


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
