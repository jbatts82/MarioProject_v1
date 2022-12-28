###############################################################################
# File Name  : constants.py
# Date       : 12/17/2022
# Description: Game constants
###############################################################################

# screen constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
MAIN_CAPTION = 'My Mario Lab'
FPS = 60

# controller configs
CONFIG_1 = 0
CONFIG_2 = 1
NES_1 = 0


# sprite locations
MARIO_SPRITE_SHEET_LOC = 'resources/graphics/mario_bros.png'
BACKGROUND_PNG_LOC = 'resources/graphics/level_1.png'
MISC3_LOC = 'resources/graphics/misc-3.gif'

# sprite attributes
SIZE_MULTIPLIER = 5
ANIMATION_COOLDOWN = 150

# mario states
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
GETTING_BIGGER = 'small to big'
GETTING_SMALLER = 'big to small'
DEATH_JUMP = 'death jump'

# hex colors codes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
UNUSED_COLOR = (255, 0, 255)
