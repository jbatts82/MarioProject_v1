###############################################################################
# File Name  : main.py
# Date       : 12/17/2022
# Description: Main Loop - Run from here...
###############################################################################

import sys
import pygame
import states.app as app

pygame.init()
app_controller = app.Controller()

app_controller.main_loop()

# if game loop broke
pygame.quit()
sys.exit()
