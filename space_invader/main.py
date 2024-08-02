import pygame
import math
import random
from pygame import mixer

# game initialization
pygame.init()

screen = pygame.display.set_mode((800,600))
# (0,0) top left 

background = pygame.image.load("background.png")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Background music
mixer.music.load("background.wav")
mixer.music.play(-1)

# player 
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,736)
enemyY = random.randint(40, 150)
enemyX_change = 1
enemyY_change = 40

# bullet 
bulletImg = pygame.image.load("bullet.png")
bulletX = 480
bulletY = 0
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def firebullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+10))

score = 0

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False

# Scoreboard
font = pygame.font.Font('freesansbold.ttf',32)
def show_score(x,y):
    scoreTitle = font.render("Score:"+str(score), True, (255,255,255))
    screen.blit(scoreTitle,(x,y))

# Game over
def game_over_text():
    over_font = pygame.font.Font('freesansbold.ttf',64)
    over_text = over_font.render("Score:"+str(score), True, (255,255,255))
    screen.blit(over_text,(260,200))

# game loop
running = True
while running:
    # blank screen 
    screen.fill((0,0,0))

    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_SPACE:
                if (bullet_state is "ready"):
                    bulletX = playerX
                    firebullet(bulletX, bulletY)
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
    playerX += playerX_change
    # ensure player stays on the screen
    if (playerX >= 736):
        playerX = 736
    if (playerX <= 0):
        playerX = 0

    # dynamics of enemy
    enemyX += enemyX_change
    if (enemyX<0 or enemyX>736):
        enemyX_change *= -1
        enemyY += enemyY_change

    # dynamics of bullets 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        firebullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # collision detection 
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        collisionSound = mixer.Sound("explosion.wav")
        collisionSound.play()
        bulletY = 480
        bullet_state = "ready"
        score += 10
        enemyX = random.randint(0,736)
        enemyY = random.randint(40, 150)

    if enemyY > 440:
        enemyY = 3000
        game_over_text()

    scoreX, scoreY = 10, 10

    show_score(scoreX, scoreY)
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
