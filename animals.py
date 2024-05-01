import pygame
from abc import ABC
import random
from board import Board


class Block:
    def __init__(self, x_position, y_position, n=0):
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
        self.death = False

    def get_color(self):
        # testng

        return self.color

    def draw(self, screen):
        # 60x60 pixel rectangle
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

        Parameters:
            self (Grid): The grid object instance.
            x_position (int): The x-coordinate of the current block.
            y_position (int): The y-coordinate of the current block.
            blocks_list (list): 2D list representing the grid of blocks.
        Returns:
            None
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
        """Moves the block to the lowest possible space that it can fill."""
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
        else:
            if isinstance(blocks_list[x_position][y_position], Block) and isinstance(
                blocks_list[x_position][y_position + 1], str
            ):
                blocks_list[x_position][y_position].death = True

        return False

    def horizontal_merge(
        self,
        x_position,
        y_position,
        blocks_list,
    ):
        """
        Merge the current block with the one on its right if conditions are met.

        Parameters:
            self (Grid): The grid object instance.
            x_position (int): The x-coordinate of the current block.
            y_position (int): The y-coordinate of the current block.
            blocks_list (list): 2D list representing the grid of blocks.
        Returns:
            None
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


class MovingAnimal:
    def __init__(self, player_num, controller):
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

    def move_animal(self, player_input, blocks_list):
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

    def draw_moving_animals(self, screen):
        pos = self.possible_x_positions[self.player_position]
        pygame.draw.rect(screen, self.color, pygame.Rect(pos, 30, 60, 60))
