import pygame
import random
import math
import datetime
from pygame import mixer
import time
# initializing Game
pygame.init()
scorea = 3
music = False
# setting size of screen
screen = pygame.display.set_mode((800, 600))
# Title and Icon
pygame.display.set_caption('COVID-19 ATTACKS')
icons = pygame.image.load('icon.png')
pygame.display.set_icon(icons)
# Player
playerImg = pygame.image.load('player.png')
playerX = 400
playerY = 500
playerX_change = 0

r = random.choice(range(0, 255))
gr = random.choice(range(0, 255))
bl = random.choice(range(0, 255))
odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []
num = 23
for i in range(num):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(50)
    enemyY_change.append(30)
    if i in odd:
        enemyX_change.append(0.5)
    else:
        enemyX_change.append(-0.5)

# BULLET
bulletImg = pygame.image.load('water.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 1.5
bullet_state = 'Ready'

score = 0
font = pygame.font.Font('freesansbold.ttf', 40)
fo = pygame.font.Font('freesansbold.ttf', 20)
fon = pygame.font.Font('freesansbold.ttf', 33)
textX = 10
textY = 10

coll = False


def show_score(a, b):
    scorev = font.render('SCORE ::' + str(score), True, (0, 0, 0))
    screen.blit(scorev, (a, b))


def state(c, d):
    states = fo.render(str(bullet_state), True, (0, 0, 0))
    screen.blit(states, (c, d))


def player(e, f):
    screen.blit(playerImg, (e, f))


def enemy(g, h, j):
    screen.blit(enemyImg[j], (g, h))


def firebullet(k, m):
    global bullet_state
    bullet_state = 'Reloading...'
    screen.blit(bulletImg, (k + 16, m + 10))


def collision(a, b, c, d):
    e = (a - c) ** 2
    f = (b - d) ** 2
    g = math.sqrt(e + f)
    if g <= 35:
        return True
    else:
        return False


class button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            fonta = pygame.font.SysFont('comicsans', 60)
            text = fonta.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos1):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos1[0] < self.x + self.width:
            if self.y < pos1[1] < self.y + self.height:
                return True

        return False


def draw():
    but.draw(screen, (0, 0, 0))


def draw1():
    end1.draw(screen, (0, 0, 0))


def draw2():
    end2.draw(screen, (0, 0, 0))


