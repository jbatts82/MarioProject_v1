###############################################################################
# File Name  : block.py
# Date       : 12/26/2022
# Description: Static Objects, terrain object to challenge Mario.
###############################################################################

import pygame
import communityChest.spriteSheet as ss
import data.constants as const
from data.gameObjects.game_object import StaticEntity


class Block(StaticEntity):
    def __init__(self, screen, x_pos, y_pos, width, height, name='block_object'):
        print(name)
        StaticEntity.__init__(self, screen, x_pos, y_pos, width, height)
        self.sprite_sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()

        self.get_block_image()

    def get_block_image(self):
        sprite_tool = ss.SpriteSheet(self.sprite_sheet)
        self.image1 = []
        self.image1.append(sprite_tool.extract_image(373, 142, 16, 16))
        self.image = self.image1[0]


