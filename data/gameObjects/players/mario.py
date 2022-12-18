###############################################################################
# File Name  : mario.py
# Date       : 12/17/2022
# Description: Mario data and logic
###############################################################################

import pygame
import data.constants as const
from data.gameObjects.players.player import Player
import communityChest.spriteSheet as ss


class Mario(Player):
    def __init__(self, x_pos=None, y_pos=None, width=None, height=None, name='mario'):
        super().__init__(x_pos, y_pos, width, height)
        self.state = const.STAND
        self.sprite_sheet = pygame.image.load(const.MARIO_SPRITE_SHEET_LOC).convert_alpha()
        self.last_update = pygame.time.get_ticks()
        self.animation_idx = 0
        self.animations = []
        self.create_animation_dictionary()

    # chopping up 'mario_bros.png' into actions and frames
    def create_animation_dictionary(self):
        # load sprite sheet into extracting tool
        sprite_tool = ss.SpriteSheet(self.sprite_sheet)

        self.right_frames = []
        self.left_frames = []
        self.right_small_reg_frames = []
        self.right_big_reg_frames = []
        self.left_small_reg_frames = []
        self.left_big_reg_frames = []

        # Get images for right side mario
        self.right_small_reg_frames.append(sprite_tool.extract_image(80, 32, 16, 16))
        self.right_small_reg_frames.append(sprite_tool.extract_image(80 + 16, 32, 16, 16))
        self.right_small_reg_frames.append(sprite_tool.extract_image(80 + 16 + 16, 32, 16, 16))

        self.right_big_reg_frames.append(sprite_tool.extract_image(80, 0, 16, 32))
        self.right_big_reg_frames.append(sprite_tool.extract_image(80 + 16 + 16, 0, 16, 32))
        self.right_big_reg_frames.append(sprite_tool.extract_image(80 + 16, 0, 16, 32))

        # Create images for left side mall mario
        for frame in self.right_small_reg_frames:
            new_image = pygame.transform.flip(frame, True, False)
            self.left_small_reg_frames.append(new_image)

        self.reg_small_frames = [self.right_small_reg_frames, self.left_small_reg_frames]

        self.animations.append(self.right_small_reg_frames)
        self.animations.append(self.right_big_reg_frames)