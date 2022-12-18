###############################################################################
# File Name  : player.py
# Date       : 12/18/2022
# Description: Mario data and logic
###############################################################################

from data.gameObjects.game_object import MovableEntity


class Player(MovableEntity):
    def __init__(self, x_pos=None, y_pos=None, width=None, height=None, name='player'):
        super().__init__(x_pos, y_pos, width, height)
