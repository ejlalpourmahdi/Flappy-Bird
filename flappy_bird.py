import pygame
import random

pygame.init()

#game font
font = pygame.font.SysFont("Lupulus-Bold" , 50)
border = pygame.font.SysFont("Lupulus-Bold" , 60)

#game display setting
displayWidth = 1200
displayHeigth = 800
gameIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/game-icon.png")
screen = pygame.display.set_mode((displayWidth, displayHeigth))
pygame.display.set_caption("Flappy Bird")
pygame.display.set_icon(gameIcon)
