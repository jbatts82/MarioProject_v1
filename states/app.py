###############################################################################
# File Name  : app.py
# Date       : 12/17/2022
# Description: top level of system
###############################################################################

import pygame
import data.constants as const

keybindings = {
    'action': pygame.K_s,
    'jump': pygame.K_a,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'down': pygame.K_DOWN,
    'up': pygame.K_UP
}


class Control:
    def __init__(self):
        # init control objects
        self.run_game = True

        # set up clock
        self.clock = pygame.time.Clock()

    def main_loop(self):
        while self.run_game:
            self.clock.tick(const.FPS)
