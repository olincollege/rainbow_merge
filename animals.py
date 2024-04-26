import pygame
from abc import ABC
import random
from board import Board


class Block:
    def __init__(self, x_position, y_position, n=0):
        self.colors = [
            (245, 0, 0),
            (250, 100, 100),
            (150, 20, 250),
            (250, 210, 10),
            (250, 150, 0),
            (245, 0, 0),
            (250, 250, 100),
            (255, 180, 180),
            (255, 255, 0),
            (100, 235, 10),
            (0, 185, 0),
        ]
        self.n = n
        self.color = self.colors[self.n]
        self.possible_y_positions = [220, 280, 340, 400, 460, 520, 580, 640]
        self.x_position = x_position
        self.y_position = y_position
        self.speed = 3

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.color, pygame.Rect(self.x_position, self.y_position, 60, 60)
        )


class moving_animals:
    def __init__(self, player_num, controller):
        self.colors = [
            (245, 0, 0),
            (250, 100, 100),
            (150, 20, 250),
            (250, 210, 10),
            (250, 150, 0),
            (245, 0, 0),
            (250, 250, 100),
            (255, 180, 180),
            (255, 255, 0),
            (100, 235, 10),
            (0, 185, 0),
        ]
        self.n = random.randrange(4)
        self.possible_x_positions = [10, 70, 130, 190, 250, 310, 370, 430]
        self.possible_y_positions = [220, 280, 340, 400, 460, 520, 580, 640]
        self.color = self.colors[self.n]
        self.animal_positions = {
            0: (36, 50),
            1: (86, 50),
            2: (122, 50),
            3: (158, 50),
            4: (194, 50),
            5: (230, 50),
            6: (266, 50),
            7: (302, 50),
            8: (338, 50),
            9: (374, 50),
            10: (410, 50),
        }
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
            block = Block(
                self.possible_x_positions[self.player_position],
                self.possible_y_positions[row_to_place],
                n=self.n,
            )
            blocks_list[self.player_position][row_to_place] = block
            print(blocks_list)
            self.n = random.randrange(4)
            self.color = self.colors[self.n]

    def draw_moving_animals(self, screen):
        pos = self.possible_x_positions[self.player_position]
        pygame.draw.rect(screen, self.color, pygame.Rect(pos, 10, 60, 60))
