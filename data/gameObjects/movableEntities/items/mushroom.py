###############################################################################
# File Name  : mushroom.py
# Date       : 12/27/2022
# Description: Mushroom Item
###############################################################################

import pygame
import communityChest.spriteSheet as ss
import data.constants as const
from data.gameObjects.movableEntities.items.item import Item


class Mushroom(Item):
    def __init__(self, screen, x_pos, y_pos, width, height, name='mushroom_object'):
        print(name)
        Item.__init__(self, screen, x_pos, y_pos, width, height)
        self.sprite_sheet = pygame.image.load(const.MISC3_LOC).convert_alpha()
        self.get_image()

    def get_image(self):
        sprite_tool = ss.SpriteSheet(self.sprite_sheet)
        self.image1 = []
        self.image1.append(sprite_tool.extract_image(52, 43, 16, 16))
        self.image1[0].set_colorkey(const.BLACK)
        self.image = self.image1[0]
