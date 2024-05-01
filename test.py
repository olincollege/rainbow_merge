import sys
import pygame
from pygame.locals import *
from subgame import Subgame
from animals import MovingAnimal, Block
from controller import P1Controller
import copy


def check_structure_changed(pre_list, blocks_list):
    # Check if structure has changed after merges or falls
    for x_p in range(8):
        for y_p in range(8):
            if type(pre_list[x_p][y_p]) != type(blocks_list[x_p][y_p]):
                return True
    return False


def handle_merges(blocks_list, merge_function):
    while True:
        pre_list = copy.deepcopy(blocks_list)
        for x_p in range(8):
            for y_p in range(8):
                if isinstance(blocks_list[x_p][y_p], Block):
                    if merge_function(x_p, y_p, blocks_list):
                        return blocks_list[x_p][y_p]  # Return the merged Block object

        if not check_structure_changed(pre_list, blocks_list):
            break  # No merges occurred, exit loop
    return None  # No merge with Block object, return None


def handle_falls(blocks_list):
    while True:
        pre_list = copy.deepcopy(blocks_list)
        for x_p in range(8):
            for y_p in range(8):
                if isinstance(blocks_list[x_p][y_p], Block):
                    if blocks_list[x_p][y_p].fall(x_p, y_p, blocks_list):
                        return blocks_list[x_p][y_p]  # Return the fallen Block object

        if not check_structure_changed(pre_list, blocks_list):
            break  # No falls occurred, exit loop
    return None  # No fall with Block object, return None


def main():
    pygame.init()
    pygame.font.init()

    controller = P1Controller()
    moving_animal = MovingAnimal(
        1, controller
    )  # Assuming player_num is passed during initialization
    player1 = P1Controller()
    subgame = Subgame()
    clock = pygame.time.Clock()

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

    color_names = {
        # B50303
        (181, 3, 3): "Dark Red",
        # F26418
        (242, 100, 24): "Orange",
        # F89012
        (248, 144, 18): "Light Orange",
        # F9C74F
        (249, 199, 79): "Yellow",
        # 90BE6D
        (144, 190, 109): "Light Green",
        # 43AA8B
        (67, 170, 139): "Green",
        # 4D908E
        (77, 144, 142): "Green Blue",
        # 577590
        (87, 117, 144): "Blue",
        # 277DA1
        (39, 125, 161): "Dark Blue",
        # 8358BB
        (131, 88, 187): "Purple",
    }
    color_scores = {
        # B50303
        "Dark Red": 1,
        # F26418
        "Orange": 2,
        # F89012
        "Light Orange": 3,
        # F9C74F
        "Yellow": 4,
        # 90BE6D
        "Light Green": 5,
        # 43AA8B
        "Green": 6,
        # 4D908E
        "Green Blue": 7,
        # 577590
        "Blue": 8,
        # 277DA1
        "Dark Blue": 9,
        # 8358BB
        "Purple": 10,
    }
    score = 0  # initialize score
    while True:
        # Handle game events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                player1_input = player1.get_user_input()
                moving_animal.move_animal(player1_input, blocks_list)

        # Handle vertical merges
        merged_block = handle_merges(
            blocks_list,
            lambda x, y, blocks_list: blocks_list[x][y].vertical_merge(
                x, y, blocks_list
            ),
        )
        if isinstance(merged_block, Block):
            score += color_scores.get(
                color_names.get(merged_block.color), 0
            )  # Increment score based on merged block's color

        # Handle horizontal merges
        merged_block = handle_merges(
            blocks_list,
            lambda x, y, blocks_list: blocks_list[x][y].horizontal_merge(
                x, y, blocks_list
            ),
        )
        if isinstance(merged_block, Block):
            score += color_scores.get(
                color_names.get(merged_block.color), 0
            )  # Increment score based on merged block's color

        # Handle falls
        fallen_block = handle_falls(blocks_list)
        if isinstance(fallen_block, Block):
            score += color_scores.get(
                color_names.get(merged_block.color), 0
            )  # Increment score based on merged block's color

        # draw game elements
        subgame.draw_board(subgame.subgame_board)
        subgame.display_score(score, subgame.screen)
        moving_animal.draw_moving_animals(subgame.screen)  # hanging block
        for x_p in range(8):
            for y_p in range(8):
                if type(blocks_list[x_p][y_p]) == type(test_block):
                    blocks_list[x_p][y_p].draw(
                        subgame.screen
                    )  # draw every dropped block

        # refresh window
        pygame.display.update()
        subgame.screen.fill(subgame.background_color)

        # limit the framerate
        clock.tick(60)


main()
