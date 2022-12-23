###############################################################################
# File Name  : joystick.py
# Date       : 12/23/2022
# Description: Input from nes style joystick
###############################################################################

import pygame.joystick

pygame.joystick.init()

nes_controller_keybindings = {
    'action': pygame.K_g,
    'jump': pygame.K_h,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'down': pygame.K_s,
    'up': pygame.K_w
}


class JoyStick:
    def __init__(self, name='JoyStick_object'):
        print(name)
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        print("JoySticks Available: " + str(joysticks))

    def update(self, keys):
        pass
