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

#menu
logoType = pygame.image.load("Python - Projects/flappy bird/assets/images/Flappy-Bird-logo.png")
logoType = pygame.transform.scale(logoType, (448, 216))
startButtonIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/start-button.png")
startButtonIcon = pygame.transform.scale(startButtonIcon, (330, 130))
startButtonRect = startButtonIcon.get_rect(topleft = (435, 550))
menu = True

#score
scoreTable = pygame.image.load("Python - Projects/flappy bird/assets/images/scores-table.png")
scoreTable = pygame.transform.scale_by(scoreTable, 5)
ironMedal = pygame.image.load("Python - Projects/flappy bird/assets/images/iron-medal.png")
ironMedal = pygame.transform.scale_by(ironMedal, 5)
bronzeMedal = pygame.image.load("Python - Projects/flappy bird/assets/images/bronze-medal.png")
bronzeMedal = pygame.transform.scale_by(bronzeMedal, 5)
silverMedal = pygame.image.load("Python - Projects/flappy bird/assets/images/silver-medal.png")
silverMedal = pygame.transform.scale_by(silverMedal, 5)
goldMedal = pygame.image.load("Python - Projects/flappy bird/assets/images/gold-medal.png")
goldMedal = pygame.transform.scale_by(goldMedal, 5)
newRecordIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/new-record-icon.png")
newRecordIcon = pygame.transform.scale_by(newRecordIcon, 2)
newRecord = False
score = 0
bestScore = 0

#musics and sounds
pygame.mixer.music.load("Python - Projects/flappy bird/assets/sounds/game-music.mp3")
pygame.mixer.music.play(-1)
wing = pygame.mixer.Sound("Python - Projects/flappy bird/assets/sounds/wing.wav")

#gameover settings
gameover = False
gameoverIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/game-over-icon.png")
gameoverIcon = pygame.transform.scale(gameoverIcon, (384, 84))
playButtonIcon = pygame.image.load("Python - Projects/flappy bird/assets/images/play-button.png")
playButtonIcon = pygame.transform.scale_by(playButtonIcon, 3)
playButtonX = 505
playButtonY = 620
playButtonRect = playButtonIcon.get_rect(topleft = (playButtonX, playButtonY))


#tutorial
tutorial = False
tutorialIMG = pygame.image.load("Python - Projects/flappy bird/assets/images/click-tutorial.png")
tutorialIMG = pygame.transform.scale(tutorialIMG, (144, 384))

#loading
loadingIMG = pygame.image.load("Python - Projects/flappy bird/assets/images/loading.jpg")
loadingIMG = pygame.transform.scale(loadingIMG, (1200, 800))
menuLoading = False
mlc = 0
gameoverLoading = False
goc = 0

#fps
fps = pygame.time.Clock()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()
        #bird jump
        if pygame.mouse.get_pressed()[0]:
            bird.jump()

    #render the background
    screen.blit(background, (0, 0))
    screen.blit(ground, (groundScroll, 736))


    #menu performance
    if menu:
        mousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and startButtonRect.collidepoint(mousePos):
            menu = False
            menuLoading = True
            mlc = 0
        
        #render the menu sources
        screen.blit(logoType, (376, 20))
        screen.blit(birdIcon , (826 , 118))
        screen.blit(startButtonIcon, (435, 550))
