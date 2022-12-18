###############################################################################
# File Name  : game_objects.py
# Date       : 12/17/2022
# Description: Base classes for mario and other game objects
###############################################################################

import pygame
import data.constants as const


class GameObject(pygame.sprite.Sprite):
    def __init__(self, screen, x_pos, y_pos, width, height, name='game_object'):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.state = None
        self.image = pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.tempx = 0
        self.tempy = 0


    def update(self):
        self.tempy += 1
        self.set_position(self.tempx, self.tempy)

    def set_position(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos

    def draw(self):
        self.screen.blit(self.image, self.rect)




class MovableEntity(GameObject):
    def __init__(self, screen, x_pos, y_pos, width, height, name='movable_object'):
        GameObject.__init__(self, screen, x_pos, y_pos, width, height)
        pass

    def move(self):
        pass
