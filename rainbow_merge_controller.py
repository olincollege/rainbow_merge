import pygame


class P1Controller:
    """
    A controller for player one, inheriting from the base controller class.
    Handles user input specific to player one using a keyboard.
    """

    def __init__(self):
        """
        Initializes the p1_controller with specific keyboard controls for player one.
        """
        self.keyboard_controls = [
            "A",
            "D",
            "S",
        ]  # Controls for player 1 (left, right, drop/superpower)

    def get_user_input(self):
        """
        Detects and returns the current user input based on the predefined keyboard controls.
        Returns:
            str: A string representing the player's action (left, right, drop) or 'no input' if no relevant keys are pressed.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            return "left"
        elif keys[pygame.K_d]:
            return "right"
        elif keys[pygame.K_s]:
            return "drop"
        elif keys[pygame.K_F2]:
            return "settings"
        return "no input"  # Default return when no relevant keys are pressed
