###############################################################################
# File Name  : game_objects.py
# Date       : 12/17/2022
# Description: Base classes for mario and other game objects
###############################################################################

import pygame
import data.constants as const
import states.app as app


class GameObject(pygame.sprite.Sprite):
    def __init__(self, screen, x_pos, y_pos, width, height, name='game_object'):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.state = None
        self.image = pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def set_position(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        pass


class MovableEntity(GameObject):
    def __init__(self, screen, x_pos, y_pos, width, height, name='movable_object'):
        GameObject.__init__(self, screen, x_pos, y_pos, width, height)
        self.x_velocity = 1
        self.y_velocity = 1
        self.delta_x = 0
        self.delta_y = 0
        self.position_x = 0
        self.position_y = 0

    def update(self):
        self.move_position(1, 1)

    def move_position(self, x, y):
        self.delta_x = x
        self.delta_y = y
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y
        self.set_position(self.rect.x, self.rect.y)
