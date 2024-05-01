import sys
import pygame
from pygame.locals import *
from rainbow_merge_view import View
from rainbow_merge_block import MovingBlock, Block
from rainbow_merge_controller import P1Controller
import copy


def check_structure_changed(pre_list, blocks_list):
    """
    Check if the structure of the game board has changed after merges or falls.

    Args:
        pre_list (list): The previous state of the game board.
        blocks_list (list): The current state of the game board.

    Returns:
        bool: True if the structure has changed, False otherwise.
    """
    # Check if structure has changed after merges or falls
    for x_p in range(8):
        for y_p in range(8):
            if type(pre_list[x_p][y_p]) != type(blocks_list[x_p][y_p]):
                return True
    return False


def handle_merges(blocks_list, merge_function):
    """
    Handle merges of blocks on the game board.

    Args:
        blocks_list (list): The current state of the game board.
        merge_function (function): The merge function to apply.

    Returns:
        Block or None: The merged Block object if a merge occurred, None otherwise.
    """
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
    """
    Handle falls of blocks on the game board.

    Args:
        blocks_list (list): The current state of the game board.

    Returns:
        Block or None: The fallen Block object if a fall occurred, None otherwise.
    """
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
    """
    Check if the first column of the game board contains any blocks.

    Args:
        blocks_list (list): The current state of the game board.

    Returns:
        bool: True if the first column contains blocks, False otherwise.
    """
    for row in blocks_list:
        if isinstance(row[0], Block):
            return True
    return False


def check_for_black(blocks_list):
    """
    Check if a black block exists on the game board.

    Args:
        blocks_list (list): The current state of the game board.

    Returns:
        bool: True if a black block exists, False otherwise.
    """
    for row in blocks_list:
        for block in row:
            if isinstance(block, Block) and block.color == (7, 13, 13):
                return True
    return False


def win_screen(screen, score):
    """
    Display the win screen with the final score.

    Args:
        screen (pygame.Surface): The game screen.
        score (int): The final score.
    """
    font = pygame.font.SysFont(None, 48)
    text = font.render("You Win!", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    click_text = font.render("Click any key to restart!", True, (255, 0, 0, 0))

    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 200))
    screen.blit(
        score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 300)
    )
    screen.blit(
        click_text, (screen.get_width() // 2 - click_text.get_width() // 2, 400)
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


def game_over_screen(screen, score):
    """
    Display the game over screen with the final score.

    Args:
        screen (pygame.Surface): The game screen.
        score (int): The final score.
    """
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
    click_text = font.render("Click any key to restart!", True, (255, 0, 0, 0))

    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 200))
    screen.blit(
        score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 300)
    )
    screen.blit(
        click_text, (screen.get_width() // 2 - click_text.get_width() // 2, 400)
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
    """
    Runs Rainbow Merge Game
    """
    pygame.init()
    pygame.font.init()

    controller = P1Controller()
    moving_block = MovingBlock(1, controller)
    player1 = P1Controller()
    view = View()
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
    black_block_created = False  # Flag to track if a black block has been created

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                player1_input = player1.get_user_input()
                moving_block.move_block(player1_input, blocks_list)
                black_block_created = check_for_black(blocks_list)
                if black_block_created:
                    game_over = True
                    if game_over == True:
                        win_screen(view.screen, score)
                first_row_has_elements = check_first_column(blocks_list)
                if first_row_has_elements:
                    game_over = True
                    if game_over == True:
                        game_over_screen(view.screen, score)

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

        view.draw_board(view.view_board)
        view.display_score(score, view.screen)
        moving_block.draw_moving_blocks(view.screen)
        for x_p in range(8):
            for y_p in range(8):
                if isinstance(blocks_list[x_p][y_p], Block):
                    blocks_list[x_p][y_p].draw(view.screen)

        pygame.display.update()
        view.screen.fill(view.background_color)

        clock.tick(60)


if __name__ == "__main__":
    main()
