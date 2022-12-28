###############################################################################
# File Name  : app.py
# Date       : 12/17/2022
# Description: top level of system
###############################################################################

import pygame
import random
import data.constants as const
import data.gameObjects.movableEntities.players.mario as mario
import data.gameObjects.movableEntities.players.luigi as luigi
import data.gameObjects.movableEntities.players.player as player
import data.gameObjects.staticEntities.block as block
import data.gameObjects.staticEntities.cloud as cloud
import data.gameObjects.movableEntities.items.mushroom as mushroom
import states.joystick
import states.keyboard


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
        keyboard1 = states.keyboard.Keyboard(0)
        keyboard2 = states.keyboard.Keyboard(1)
        random.seed()
        self.static_object_width = 128
        self.static_object_height = 128
        self.movable_object_width = self.static_object_width / 2
        self.movable_object_height = self.static_object_height / 2
        self.player_object_width = self.movable_object_width / 2
        self.player_object_height = self.movable_object_height / 2
        self.mario_object_width = self.player_object_width / 2
        self.mario_object_height = self.player_object_height / 2

        # define objects to draw on the game screen
        self.a_block = block.Block(self.screen,
                                   random.randrange(0, const.SCREEN_WIDTH - self.static_object_width),
                                   random.randrange(0, const.SCREEN_HEIGHT - self.static_object_height),
                                   self.static_object_width,
                                   self.static_object_height)

        self.a_cloud = cloud.Cloud(self.screen,
                                   random.randrange(0, const.SCREEN_WIDTH - self.static_object_width),
                                   random.randrange(0, const.SCREEN_HEIGHT/2 - self.static_object_height),
                                   self.static_object_width,
                                   self.static_object_height)

        self.a_mushroom = mushroom.Mushroom(self.screen,
                                            random.randrange(0, const.SCREEN_WIDTH - self.static_object_width),
                                            random.randrange(0, const.SCREEN_HEIGHT - self.static_object_height),
                                            16,
                                            16)


        self.luigi_object = luigi.Luigi(self.screen, keyboard1, 0, 0, 32, 32)
        self.mario_object = mario.Mario(self.screen,
                                        keyboard2,
                                        0,
                                        const.SCREEN_HEIGHT - (16 * const.SIZE_MULTIPLIER),
                                        16,
                                        16)


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
        self.a_block.update()
        self.a_cloud.update()
        self.a_mushroom.update()
        self.luigi_object.update(self.keys)
        self.mario_object.update(self.keys)

    def process_drawings(self):
        self.screen.fill(const.BLUE)
        self.a_block.draw()
        self.a_cloud.draw()
        self.a_mushroom.draw()
        self.luigi_object.draw()
        self.mario_object.draw()
