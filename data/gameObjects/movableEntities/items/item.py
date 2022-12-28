###############################################################################
# File Name  : item.py
# Date       : 12/26/2022
# Description: Base Item
###############################################################################

from data.gameObjects.game_object import MovableEntity


class Item(MovableEntity):
    def __init__(self, screen, x_pos, y_pos, width, height, name='item_object'):
        print(name)
        MovableEntity.__init__(self, screen, x_pos, y_pos, width, height)