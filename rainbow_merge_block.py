import pygame
from abc import ABC
import random
from rainbow_merge_board import Board


class Block:
    def __init__(self, x_position, y_position, n=0):
        """
        Initialize a Block instance with specified color index, and x and y positions.

        Args:
            x_position (int): The x-coordinate where the block will be placed on the screen.
            y_position (int): The y-coordinate where the block will be placed on the screen.
            n (int): The color index, used to determine the block's color from a predefined list.
        """
        self.colors = [
            # B50303
            (181, 3, 3),
            # E55A10
            (229, 90, 16),
            # F9A339
            (249, 163, 57),
            # FAE46A
            (250, 228, 106),
            # 90BE6D
            (144, 190, 109),
            # 43AA8B
            (67, 170, 139),
            # 577590
            (87, 117, 144),
            # 277DA1
            (39, 125, 161),
            # 8358BB
            (131, 88, 187),
            # 070D0D
            (7, 13, 13),
        ]
        self.n = n
        self.color = self.colors[self.n % 16]
        self.possible_x_positions = [10, 70, 130, 190, 250, 310, 370, 430]
        self.possible_y_positions = [220, 280, 340, 400, 460, 520, 580, 640]
        self.x_position = x_position
        self.y_position = y_position

    def get_color(self):
        """
        Get the current color of the block.

        Returns:
            tuple: The RGB tuple representing the color of the block.
        """
        return self.color

    def draw(self, screen):
        """
        Draw the block on a specified Pygame screen as a 60x60 pixel rectangle.

        Args:
            screen: The Pygame display surface to draw the block on.
        """
        pygame.draw.rect(
            screen, self.color, pygame.Rect(self.x_position, self.y_position, 60, 60)
        )

    def vertical_merge(
        self,
        x_position,
        y_position,
        blocks_list,
    ):
        """
        Merge the current block with the one below it if conditions are met.

        Args:
            x_position (int): The x-coordinate of the current block.
            y_position (int): The y-coordinate of the current block.
            blocks_list (list): 2D list representing the grid of blocks.
        Returns:
            True if the blocks are the same color and vertically merged together,
            False if the blocks are not the same color
        """
        # vertical merges
        if y_position < 7:
            # check if there is a block below the current one
            if isinstance(blocks_list[x_position][y_position], Block) and isinstance(
                blocks_list[x_position][y_position + 1], Block
            ):
                # merge if the blocks are the same color
                if blocks_list[x_position][y_position + 1].n == self.n:
                    # kill current block
                    blocks_list[x_position][y_position] = " "
                    # update merged block
                    blocks_list[x_position][y_position + 1] = Block(
                        self.possible_x_positions[x_position],
                        self.possible_y_positions[y_position + 1],
                        n=self.n + 1,
                    )
                    # kill current block again (to ensure no weird things happened during merge)
                    blocks_list[x_position][y_position] = " "
                    return True
        return False

    def fall(
        self,
        x_position,
        y_position,
        blocks_list,
    ):
        """
        Makes the block fall to the next available space directly below it, if possible.

        Args:
            x_position (int): The x-coordinate index of the block in the grid.
            y_position (int): The y-coordinate index of the block in the grid.
            blocks_list (list of lists): 2D list representing the grid of blocks.

        Returns:
            bool: True if the block was able to fall, False otherwise.
        """

        # vertical merges
        if y_position < 7:
            # check if there is a block below the current one
            if isinstance(blocks_list[x_position][y_position], Block) and isinstance(
                blocks_list[x_position][y_position + 1], str
            ):
                blocks_list[x_position][y_position] = " "
                # update merged block
                blocks_list[x_position][y_position + 1] = Block(
                    self.possible_x_positions[x_position],
                    self.possible_y_positions[y_position + 1],
                    n=self.n,
                )
                # kill current block again (to ensure no weird things happened during merge)
                blocks_list[x_position][y_position] = " "
                return True
        return False

    def horizontal_merge(
        self,
        x_position,
        y_position,
        blocks_list,
    ):
        """
        Merge the current block with the one on its right if conditions are met.

        Args:
            x_position (int): The x-coordinate of the current block.
            y_position (int): The y-coordinate of the current block.
            blocks_list (list): 2D list representing the grid of blocks.
        Returns:
            True if the blocks are the same color and horizontally merged together,
            False if the blocks are not the same color
        """
        if x_position < 7:
            # check if there is a block on the right side of the current one
            if isinstance(blocks_list[x_position][y_position], Block) and isinstance(
                blocks_list[x_position + 1][y_position], Block
            ):
                if blocks_list[x_position + 1][y_position].n == self.n:
                    # kill current block
                    blocks_list[x_position + 1][y_position] = " "
                    # upgrade merged block
                    blocks_list[x_position][y_position] = Block(
                        self.possible_x_positions[x_position],
                        self.possible_y_positions[y_position],
                        n=self.n + 1,
                    )
                    # kill current block again (to ensure no weird things happened during merge)
                    blocks_list[x_position + 1][y_position] = " "
                    return True
        return False


