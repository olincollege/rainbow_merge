import pygame


class Controller:
    """
    A base controller class providing basic functionalities for game controllers.
    This class includes methods to restart the game, display help information, and list game controls.
    """

    def main_settings(self):
        """
        Function when F2 is called
        """
        pass

    def restart(self):
        """
        Resets the game to its initial state. This method should be implemented to define
        what happens when the game is restarted, such as resetting scores and game entities.
        """
        pass

    def help(self):
        """
        Displays help information to the player. This method should be implemented to provide
        guidance on how to play the game or describe the controls.
        """
        pass

    def get_controls(self):
        """
        Lists or displays the controls for the game. This method could return a list of controls
        or display them on the game screen.
        """
        pass


class P1Controller(Controller):
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
