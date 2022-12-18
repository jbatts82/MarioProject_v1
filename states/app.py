###############################################################################
# File Name  : app.py
# Date       : 12/17/2022
# Description: top level of system
###############################################################################

import pygame
import data.constants as const
import data.gameObjects.players.mario as mario

keybindings = {
    'action': pygame.K_s,
    'jump': pygame.K_a,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'down': pygame.K_DOWN,
    'up': pygame.K_UP
}


class Controller:
    def __init__(self):
        self.run_game = True
        pygame.init()
        # init game_objects
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        pygame.display.set_caption(const.MAIN_CAPTION)
        self.mario = mario.Mario(self.screen, 1, 1, 16, 16)

    def main_loop(self):
        print("main_loop")
        while self.run_game:
            self.process_events()
            self.process_updates()
            self.process_drawings()
            pygame.display.flip()
            self.clock.tick(const.FPS)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == keybindings['down']:
                    print("Down")
                if event.key == keybindings['up']:
                    print("Up")
                if event.key == keybindings['left']:
                    print("Left")
                if event.key == keybindings['right']:
                    print("Right")
                if event.key == keybindings['action']:
                    print("Action")
                if event.key == keybindings['jump']:
                    print("Jump")

    def process_updates(self):
        pygame.display.update()
        self.mario.update()

    def process_drawings(self):
        self.screen.fill(const.BLUE)
        self.mario.draw()