but = button((255, 88, 51), 336, 400, 200, 75, 'START')
end1 = button((255, 0, 0), 100, 500, 200, 75, 'END')
end2 = button((255, 0, 0), 400, 500, 200, 75, 'REDO')
imnum = 0
img1 = pygame.image.load('q1.png')
img2 = pygame.image.load('q2.png')
img3 = pygame.image.load('q3.png')
img4 = pygame.image.load('q4.png')
img5 = pygame.image.load('q5.png')
img6 = pygame.image.load('q6.png')
img7 = pygame.image.load('q7.png')
images = [img1, img2, img3, img4, img5, img6, img7]
specialX = random.randint(10, 700)
specialY = 50
specialX_change = 0.5
specialY_change = 30
spImg = pygame.image.load('divide.png')
spnum = 0
# Positive start here
mail = 0
score_m = 1
m = 'MEH'
r = 0
g = 0
b = 0
halfe = False
image = False
# Game Loop
Game = False
end = False
running = True
running_1 = False
while running:
    if Game is False:
        screen.fill((255, 255, 255))
        ins1 = fo.render('PRESS W MOVE LEFT', True, (00, 175, 255))
        screen.blit(ins1, (0, 0))
        ins3 = fo.render('PRESS D TO MOVE RIGHT', True, (255, 0, 255))
        screen.blit(ins3, (0, 50))
        ins4 = fo.render('PRESS SPACE TO FIRE', True, (00, 255, 00))
        screen.blit(ins4, (0, 100))
        ins5 = fo.render('IF YOU HIT THE SPECIAL ICON', True, (00, 00, 00))
        screen.blit(ins5, (0, 150))
        ins6 = fo.render('THEN THE NUMBER OF COVID-19 GERMS WILL BE HALFED FOR SOME TIME.',
                         True, (00, 00, 00))
        screen.blit(ins6, (0, 175))
        ins2 = fon.render('IT IS TIME TO TAKE REVENGE FROM COVID - 19', True, (255, 00, 00))
        screen.blit(ins2, (0, 260))
        draw()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if but.isOver(pos):
                    Game = True
                    running_1 = True
                    x = datetime.datetime.now()
                    y = x.strftime('%H:%M:%S')
            if event.type == pygame.MOUSEMOTION:
                if but.isOver(pos):
                    but.color = (219, 255, 51)
                else:
                    but.color = (255, 88, 51)
    if running_1:
        if coll is True and imnum < 3000:
            global ima
            img = ima
            screen.fill((255, 0, 0))
            screen.blit(img, (00, 00))
            imnum += 1
        # Background ( RED, GREEN, Blue)
        else:
            screen.fill((255, 255, 255))
            coll = False
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    running = False
                if event1.type == pygame.KEYDOWN:
                    if event1.key == pygame.K_d:
                        playerX_change = (0.5 + (score / 200))
                    if event1.key == pygame.K_a:
                        playerX_change = (-0.5 - (score / 200))
                    if event1.key == pygame.K_SPACE and bullet_state == 'Ready':
                        bulletX = playerX
                        firebullet(bulletX, bulletY)
                if event1.type == pygame.KEYUP:
                    if event1.key == pygame.K_d or event1.key == pygame.K_a:
                        playerX_change = 0
            playerX += playerX_change
            if playerX >= 736:
                playerX = 736
            elif playerX <= 0:
                playerX = 0
            if halfe:
                en = round(int(scorea + 1) / 2)
            else:
                en = scorea + 1
            for i in range(en):
                if enemyX_change[i] >= 0:
                    enemyX[i] += (enemyX_change[i] + (score / 200))
                else:
                    enemyX[i] += (enemyX_change[i] - (score / 200))
                if enemyX[i] >= 736:
                    enemyX[i] = 736
                    enemyX_change[i] = -0.5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] <= 0:
                    enemyX[i] = 0
                    enemyX_change[i] = 0.5
                    enemyY[i] += enemyY_change[i]
                if enemyY[i] > 440:
                    running_1 = False
                    end = True
                    a = datetime.datetime.now()
                    b = a.strftime('%H:%M:%S')
                    o = ','.join(map(str, y.split(':')))
                    h = int(o[0] + o[1])
                    m = int(o[3] + o[4])
                    s = int(o[6] + o[7])
                    dif = a - datetime.timedelta(hours=h, minutes=m, seconds=s)
                    diff = dif.strftime('%H:%M:%S')
                    d = diff.split(':')
                    print('YOU TOOK ', d[0], 'HOURS,', d[1], 'MINUTES AND ', d[2], 'SECONDS')
                collide = collision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collide:
                    bulletY = 500
                    bullet_state = 'Ready'
                    score += score_m
                    scorea += 1
                    score_m += 1
                    if scorea > 19:
                        scorea = 19
                    print(score)
                    enemyX[i] = random.randint(0, 735)
                    enemyY[i] = 50
                enemy(enemyX[i], enemyY[i], i)
            if bullet_state == 'Reloading...':
                bulletY -= (bulletY_change + (score / 200))
                firebullet(bulletX, bulletY)
                if bulletY <= 0:
                    if score_m > 1:
                        score_m -= 1
                    else:
                        score_m = 1
                    bullet_state = 'Ready'
                    bulletY = 500
            if halfe is False and image is False:
                if spnum == 0:
                    image = True
            if image:
                screen.blit(spImg, (specialX, specialY))
                specialX += specialX_change
                if specialX >= 736:
                    specialY += specialY_change
                    specialX_change = specialX_change * (-1)
                if specialX <= 0:
                    specialY += specialY_change
                    specialX_change = specialX_change * (-1)
                if specialY >= 420:
                    specialY = 50
                collide_sp = collision(specialX, specialY, bulletX, bulletY)
                if collide_sp:
                    image = False
                    halfe = True
                    coll = True
                    ima = random.choice(images)
                    score_m = score_m
            if halfe is True and spnum < 10000:
                spnum += 1
            else:
                halfe = False
                spnum = 0
            show_score(textX, textY)
            if score_m > 5:
                score_m = 5
            if score_m == 2:
                m = 'OK'
                r = 255
                g = 255
                b = 0
            elif score_m == 3:
                m = 'GOOD'
                r = 0
                g = 0
                b = 255
            elif score_m == 4:
                m = 'YAY'
                r = 255
                g = 0
                b = 255
            elif score_m >= 5:
                m = 'AWESOME'
                r = 0
                g = 255
                b = 0
            else:
                m = 'MEH'
                r = 255
                g = 0
                b = 0
            mu = fon.render('X  ' + str(score_m) + ' : ' + str(m), True, (r, g, b))
            screen.blit(mu, (310, 10))
            state(600, 20)
            player(playerX, playerY)
            imnum = 0
    if end:
        screen.fill((255, 255, 255))
        score_display1 = font.render('YOUR SCORE :     ' + str(score), True, (255, 00, 00))
        screen.blit(score_display1, (200, 100))
        f = open('Highscore.txt', 'r')
        hc = int(f.readline())
        f.close()
        if hc <= score:
            f = open('Highscore.txt', 'w')
            f.write(str(score))
            nhc_display = font.render('NEW HIGH SCORE :     ' + str(score), True, (255, 00, 00))
            screen.blit(nhc_display, (200, 200))
        else:
            hc_display = font.render("HIGHEST SCORE :     " + str(hc), True, (255, 00, 00))
            screen.blit(hc_display, (200, 200))
        time_display = fon.render('TIME TAKEN:  ' + str(d[1]) + '  :  ' + str(d[2]), True, (255, 0, 0))
        screen.blit(time_display, (100, 300))
        draw1()
        draw2()
        for event3 in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event3.type == pygame.QUIT:
                running = False
            if event3.type == pygame.MOUSEBUTTONDOWN:
                if end1.isOver(pos):
                    running = False
                if end2.isOver(pos):
                    score = 0
                    scorea = 3
                    end = False
                    running_1 = True
                    x = datetime.datetime.now()
                    y = x.strftime('%H:%M:%S')
                    score_m = 1
                    for i in range(num):
                        enemyX[i] = random.randint(0, 735)
                        enemyY[i] = 50
            if event3.type == pygame.MOUSEMOTION:
                if end1.isOver(pos):
                    end1.color = (0, 255, 0)
                else:
                    end1.color = (255, 0, 0)
                if end2.isOver(pos):
                    end2.color = (0, 255, 0)
                else:
                    end2.color = (255, 0, 0)
    pygame.display.update()
