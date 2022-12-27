###############################################################################
# File Name  : cloud.py
# Date       : 12/26/2022
# Description: Static Objects, terrain object to challenge Mario.
###############################################################################

import pygame
import communityChest.spriteSheet as ss
import data.constants as const
from data.gameObjects.game_object import StaticEntity


class Cloud(StaticEntity):
    def __init__(self, screen, x_pos, y_pos, width, height, name='block_object'):
        print(name)
        StaticEntity.__init__(self, screen, x_pos, y_pos, width, height)
        self.sprite_sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()

        self.get_cloud_image()

    def get_cloud_image(self):
        sprite_tool = ss.SpriteSheet(self.sprite_sheet)
        self.image1 = []
        self.image1.append(sprite_tool.extract_image(162, 198, 32, 24))
        self.image1[0].set_colorkey(const.BLACK)
        self.image = self.image1[0]



