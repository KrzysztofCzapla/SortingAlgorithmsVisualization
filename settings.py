import pygame
pygame.init()
pygame.font.init()
#### SCREEN ####

# Get display info
infoObject = pygame.display.Info()

WIDTH = int(infoObject.current_w*2/3)
HEIGHT = int(infoObject.current_h*2/3)

################

FONT = pygame.font.SysFont('arial', 30)


COLOR = (10,110,10)
COLOR_ELEMENT = (100,10,10)
COLOR_BACKGROUND = (255,255,255)

FPS = 60