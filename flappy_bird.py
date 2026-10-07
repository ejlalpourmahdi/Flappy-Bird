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

#pipes settings
pipeWidth = 100
pipeIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/pipe-icon.png")
rotatedPipeIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/rotated-pipe-icon.png")
pipes = []
class Pipe:
    def __init__(self):
        self.x = displayWidth
        self.width = 70
        self.gap = 150
        self.bottomPipeHeight = random.randint(100, 400)
        self.bottomPipeY = displayHeigth - self.bottomPipeHeight
        self.pipeIcon = pygame.transform.scale(pipeIcon, (pipeWidth, self.bottomPipeHeight))
        self.topPipeHeight = displayHeigth - (self.bottomPipeHeight + self.gap)
        self.rotatedPipeIcon = pygame.transform.scale(rotatedPipeIcon, (pipeWidth, self.topPipeHeight))
        self.speed = 4

    #move the pipes
    def move(self):
        self.x -= self.speed

    #render the pipes
    def render(self):
        screen.blit(self.rotatedPipeIcon, (self.x, 0))
        screen.blit(self.pipeIcon, (self.x, self.bottomPipeY))

    def reset(self):
        self.x = displayWidth
        self.width = 70
        self.gap = 150
        self.bottomPipeHeight = random.randint(100, 400)
        self.bottomPipeY = displayHeigth - self.bottomPipeHeight
        self.pipeIcon = pygame.transform.scale(pipeIcon, (pipeWidth, self.bottomPipeHeight))
        self.topPipeHeight = displayHeigth - (self.bottomPipeHeight + self.gap)
        self.rotatedPipeIcon = pygame.transform.scale(rotatedPipeIcon, (pipeWidth, self.topPipeHeight))
        self.speed = 4
pipes.append(Pipe())
