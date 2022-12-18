###############################################################################
# File Name  : game_objects.py
# Date       : 12/17/2022
# Description: Base classes for mario and other game objects
###############################################################################

import pygame
import data.constants as const


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, width, height, name='game_object'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.state = None


class StaticEntity(GameObject):
    def __init__(self, x_pos, y_pos, width, height, name='static_object'):
        super().__init__(self, x_pos, y_pos, width, height, name)


class MovableEntity(GameObject):
    def __init__(self, x_pos, y_pos, width, height, name='movable_object'):
        super().__init__(x_pos, y_pos, width, height, name)

    def move(self):
        pass
