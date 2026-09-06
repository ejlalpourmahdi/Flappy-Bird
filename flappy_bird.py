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

    #tutorial performance
    if tutorial:
        if pygame.mouse.get_pressed()[0]:
            tutorial = False

        #render the tutorial sources
        bird.render()
        screen.blit(tutorialIMG, (558, 208))

    #game performance
    if menu == False and tutorial == False and gameover == False and menuLoading == False and gameoverLoading == False:
        

        #ground moves
        groundScroll -= 1
        if groundScroll < -89:
            groundScroll = 0

        #bird fall
        bird.fall()

        #render the pipes
        for i in range(len(pipes)):
            pipes[i].move()
            pipes[i].render()
            #load new pipes
            if pipes[-1].x < 550:
                pipes.append(Pipe())
            
            #bird collision check
            if ((bird.y <= pipes[i].topPipeHeight) and (pipes[i].x <= bird.x <= pipes[i].x+pipeWidth)) or ((bird.y >= displayHeigth-pipes[i].bottomPipeHeight-10) and (pipes[i].x <= bird.x <= pipes[i].x+pipeWidth)):
                gameover = True
                gmoY = 0
                stY = 800
                stc = 0
                bestScorec = 0
                
            if bird.y < 0 or bird.y > 800 - birdHeight:
                gameover = True
                gmoY = 0
                stY = 800
                stc = 0
                bestScorec = 0

            #increase the score
            if bird.x == pipes[i].x + pipeWidth:
                score += 1
                
                
            

        screen.blit(birdIcon , (bird.x , bird.y))
        scoreText = font.render(f"{score}" , True , (255, 255, 255))
        scoreTextBorder = border.render(f"{score}" , True , (0, 0, 0))
        screen.blit(scoreTextBorder , (572 , 17))
        screen.blit(scoreText , (575 , 20))
        pygame.display.update()

    #loading performance
    if menuLoading:
        mlc += 1
        if mlc < 150:
            screen.blit(loadingIMG, (0, 0))
        else:
            menuLoading = False
            tutorial = True
    if gameoverLoading:
        goc += 1
        if goc < 150:
            screen.blit(loadingIMG, (0, 0))
        else:
            gameoverLoading = False
            menu = True

    #gameover performance
    if gameover:
        if score > bestScore :
            bestScore = score
            if score != 0:
                newRecord = True
        
        #render gameover text
        gmoY += 3
        if gmoY > 100:
            gmoY = 100
        screen.blit(gameoverIcon, (404, gmoY))
        
        #render scores table
        stY -= 5
        if stY < 310:
            stY = 310
        screen.blit(scoreTable, (287, stY))


        #render score and best score
        if stY == 310:
            if stc < score:
                stc += 1
            stcText = font.render(f"{stc}", True, (255, 255, 255))
            stcBorder = border.render(f"{stc}", True, (0, 0, 0))
            screen.blit(stcBorder, (732 , 390))
            screen.blit(stcText, (735 , 393))
            if bestScorec < bestScore:
                bestScorec += 1
            bstcText = font.render(f"{bestScorec}", True, (255, 255, 255))
            bstcBorder = border.render(f"{bestScorec}", True, (0, 0, 0))
            screen.blit(bstcBorder, (732 , 500))
            screen.blit(bstcText, (735 , 503))
            #render the new record icon
            if newRecord:
                screen.blit(newRecordIcon, (672, 525))
            #render the medals
            if 10 <= score < 20:
                screen.blit(ironMedal, (353, 415))
            if 20 <= score < 30:
                screen.blit(bronzeMedal, (353, 415))
            if 30 <= score < 40:
                screen.blit(silverMedal, (353, 415))
            if 40 <= score:
                screen.blit(goldMedal, (353, 415))

            #render play button
            screen.blit(playButtonIcon, (playButtonX, playButtonY))
            mousePos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and playButtonRect.collidepoint(mousePos):
                goc = 0
                gameoverLoading = True
                gameover = False
                score = 0
                bird.reset()
                Pipe().reset()
                newRecord = False
                pipes=[]
                pipes.append(Pipe())

    pygame.display.update()
    fps.tick(60)
