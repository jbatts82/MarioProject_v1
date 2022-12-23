###############################################################################
# File Name  : mario.py
# Date       : 12/17/2022
# Description: Mario data and logic
###############################################################################

import pygame
import data.constants as const
from data.gameObjects.players.player import Player
import communityChest.spriteSheet as ss
import states.app as app


class Mario(Player):
    def __init__(self, screen, x_pos, y_pos, width, height, name='mario'):
        Player.__init__(self, screen, x_pos, y_pos, width, height)
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

    def handle_state(self, keys):
        if self.state == const.STAND:
            self.standing(keys)
        elif self.state == const.WALK:
            self.walking(keys)
        elif self.state == const.JUMP:
            self.jumping(keys)
        elif self.state == const.FALL:
            self.falling(keys)
        elif self.state == const.DEATH_JUMP:
            self.jumping_to_death(keys)
        elif self.state == const.GETTING_BIGGER:
            self.changing_to_big()
        elif self.state == const.GETTING_SMALLER:
            self.changing_to_small()
        else:
            pass

    def update(self, keys):
        if keys is not None:
            if keys[app.keybindings['right']]:
                self.move_position(self.x_velocity, 0)
            if keys[app.keybindings['left']]:
                self.move_position(-self.x_velocity, 0)
            if keys[app.keybindings['up']]:
                self.move_position(0, -self.y_velocity)
            if keys[app.keybindings['down']]:
                self.move_position(0, self.y_velocity)

    def standing(self, keys):
        self.x_velocity = 0
        self.y_velocity = 0

        if keys[app.keybindings['right']]:
            self.state = const.WALK

    def walking(self, keys):
        self.x_velocity += 1
        if keys is not None:
            if keys[app.keybindings['right']]:
                self.update_position(1, 0)
            if keys[app.keybindings['left']]:
                self.update_position(-1, 0)
