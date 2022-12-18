###############################################################################
# File Name  : player.py
# Date       : 12/18/2022
# Description: Mario data and logic
###############################################################################

from data.gameObjects.game_object import MovableEntity


class Player(MovableEntity):
    def __init__(self, screen, x_pos, y_pos, width, height, name='player'):
        MovableEntity.__init__(self, screen, x_pos, y_pos, width, height)
