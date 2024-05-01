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


def check_first_column(blocks_list):
    for row in blocks_list:
        if isinstance(row[0], Block):
            return True
    return False


def game_over_screen(screen, score):
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))

    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 200))
    screen.blit(
        score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 300)
    )

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                main()  # Restart the game if any mouse button is clicked

        pygame.time.wait(100)  # Add a small delay to prevent high CPU usage


def main():
    pygame.init()
    pygame.font.init()

    controller = P1Controller()
    moving_animal = MovingAnimal(1, controller)
    player1 = P1Controller()
    subgame = Subgame()
    clock = pygame.time.Clock()

    blocks_list = [
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
    ]

    color_names = {
        (181, 3, 3): "Red",
        (229, 90, 16): "Orange",
        (249, 163, 57): "Light Orange",
        (250, 228, 106): "Yellow",
        (144, 190, 109): "Green",
        (67, 170, 139): "Green Blue",
        (87, 117, 144): "Grey Blue",
        (39, 125, 161): "Blue",
        (131, 88, 187): "Purple",
        (7, 13, 13): "Black",
    }
    color_scores = {
        "Red": 2,
        "Orange": 4,
        "Light Orange": 8,
        "Yellow": 16,
        "Green": 32,
        "Green Blue": 64,
        "Grey Blue": 128,
        "Blue": 256,
        "Purple": 512,
        "Black": 1024,
    }
    score = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                player1_input = player1.get_user_input()
                moving_animal.move_animal(player1_input, blocks_list)
                first_row_has_elements = check_first_column(blocks_list)
                if first_row_has_elements:
                    game_over = True

        merged_block = handle_merges(
            blocks_list,
            lambda x, y, blocks_list: blocks_list[x][y].horizontal_merge(
                x, y, blocks_list
            ),
        )
        if isinstance(merged_block, Block):
            score += color_scores.get(color_names.get(merged_block.color), 0)
            print(color_scores.get(color_names.get(merged_block.color), 0))

        # Handle vertical merges
        merged_block = handle_merges(
            blocks_list,
            lambda x, y, blocks_list: blocks_list[x][y].vertical_merge(
                x, y, blocks_list
            ),
        )
        if isinstance(merged_block, Block):
            score += color_scores.get(color_names.get(merged_block.color), 0)
            print(color_scores.get(color_names.get(merged_block.color), 0))

        fallen_block = handle_falls(blocks_list)
        if isinstance(fallen_block, Block):
            score += color_scores.get(color_names.get(fallen_block.color), 0)
            print(color_scores.get(color_names.get(fallen_block.color), 0))

        subgame.draw_board(subgame.subgame_board)
        subgame.display_score(score, subgame.screen)
        moving_animal.draw_moving_animals(subgame.screen)
        for x_p in range(8):
            for y_p in range(8):
                if isinstance(blocks_list[x_p][y_p], Block):
                    blocks_list[x_p][y_p].draw(subgame.screen)

        pygame.display.update()
        subgame.screen.fill(subgame.background_color)

        clock.tick(60)

    game_over_screen(subgame.screen, score)


main()