class MovingBlock:
    def __init__(self, player_num, controller):
        """
        Initializes a MovingAnimal instance, which represents a player-controlled element that can drop blocks onto a grid.

        Args:
            player_num (int): The number identifying the player. This number determines certain behaviors like controller setup.
            controller: The input mechanism associated with the player. This can be a keyboard, gamepad, etc., specific to player one.
        """
        self.colors = [
            # B50303
            (181, 3, 3),
            # E55A10
            (229, 90, 16),
            # F9A339
            (249, 163, 57),
            # FAE46A
            (250, 228, 106),
            # 90BE6D
            (144, 190, 109),
            # 43AA8B
            (67, 170, 139),
            # 577590
            (87, 117, 144),
            # 277DA1
            (39, 125, 161),
            # 8358BB
            (131, 88, 187),
            # 070D0D
            (7, 13, 13),
        ]
        self.n = random.randrange(4)
        self.possible_x_positions = [10, 70, 130, 190, 250, 310, 370, 430]
        self.possible_y_positions = [220, 280, 340, 400, 460, 520, 580, 640]
        self.color = self.colors[self.n]
        self.player_num = player_num
        if player_num == 1:
            self.controller = controller
        self.player_position = 6

    def move_block(self, player_input, blocks_list):
        """
        Processes player input to move the animal left, right, or drop a block at the lowest possible unoccupied position in the column.

        Args:
            player_input (str): The input command from the player ('left', 'right', or 'drop') indicating the desired action.
            blocks_list (list of lists): The grid where blocks are placed, used to check for available spaces when dropping blocks.
        """
        if player_input == "right":
            if self.player_position == 7:
                self.player_position = 0
            else:
                self.player_position += 1
        elif player_input == "left":
            if self.player_position == 0:
                self.player_position = 7
            else:
                self.player_position -= 1
        elif player_input == "drop":
            # check to find lowest possible row at which block can exist
            row_to_place = 7
            while not blocks_list[self.player_position][row_to_place] == " ":
                row_to_place -= 1
                if row_to_place < 0:
                    break
            if row_to_place >= 0:
                block = Block(
                    self.possible_x_positions[self.player_position],
                    self.possible_y_positions[row_to_place],
                    n=self.n,
                )
                blocks_list[self.player_position][row_to_place] = block
                # print(blocks_list)
                self.n = random.randrange(4)
                self.color = self.colors[self.n]

    def draw_moving_blocks(self, screen):
        """
        Draws the moving animal on the provided Pygame screen at its current position using its current color.

        Args:
            screen: The Pygame display surface where the animal will be drawn as a 60x60 pixel rectangle at a position determined by the current player position.
        """
        pos = self.possible_x_positions[self.player_position]
        pygame.draw.rect(screen, self.color, pygame.Rect(pos, 30, 60, 60))
