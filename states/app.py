###############################################################################
# File Name  : app.py
# Date       : 12/17/2022
# Description: top level of system
###############################################################################

import pygame
import random
import data.constants as const
import data.gameObjects.players.mario as mario
import data.gameObjects.game_object as go
import data.gameObjects.players.player as player
import states.joystick

player1_keybindings = {
    'action': pygame.K_n,
    'jump': pygame.K_m,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'down': pygame.K_DOWN,
    'up': pygame.K_UP
}

player2_keybindings = {
    'action': pygame.K_g,
    'jump': pygame.K_h,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'down': pygame.K_s,
    'up': pygame.K_w
}




class Controller:
    def __init__(self):
        print("main_init")
        self.run_game = True
        pygame.init()
        # init game_objects
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        pygame.display.set_caption(const.MAIN_CAPTION)
        self.keys = None
        joysticks = states.joystick.JoyStick()

        random.seed()
        self.static_object_width = 128
        self.static_object_height = 128
        self.movable_object_width = self.static_object_width / 2
        self.movable_object_height = self.static_object_height / 2
        self.player_object_width = self.movable_object_width / 2
        self.player_object_height = self.movable_object_height / 2
        self.mario_object_width = self.player_object_width / 2
        self.mario_object_height = self.player_object_height / 2


        self.a_static_object = go.GameObject(self.screen,
                                             random.randrange(0, const.SCREEN_WIDTH - self.static_object_width),
                                             random.randrange(0, const.SCREEN_HEIGHT - self.static_object_height),
                                             self.static_object_width,
                                             self.static_object_height)

        self.a_movable_object = go.MovableEntity(self.screen,
                                                 0,
                                                 0,
                                                 64,
                                                 64)
        self.a_player_object = player.Player(self.screen, 0, 0, 32, 32)
        self.mario_object = mario.Mario(self.screen, 0, const.SCREEN_HEIGHT-16, 16, 16)

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
                self.keys = pygame.key.get_pressed()
            if event.type == pygame.KEYUP:
                self.keys = pygame.key.get_pressed()

    def process_updates(self):
        pygame.display.update()
        self.a_static_object.update()
        self.a_movable_object.update()
        self.a_player_object.update(self.keys)
        self.mario_object.update(self.keys)

    def process_drawings(self):
        self.screen.fill(const.BLUE)
        self.a_static_object.draw()
        self.a_movable_object.draw()
        self.a_player_object.draw()
        self.mario_object.draw()
