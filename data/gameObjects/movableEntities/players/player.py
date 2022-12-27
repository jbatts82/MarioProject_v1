###############################################################################
# File Name  : player.py
# Date       : 12/18/2022
# Description: Mario data and logic
###############################################################################

from data.gameObjects.game_object import MovableEntity


class Player(MovableEntity):
    def __init__(self, screen, controller,  x_pos, y_pos, width, height, name='player_object'):
        print(name)
        MovableEntity.__init__(self, screen, x_pos, y_pos, width, height)
        self.controller = controller
        self.key_binds = self.controller.get_configuration()


    def update(self, keys):
        if keys is not None:
            if keys[self.key_binds['right']]:
                self.move_position(self.x_velocity, 0)
            if keys[self.key_binds['left']]:
                self.move_position(-self.x_velocity, 0)
            if keys[self.key_binds['up']]:
                self.move_position(0, -self.y_velocity)
            if keys[self.key_binds['down']]:
                self.move_position(0, self.y_velocity)
