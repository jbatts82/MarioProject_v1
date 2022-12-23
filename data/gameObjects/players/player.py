###############################################################################
# File Name  : player.py
# Date       : 12/18/2022
# Description: Mario data and logic
###############################################################################

from data.gameObjects.game_object import MovableEntity
import states.app as app


class Player(MovableEntity):
    def __init__(self, screen, x_pos, y_pos, width, height, name='player'):
        MovableEntity.__init__(self, screen, x_pos, y_pos, width, height)

    def update(self, keys):
        if keys is not None:
            if keys[app.player1_keybindings['right']]:
                self.move_position(self.x_velocity, 0)
            if keys[app.player1_keybindings['left']]:
                self.move_position(-self.x_velocity, 0)
            if keys[app.player1_keybindings['up']]:
                self.move_position(0, -self.y_velocity)
            if keys[app.player1_keybindings['down']]:
                self.move_position(0, self.y_velocity)
