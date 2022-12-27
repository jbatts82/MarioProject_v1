###############################################################################
# File Name  : mario.py
# Date       : 12/17/2022
# Description: Mario data and logic
###############################################################################

import pygame
import data.constants as const
from data.gameObjects.movableEntities.players.player import Player
import communityChest.spriteSheet as ss


class Mario(Player):
    def __init__(self, screen, controller, x_pos, y_pos, width, height, name='mario_object'):
        print(name)
        Player.__init__(self, screen, controller, x_pos, y_pos, width, height)
        self.state = const.STAND
        self.sprite_sheet = pygame.image.load(const.MARIO_SPRITE_SHEET_LOC).convert_alpha()
        self.last_update = pygame.time.get_ticks()
        self.frame_idx = 0
        self.frame = None
        self.animation = []
        self.create_animation_dictionary()
        self.animation_cooldown = const.ANIMATION_COOLDOWN

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

    def handle_state(self, keys):
        if self.state == const.STAND:
            self.standing(keys)
        elif self.state == const.WALK:
            self.walking(keys)
        else:
            pass


    def update(self, keys):
        if keys is not None:
            if keys[self.key_binds['right']]:
                self.move_position(self.x_velocity, 0)
            if keys[self.key_binds['left']]:
                self.move_position(-self.x_velocity, 0)
            if keys[self.key_binds['up']]:
                pass
            if keys[self.key_binds['down']]:
                pass


    def standing(self, keys):
        self.x_velocity = 0
        self.y_velocity = 0

        if keys[self.key_binds['right']]:
            self.state = const.WALK

    def walking(self, keys):
        self.x_velocity += 1
        if keys is not None:
            if keys[self.key_binds['right']]:
                pass
            if keys[self.key_binds['left']]:
                pass

    def update_animation(self):
        pass

    def update_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation[self.frame]):
                frame = 0

        self.image = self.animation[self.frame]
