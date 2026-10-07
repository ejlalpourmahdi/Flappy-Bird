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

#background
background = pygame.image.load("Python - Projects/flappy bird/assets/images/background.jpg")
background = pygame.transform.scale(background , (1200 , 800))
ground = pygame.image.load("Python - Projects/flappy bird/assets/images/ground.png")
ground = pygame.transform.scale(ground, (1287, 66))
groundScroll = -12

#bird character settings
birdIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/bird-icon.png")
birdWidth, birdHeight = 50, 50
birdIcon = pygame.transform.scale_by(birdIcon, 0.05)
class Bird:
    def __init__(self, img):
        self.x = 100
        self.y = displayHeigth // 2
        self.velocity = 0
        self.gravity = 0.5
        self.jumpPower = -8
        self.size = 50
        self.icon = img

    def jump(self):
        self.velocity = self.jumpPower
        wing.play()

    def fall(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def render(self):
        screen.blit(self.icon, (self.x, self.y))

    def reset(self):
        self.x = 100
        self.y = displayHeigth // 2
        self.velocity = 0
        self.gravity = 0.5
        self.jumpPower = -8
        self.size = 50
bird = Bird(birdIcon)
