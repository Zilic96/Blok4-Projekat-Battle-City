import sys

import functools

import multiprocessing
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
"""class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Window size
        self.setWindowTitle("Battle City")
        self.setFixedSize(1200, 800)
        # Image as background
        startGameImage = QImage("Image/StartGame.png")
        sStartGameImage = startGameImage.scaled(QSize(1200, 800))
        palette = QPalette()
        palette.setBrush(10, QBrush(sStartGameImage))
        self.setPalette(palette)
        # New Game Button
        self.button = QPushButton('New Game', self)
        self.button.resize(200, 60)
        self.button.move(500, 540)
        self.button.setStyleSheet("background-color: #BD4400")
        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.setWindowTitle("Battle City")
        self.setFixedSize(1200, 800)

        palette = QPalette()
        palette.setBrush(10, Qt.black)
        self.setPalette(palette)
        self.button.deleteLater()

        scene = Scene()
"""


#PODUPLATI METAK I NAPRAVITI PUCANJE LEVO/DESNO
SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 800
PLAYER_SPEED            = 3   # pix/frame
ENEMY_SPEED             = 5
PLAYER_BULLET_X_OFFSETS = 23
PLAYER_BULLET_Y         = 15
BULLET_SPEED            = 10  # pix/frame
BULLET_FRAMES           = 110
FRAME_TIME_MS           = 16  # ms/frame
#ENEMY_BULLET_TIMER      = 25000
MIN_ENEMY_BULLET_TIMER  = 3000
MAX_ENEMY_BULLET_TIMER  = 6000
ENEMY_NUMBER = 7
playerPositions = [(0,0),(0,0)]
enemyPositions = [(0,0)]

maps = []
niz = []
enemies = []
enemyTankNumber = 1
class Player(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.image = "Image/tankTop"
        self.image2 = "Image/tank2Top"
        self.lifes = 3
        self.score = 0
    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
        canMove = True
        if Qt.Key_Left in keys_pressed:
            for b in niz:
                if (self.x() >= b.LeftCor and self.x() <= b.RightCor+3):
                    if ((self.y() >= b.TopCor and self.y() <= b.BotCor) or (self.y() + 50 >= b.TopCor and self.y() + 50 <= b.BotCor) or (self.y() < b.TopCor and self.y() + 50 > b.BotCor)):
                        dx -= 0
                        canMove = False
            for enemy in enemies:
                if (self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+53):
                    if ((self.y() >= enemy[0].y() and self.y() <= enemy[0].y()+50) or (self.y() + 50 >= enemy[0].y() and self.y() + 50 <= enemy[0].y()+50)):
                        dx -= 0
                        canMove = False

            if (self.x() >= playerPositions[1][0] and self.x() <= playerPositions[1][0] + 53):
                if ((self.y() >= playerPositions[1][1] and self.y() <= playerPositions[1][1] + 50) or (self.y() + 50 >= playerPositions[1][1] and self.y() + 50 <= playerPositions[1][1] + 50)):
                    dx -= 0
                    canMove = False

            if self.x() <= 0:
                dx -= 0
            elif (canMove):
                dx -= PLAYER_SPEED
            self.setimage("Image/tankLeft")

        elif Qt.Key_Right in keys_pressed:
            for b in niz:
                if (self.x() + 50 >= b.LeftCor-3 and self.x()+ 50 <= b.RightCor):
                    if ((self.y() >= b.TopCor and self.y() <= b.BotCor) or (self.y() + 50 >= b.TopCor and self.y() + 50 <= b.BotCor) or (self.y() < b.TopCor and self.y() + 50 > b.BotCor)):
                        dx -= 0
                        canMove = False

            for enemy in enemies:
                if (self.x() + 50 >= enemy[0].x()-3 and self.x()+ 50 <= enemy[0].x()+50):
                    if ((self.y() >= enemy[0].y() and self.y() <= enemy[0].y()+50) or (self.y() + 50 >= enemy[0].y() and self.y() + 50 <= enemy[0].y()+50)):
                        dx -= 0
                        canMove = False

            if (self.x() + 50 >= playerPositions[1][0]-3 and self.x() + 50 <= playerPositions[1][0] + 50):
                if ((self.y() >= playerPositions[1][1] and self.y() <= playerPositions[1][1] + 50) or (self.y() + 50 >= playerPositions[1][1] and self.y() + 50 <= playerPositions[1][1] + 50)):
                    dx -= 0
                    canMove = False

            if self.x() >= 941:
                dx -= 0
            elif(canMove):
                dx += PLAYER_SPEED
            self.setimage("Image/tankRight")

        elif Qt.Key_Up in keys_pressed:
            for b in niz:
                if (self.y() <= b.BotCor+3 and self.y() >= b.TopCor):
                    if ((self.x() >= b.LeftCor and self.x() <= b.RightCor) or ( self.x() + 50 >= b.LeftCor and self.x() + 50 <= b.RightCor) or (self.x() < b.LeftCor and self.x() + 50 > b.RightCor)):
                        dy -= 0
                        canMove = False

            for enemy in enemies:
                if (self.y() <= enemy[0].y()+53 and self.y() >= enemy[0].y()):
                    if ((self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+50) or ( self.x() + 50 >= enemy[0].x() and self.x() + 50 <= enemy[0].x()+50)):
                        dy -= 0
                        canMove = False

            if (self.y() <= playerPositions[1][1] + 53 and self.y() >= playerPositions[1][1]):
                if ((self.x() >= playerPositions[1][0] and self.x() <= playerPositions[1][0] + 50) or (self.x() + 50 >= playerPositions[1][0] and self.x() + 50 <= playerPositions[1][0] + 50)):
                    dy -= 0
                    canMove = False

            if self.y() <= 0:
                dy -= 0
            elif (canMove):
                dy -= PLAYER_SPEED
            self.setimage("Image/tankTop")

        elif Qt.Key_Down in keys_pressed:
            for b in niz:
                if (self.y() + 50 <= b.BotCor and self.y() + 50 >= b.TopCor-3):
                    if ((self.x() >= b.LeftCor and self.x() <= b.RightCor) or ( self.x() + 50 >= b.LeftCor and self.x() + 50 <= b.RightCor) or (self.x() < b.LeftCor and self.x() + 50 > b.RightCor)):
                        dy -= 0
                        canMove = False

            for enemy in enemies:
                if (self.y() + 50 <= enemy[0].y()+50 and self.y() + 50 >= enemy[0].y()-3):
                    if ((self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+50) or ( self.x() + 50 >= enemy[0].x() and self.x() + 50 <= enemy[0].x()+50)):
                        dy -= 0
                        canMove = False

            if (self.y() + 50 <= playerPositions[1][1] + 50 and self.y() + 50 >= playerPositions[1][1]-3):
                if ((self.x() >= playerPositions[1][0] and self.x() <= playerPositions[1][0] + 50) or (self.x() + 50 >= playerPositions[1][0] and self.x() + 50 <= playerPositions[1][0] + 50)):
                    dy -= 0
                    canMove = False

            if self.y() >= 746:
                dy -= 0
            elif(canMove):
                dy += PLAYER_SPEED
            self.setimage("Image/tankBottom")
        playerPositions[0] = (self.x()+dx, self.y()+dy)
        self.setPos(self.x()+dx, self.y()+dy)

    def game_update2(self, keys_pressed):
        dx = 0
        dy = 0
        canMove = True
        if Qt.Key_A in keys_pressed:
            for b in niz:
                if (self.x() >= b.LeftCor and self.x() <= b.RightCor+3):
                    if ((self.y() >= b.TopCor and self.y() <= b.BotCor) or (self.y() + 50 >= b.TopCor and self.y() + 50 <= b.BotCor) or (self.y() < b.TopCor and self.y() + 50 > b.BotCor)):
                        dx -= 0
                        canMove = False

            for enemy in enemies:
                if (self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+53):
                    if ((self.y() >= enemy[0].y() and self.y() <= enemy[0].y()+50) or (self.y() + 50 >= enemy[0].y() and self.y() + 50 <= enemy[0].y()+50)):
                        dx -= 0
                        canMove = False

            if (self.x() >= playerPositions[0][0] and self.x() <= playerPositions[0][0] + 53):
                if ((self.y() >= playerPositions[0][1] and self.y() <= playerPositions[0][1] + 50) or (self.y() + 50 >= playerPositions[0][1] and self.y() + 50 <= playerPositions[0][1] + 50)):
                    dx -= 0
                    canMove = False

            if self.x() <= 0 :
                dx -= 0
            elif(canMove):
                dx -= PLAYER_SPEED
            self.setimage2("Image/tank2Left")
        elif Qt.Key_D in keys_pressed:
            for b in niz:
                if (self.x() + 50 >= b.LeftCor-3 and self.x()+ 50 <= b.RightCor):
                    if ((self.y() >= b.TopCor and self.y() <= b.BotCor) or (self.y() + 50 >= b.TopCor and self.y() + 50 <= b.BotCor) or (self.y() < b.TopCor and self.y() + 50 > b.BotCor)):
                        dx -= 0
                        canMove = False

            for enemy in enemies:
                if (self.x() + 50 >= enemy[0].x()-3 and self.x()+ 50 <= enemy[0].x()+50):
                    if ((self.y() >= enemy[0].y() and self.y() <= enemy[0].y()+50) or (self.y() + 50 >= enemy[0].y() and self.y() + 50 <= enemy[0].y()+50)):
                        dx -= 0
                        canMove = False

            if (self.x() + 50 >= playerPositions[0][0]-3 and self.x() + 50 <= playerPositions[0][0] + 50):
                if ((self.y() >= playerPositions[0][1] and self.y() <= playerPositions[0][1] + 50) or (self.y() + 50 >= playerPositions[0][1] and self.y() + 50 <= playerPositions[0][1] + 50)):
                    dx -= 0
                    canMove = False

            if self.x() >= 942:
                dx -= 0
            elif(canMove):
                dx += PLAYER_SPEED
            self.setimage2("Image/tank2Right")
        elif Qt.Key_W in keys_pressed:
            for b in niz:
                if (self.y() <= b.BotCor+3 and self.y() >= b.TopCor):
                    if ((self.x() >= b.LeftCor and self.x() <= b.RightCor) or ( self.x() + 50 >= b.LeftCor and self.x() + 50 <= b.RightCor) or (self.x() < b.LeftCor and self.x() + 50 > b.RightCor)):
                        dy -= 0
                        canMove = False

            for enemy in enemies:
                if (self.y() <= enemy[0].y()+53 and self.y() >= enemy[0].y()):
                    if ((self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+50) or ( self.x() + 50 >= enemy[0].x() and self.x() + 50 <= enemy[0].x()+50)):
                        dy -= 0
                        canMove = False

            if (self.y() <= playerPositions[0][1] + 53 and self.y() >= playerPositions[0][1]):
                if ((self.x() >= playerPositions[0][0] and self.x() <= playerPositions[0][0] + 50) or (self.x() + 50 >= playerPositions[0][0] and self.x() + 50 <= playerPositions[0][0] + 50)):
                    dy -= 0
                    canMove = False

            if self.y() <= 0:
                dy -= 0
            elif(canMove):
                dy -= PLAYER_SPEED
            self.setimage2("Image/tank2Top")
        elif Qt.Key_S in keys_pressed:
            for b in niz:
                if (self.y() + 50 <= b.BotCor and self.y() + 50 >= b.TopCor-3):
                    if ((self.x() >= b.LeftCor and self.x() <= b.RightCor) or ( self.x() + 50 >= b.LeftCor and self.x() + 50 <= b.RightCor) or (self.x() < b.LeftCor and self.x() + 50 > b.RightCor)):
                        dy -= 0
                        canMove = False

            for enemy in enemies:
                if (self.y() + 50 <= enemy[0].y()+50 and self.y() + 50 >= enemy[0].y()-3):
                    if ((self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+50) or ( self.x() + 50 >= enemy[0].x() and self.x() + 50 <= enemy[0].x()+50)):
                        dy -= 0
                        canMove = False

            if (self.y() + 50 <= playerPositions[0][1] + 50 and self.y() + 50 >= playerPositions[0][1]-3):
                if ((self.x() >= playerPositions[0][0] and self.x() <= playerPositions[0][0] + 50) or (self.x() + 50 >= playerPositions[0][0] and self.x() + 50 <= playerPositions[0][0] + 50)):
                    dy -= 0
                    canMove = False

            if self.y() >= 746:
                dy -= 0
            elif(canMove):
                dy += PLAYER_SPEED
            self.setimage2("Image/tank2Bottom")
        playerPositions[1] = (self.x() + dx, self.y() + dy)
        self.setPos(self.x()+dx, self.y()+dy)

    def setimage(self, image):
        self.image = image
        self.setPixmap(QPixmap(image))

    def getimage(self):
        return self.image

    def setimage2(self, image2):
        self.image2 = image2
        self.setPixmap(QPixmap(image2))

    def getimage2(self):
        return self.image2

class Enemy(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.rand = 3
        #self.temp = 0
        self.isAlive = True
        self.timerEnemy = QTimer()
        self.timerEnemy.timeout.connect(self.enemyBulletTemp)
        self.enemyBulletFlag = False
        self.timerEnemyMove = QTimer()
        self.timerEnemyMove.timeout.connect(self.enemyMoveTemp)
        self.enemyMoveFlag = False
        #self.timerEnemy.start(ENEMY_BULLET_TIMER)

    def enemyMoveTemp(self):
        self.enemyMoveFlag = True

    def enemyBulletTemp(self):
        self.enemyBulletFlag = True


    def gameUpdate(self):
        #self.temp = self.temp +1
        dx = 0
        dy = 0
        canMove = True
        if(self.enemyMoveFlag is True):
            self.rand = randint(0,3)
            #self.temp = 0
            self.enemyMoveFlag = False
        if(self.rand == 0):
            for b in niz:
                if (self.x() >= b.LeftCor and self.x() <= b.RightCor+3):
                    if ((self.y() >= b.TopCor and self.y() <= b.BotCor) or (self.y() + 50 >= b.TopCor and self.y() + 50 <= b.BotCor) or (self.y() < b.TopCor and self.y() + 50 > b.BotCor)):
                        dx -= 0
                        canMove = False


            for enemy in enemies:
                if(self.x() != enemy[0].x() and self.x() != enemy[0].y()):
                    if (self.x() >= enemy[0].x() and self.x() <= enemy[0].x() + 53):
                        if ((self.y() >= enemy[0].y() and self.y() <= enemy[0].y()+50) or (self.y() + 50 >= enemy[0].y() and self.y() + 50 <= enemy[0].y()+50)):
                            dx -= 0
                            canMove = False

            if (self.x() >= playerPositions[0][0] and self.x() <= playerPositions[0][0] + 53):
                if ((self.y() >= playerPositions[0][1] and self.y() <= playerPositions[0][1] + 50) or (self.y() + 50 >= playerPositions[0][1] and self.y() + 50 <= playerPositions[0][1] + 50)):
                    dx -= 0
                    canMove = False

            if (self.x() >= playerPositions[1][0] and self.x() <= playerPositions[1][0] + 53):
                if ((self.y() >= playerPositions[1][1] and self.y() <= playerPositions[1][1] + 50) or (self.y() + 50 >= playerPositions[1][1] and self.y() + 50 <= playerPositions[1][1] + 50)):
                    dx -= 0
                    canMove = False


            if self.x() <= 0:
                dx -= 0
            elif (canMove):
                dx -= ENEMY_SPEED
            #enemyPosition[1] = (self.x() + dx, self.y() + dy)
            self.setimage("Image/enemyTankLeft")
            self.setPos(self.x() + dx, self.y() + dy)
        if (self.rand == 1):
            for b in niz:
                if (self.y() <= b.BotCor+3 and self.y() >= b.TopCor):
                    if ((self.x() >= b.LeftCor and self.x() <= b.RightCor) or ( self.x() + 50 >= b.LeftCor and self.x() + 50 <= b.RightCor) or (self.x() < b.LeftCor and self.x() + 50 > b.RightCor)):
                        dy -= 0
                        canMove = False

            for enemy in enemies:
                if (self.x() != enemy[0].x() and self.x() != enemy[0].y()):
                    if (self.y() <= enemy[0].y()+53 and self.y() >= enemy[0].y()):
                        if ((self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+50) or ( self.x() + 50 >= enemy[0].x() and self.x() + 50 <= enemy[0].x()+50)):
                            dy -= 0
                            canMove = False

            if (self.y() <= playerPositions[0][1]+53 and self.y() >= playerPositions[0][1]):
                        if ((self.x() >= playerPositions[0][0] and self.x() <= playerPositions[0][0]+50) or ( self.x() + 50 >= playerPositions[0][0] and self.x() + 50 <= playerPositions[0][0]+50)):
                            dy -= 0
                            canMove = False

            if (self.y() <= playerPositions[1][1]+53 and self.y() >= playerPositions[1][1]):
                        if ((self.x() >= playerPositions[1][0] and self.x() <= playerPositions[1][0]+50) or ( self.x() + 50 >= playerPositions[1][0] and self.x() + 50 <= playerPositions[1][0]+50)):
                            dy -= 0
                            canMove = False

            if self.y() <= 0:
                dy -= 0
            elif(canMove):
                dy -= ENEMY_SPEED
            # enemyPosition[1] = (self.x() + dx, self.y() + dy)
            self.setimage("Image/enemyTankTop")
            self.setPos(self.x() + dx, self.y() + dy)
        if (self.rand == 2):
            for b in niz:
                if (self.x() + 50 >= b.LeftCor-3 and self.x()+ 50 <= b.RightCor):
                    if ((self.y() >= b.TopCor and self.y() <= b.BotCor) or (self.y() + 50 >= b.TopCor and self.y() + 50 <= b.BotCor) or (self.y() < b.TopCor and self.y() + 50 > b.BotCor)):
                        dx -= 0
                        canMove = False

            for enemy in enemies:
                if (self.x() != enemy[0].x() and self.x() != enemy[0].y()):
                    if (self.x() + 50 >= enemy[0].x()-3 and self.x() + 50 <= enemy[0].x()+50):
                        if ((self.y() >= enemy[0].y() and self.y() <= enemy[0].y()+50) or (self.y() + 50 >= enemy[0].y() and self.y() + 50 <= enemy[0].y()+50)):
                            dx -= 0
                            canMove = False

            if (self.x() + 50 >= playerPositions[0][0]-3 and self.x() + 50 <= playerPositions[0][0] + 50):
                if ((self.y() >= playerPositions[0][1] and self.y() <= playerPositions[0][1] + 50) or (self.y() + 50 >= playerPositions[0][1] and self.y() + 50 <= playerPositions[0][1] + 50)):
                    dx -= 0
                    canMove = False

            if (self.x() + 50 >= playerPositions[1][0]-3 and self.x() + 50 <= playerPositions[1][0] + 50):
                if ((self.y() >= playerPositions[1][1] and self.y() <= playerPositions[1][1] + 50) or (self.y() + 50 >= playerPositions[1][1] and self.y() + 50 <= playerPositions[1][1] + 50)):
                    dx -= 0
                    canMove = False

            if self.x() >= 942:
                dx -= 0
            elif(canMove):
                dx += ENEMY_SPEED
            # enemyPosition[1] = (self.x() + dx, self.y() + dy)
            self.setimage("Image/enemyTankRight")
            self.setPos(self.x() + dx, self.y() + dy)
        if (self.rand == 3):
            for b in niz:
                if (self.y() + 50 <= b.BotCor and self.y() + 50 >= b.TopCor-3):
                    if ((self.x() >= b.LeftCor and self.x() <= b.RightCor) or ( self.x() + 50 >= b.LeftCor and self.x() + 50 <= b.RightCor) or (self.x() < b.LeftCor and self.x() + 50 > b.RightCor)):
                        dy -= 0
                        canMove = False

            for enemy in enemies:
                if (self.x() != enemy[0].x() and self.x() != enemy[0].y()):
                    if (self.y() + 50 <= enemy[0].y()+50 and self.y() + 50 >= enemy[0].y()-3):
                        if ((self.x() >= enemy[0].x() and self.x() <= enemy[0].x()+50) or (self.x() + 50 >= enemy[0].x() and self.x() + 50 <= enemy[0].x()+50)):
                            dy -= 0
                            canMove = False

            if (self.y() + 50 <= playerPositions[0][1] + 50 and self.y() + 50 >= playerPositions[0][1]-3):
                if ((self.x() >= playerPositions[0][0] and self.x() <= playerPositions[0][0] + 50) or (self.x() + 50 >= playerPositions[0][0] and self.x() + 50 <= playerPositions[0][0] + 50)):
                    dy -= 0
                    canMove = False

            if (self.y() + 50 <= playerPositions[1][1] + 50 and self.y() + 50 >= playerPositions[1][1]-3):
                if ((self.x() >= playerPositions[1][0] and self.x() <= playerPositions[1][0] + 50) or (self.x() + 50 >= playerPositions[1][0] and self.x() + 50 <= playerPositions[1][0] + 50)):
                    dy -= 0
                    canMove = False

            if self.y() >= 746:
                dy -= 0
            elif(canMove):
                dy += ENEMY_SPEED
            # enemyPosition[1] = (self.x() + dx, self.y() + dy)
            self.setimage("Image/enemyTankBottom")
            self.setPos(self.x() + dx, self.y() + dy)
        enemyPositions[0] = ((self.x()+dx , self.y()+dy))

    def setimage(self, image):
        self.image = image
        self.setPixmap(QPixmap(image))

    def getimage(self):
        return self.image

class Bullet(QGraphicsPixmapItem):
    def __init__(self, offset_x, offset_y, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.imageBullet = "Image/bulet"
        self.imageBullet2 = "Image/bulet"
        self.imageBullet3 = "Image/bulet"
        self.setPixmap(QPixmap(self.imageBullet))
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.active = False
        self.active2 = False
        self.active3 = False
        self.frames = 0
        self.frames2 = 0
        self.frames3 = 0
        self.bulletDirection = 0
        self.bulletDirection2 = 0
        self.bulletDirection3 = 0
        #self.enemyBulletFlag = False

    def setBulletImage(self, image):
        self.imageBullet = image
        self.setPixmap(QPixmap(self.imageBullet))

    def setBulletImage2(self, image):
        self.imageBullet2 = image
        self.setPixmap(QPixmap(self.imageBullet2))

    def setBulletImage3(self, image):
        self.imageBullet3 = image
        self.setPixmap(QPixmap(self.imageBullet3))

    def game_update(self, keys_pressed, player):
        if not self.active:
            if (Qt.Key_Space in keys_pressed and player.lifes > 0):
                if player.getimage() == "Image/tankTop":
                    self.setBulletImage("Image/bulet")
                    self.bulletDirection = 0
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage() == "Image/tankRight":
                    self.setBulletImage("Image/buletHorizontal")
                    self.bulletDirection = 1
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y+8)
                elif player.getimage() == "Image/tankBottom":
                    self.setBulletImage("Image/bulet")
                    self.bulletDirection = 2
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage() == "Image/tankLeft":
                    self.setBulletImage("Image/buletHorizontal")
                    self.bulletDirection = 3
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y+8)

                self.active = True
                self.frames = BULLET_FRAMES

        else:
            if self.bulletDirection == 0:
                self.setPos(self.x(),self.y()-BULLET_SPEED)
            elif self.bulletDirection == 2:
                self.setPos(self.x(), self.y() + BULLET_SPEED)
            elif self.bulletDirection == 1:
                self.setPos(self.x() + BULLET_SPEED, self.y())
            elif self.bulletDirection == 3:
                self.setPos(self.x() - BULLET_SPEED, self.y())
            self.frames -= 1
            if self.frames <= 0:
                self.active = False
                self.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)

    def game_update2(self, keys_pressed, player):
        if not self.active2:
            if (Qt.Key_Control in keys_pressed and player.lifes > 0):
                if player.getimage2() == "Image/tank2Top":
                    self.setBulletImage2("Image/bulet")
                    self.bulletDirection2 = 0
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage2() == "Image/tank2Right":
                    self.setBulletImage2("Image/buletHorizontal")
                    self.bulletDirection2 = 1
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y+9)
                elif player.getimage2() == "Image/tank2Bottom":
                    self.setBulletImage2("Image/bulet")
                    self.bulletDirection2 = 2
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage2() == "Image/tank2Left":
                    self.setBulletImage2("Image/buletHorizontal")
                    self.bulletDirection2 = 3
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y+9)

                self.active2 = True
                self.frames2 = BULLET_FRAMES

        else:
            if self.bulletDirection2 == 0:
                self.setPos(self.x(),self.y()-BULLET_SPEED)
            elif self.bulletDirection2 == 2:
                self.setPos(self.x(), self.y() + BULLET_SPEED)
            elif self.bulletDirection2 == 1:
                self.setPos(self.x() + BULLET_SPEED, self.y())
            elif self.bulletDirection2 == 3:
                self.setPos(self.x() - BULLET_SPEED, self.y())
            self.frames2 -= 1
            if self.frames2 <= 0:
                self.active2 = False
                self.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)

    def game_update3(self, player, isGameOver):
            if not self.active3:
                 if (True and isGameOver is False and player.enemyBulletFlag is True and player.isAlive is True):
                    player.enemyBulletFlag = False
                    if player.getimage() == "Image/enemyTankTop":
                        self.setBulletImage3("Image/bulet")
                        self.bulletDirection3 = 0
                        self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                    elif player.getimage() == "Image/enemyTankRight":
                        self.setBulletImage3("Image/buletHorizontal")
                        self.bulletDirection3= 1
                        self.setPos(player.x() + self.offset_x, player.y() + self.offset_y + 9)
                    elif player.getimage() == "Image/enemyTankBottom":
                        self.setBulletImage3("Image/bulet")
                        self.bulletDirection3 = 2
                        self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                    elif player.getimage() == "Image/enemyTankLeft":
                        self.setBulletImage3("Image/buletHorizontal")
                        self.bulletDirection3 = 3
                        self.setPos(player.x() + self.offset_x, player.y() + self.offset_y + 9)

                    self.active3 = True
                    self.frames3 = BULLET_FRAMES

            else:
                if self.bulletDirection3 == 0:
                    self.setPos(self.x(), self.y() - BULLET_SPEED)
                elif self.bulletDirection3 == 2:
                    self.setPos(self.x(), self.y() + BULLET_SPEED)
                elif self.bulletDirection3 == 1:
                    self.setPos(self.x() + BULLET_SPEED, self.y())
                elif self.bulletDirection3 == 3:
                    self.setPos(self.x() - BULLET_SPEED, self.y())
                self.frames3 -= 1
                if self.frames3 <= 0:
                    self.active3 = False
                    self.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)


class Brick(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.LeftCor = 0
        self.RightCor = 0
        self.TopCor = 0
        self.BotCor = 0
        self.isEagel = False

class Eagle(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.LeftCor = 0
        self.RightCor = 0
        self.TopCor = 0
        self.BotCor = 0
        self.isEagel = True

class PowerUp(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap(image))




class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        self.enemyCount = ENEMY_NUMBER - 6

        self.bg = QGraphicsRectItem()
        self.bg.setRect(-1,-1,992,SCREEN_HEIGHT)
        self.bg.setBrush(QBrush(Qt.black))
        self.addItem(self.bg)
        self.level = 1

        self.powerUpTimer = 0

        self.gameLevel = randint(0,2)
        self.gamelevelString = "maps"+str(self.gameLevel)+".txt"
        f = open(self.gamelevelString, 'r')
        maps = [[int(num) for num in line.split(',')] for line in f]

        """self.t = Enemy("Image/enemyTankTop")
        self.t.setPos(1, 1)
        self.addItem(self.t)
        self.update()
        self.isGameOver = False"""



        row = 0
        col = 0
        for i in maps:
            col = 0
            for j in i:
                if(j==1):
                    brick = Brick("Image/brick")
                    brick.setPos(col * 32, row * 32)
                    self.addItem(brick)
                    self.update()
                    brick.LeftCor = col * 32
                    brick.RightCor = col * 32 + 32
                    brick.TopCor = row * 32
                    brick.BotCor = row * 32 + 32

                    niz.append(brick)

                elif(j==2):
                    eagle = Eagle("Image/eagle")
                    eagle.setPos(col * 32, row * 32)
                    self.addItem(eagle)
                    self.update()
                    eagle.LeftCor = col * 32
                    eagle.RightCor = col * 32 + 96
                    eagle.TopCor = row * 32
                    eagle.BotCor = row * 32 + 64

                    niz.append(eagle)

                col = col + 1
            row = row + 1

        self.player1 = Player("Image/tankTop")
        self.player1.setPos((SCREEN_WIDTH-self.player1.pixmap().width())/5,
                           (SCREEN_HEIGHT-self.player1.pixmap().height())/1)
        self.player2 = Player("Image/tank2Top")
        self.player2.setPos((SCREEN_WIDTH - self.player2.pixmap().width()) / 3*2,
                            (SCREEN_HEIGHT - self.player2.pixmap().height()) / 1)

        self.bullet = Bullet(PLAYER_BULLET_X_OFFSETS,PLAYER_BULLET_Y)
        self.bullet.setPos(-1,-1)
        self.addItem(self.bullet)

        self.bullet2 = Bullet(PLAYER_BULLET_X_OFFSETS, PLAYER_BULLET_Y)
        self.bullet2.setPos(-1, -1)
        self.addItem(self.bullet2)

        """"""

        self.addItem(self.player1)
        self.addItem(self.player2)

        #Stat label
        self.label = QGraphicsRectItem()
        self.label.setRect(992,0,SCREEN_WIDTH, SCREEN_HEIGHT)
        self.label.setBrush(QBrush(Qt.gray))
        self.addItem(self.label)

        #Stats
        self.p1 = QGraphicsPixmapItem()
        self.p1.setPos(1020, 50)
        self.p1.setPixmap(QPixmap("Image/P1"))
        self.addItem(self.p1)
        self.player1Lifes = QGraphicsPixmapItem()
        self.player1Lifes.setPos(1070,50)
        if self.player1.lifes == 3:
            self.player1Lifes.setPixmap(QPixmap("Image/3lifes"))
        elif self.player1.lifes == 2:
            self.player1Lifes.setPixmap(QPixmap("Image/2lifes"))
        elif self.player1.lifes == 1:
            self.player1Lifes.setPixmap(QPixmap("Image/1lif"))
        self.addItem(self.player1Lifes)

        self.p2 = QGraphicsPixmapItem()
        self.p2.setPos(1020, 150)
        self.p2.setPixmap(QPixmap("Image/P2"))
        self.addItem(self.p2)
        self.player2Lifes = QGraphicsPixmapItem()
        self.player2Lifes.setPos(1070, 150)
        if self.player2.lifes == 3:
            self.player2Lifes.setPixmap(QPixmap("Image/3lifes"))
        elif self.player2.lifes == 2:
            self.player2Lifes.setPixmap(QPixmap("Image/2lifes"))
        elif self.player2.lifes == 1:
            self.player2Lifes.setPixmap(QPixmap("Image/1lif"))
        self.addItem(self.player2Lifes)

        self.levelFlag = QGraphicsPixmapItem()
        self.levelFlag.setPos(1020, 750)
        self.levelFlag.setPixmap(QPixmap("Image/levelFlag"))
        self.addItem(self.levelFlag)

        self.levelNumberFont = QFont()
        self.levelNumberFont.setPixelSize(25)
        self.levelNumberFont.setBold(1)
        self.levelNumber = QGraphicsSimpleTextItem()
        self.levelNumber.setText(str(self.level))
        self.levelNumber.setPos(1060,755)
        self.levelNumber.setBrush(QBrush(Qt.black))
        self.levelNumber.setFont(self.levelNumberFont)
        self.addItem(self.levelNumber)

        self.player1ScoreFont = QFont()
        self.player1ScoreFont.setPixelSize(35)
        self.player1ScoreFont.setBold(1)
        self.player1ScoreLabel = QGraphicsSimpleTextItem()
        self.player1ScoreLabel.setText("P1 : " + str(self.player1.score))
        self.player1ScoreLabel.setPos(1020, 230)
        self.player1ScoreLabel.setBrush(QBrush(Qt.black))
        self.player1ScoreLabel.setFont(self.player1ScoreFont)
        self.addItem(self.player1ScoreLabel)

        self.player2ScoreFont = QFont()
        self.player2ScoreFont.setPixelSize(35)
        self.player2ScoreFont.setBold(1)
        self.player2ScoreLabel = QGraphicsSimpleTextItem()
        self.player2ScoreLabel.setText("P2 : " + str(self.player1.score))
        self.player2ScoreLabel.setPos(1020, 290)
        self.player2ScoreLabel.setBrush(QBrush(Qt.black))
        self.player2ScoreLabel.setFont(self.player2ScoreFont)
        self.addItem(self.player2ScoreLabel)


        self.enemyNumberPic = QGraphicsPixmapItem()
        self.enemyNumberPic.setPos(1020, 400)
        self.enemyNumberPic.setPixmap(QPixmap("Image/enemyTankTop"))
        self.addItem(self.enemyNumberPic)

        """"""
        # Timer for enemy bullet

        """self.timerEnemy = QTimer()
        self.timerEnemy.timeout.connect(self.enemyBulletTemp)
        self.timerEnemy.start(ENEMY_BULLET_TIMER)"""
        """"""

        self.enemyNumber = 6

        self.thread = QThread()
        self.moveToThread(self.thread)
        for i in range(0,6):
            self.thread.started.connect(self.createEnemy)
        self.thread.start()

        #PowerUp
        self.powerUpQTimer = QTimer()
        self.powerUpQTimer.timeout.connect(self.powerUpScene)
        self.powerUpQTimer.start(4000)

        self.powerUpImage = QGraphicsPixmapItem()
        self.powerUpName = ""

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0 ,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.view.setWindowTitle("Battle City")



    #@pyqtSlot()
    def createEnemy(self):
        global enemyTankNumber
        self.t = Enemy("Image/enemyTankTop")
        self.t.setPos(enemyTankNumber*120, 1)
        self.addItem(self.t)
        self.update()
        self.isGameOver = False

        self.enemyBullet = Bullet(PLAYER_BULLET_X_OFFSETS, PLAYER_BULLET_Y)
        self.enemyBullet.setPos(-1, -1)
        self.addItem(self.enemyBullet)

        self.t.timerEnemy.start(randint(MIN_ENEMY_BULLET_TIMER,MAX_ENEMY_BULLET_TIMER))
        self.t.timerEnemyMove.start(randint(2000,5000))
        enemies.append((self.t, self.enemyBullet))

        enemyTankNumber = enemyTankNumber + 1
        if (enemyTankNumber == 7):
            enemyTankNumber = 1

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.powerUpTimer = self.powerUpTimer + 1
        #print(self.powerUpTimer)
        self.game_update()
        self.update()

    def game_update(self):
        #self.powerUpScene()
        #Player 1 killing bricks
        if (self.bullet.x() + 8 >= 985):
            self.removeItem(self.bullet)
            self.bullet.setPos(-5, -5)
            self.bullet.active = False
        elif (self.bullet.x() < 0):
            self.removeItem(self.bullet)
            self.bullet.setPos(-5, -5)
            self.bullet.active = False
        elif (self.bullet.y() < 0):
            self.removeItem(self.bullet)
            self.bullet.setPos(-5, -5)
            self.bullet.active = False
        elif (self.bullet.y() >= 800):
            self.removeItem(self.bullet)
            self.bullet.setPos(-5, -5)
            self.bullet.active = False
        for brick in niz:
            if(self.bullet.x() >= brick.LeftCor and self.bullet.x() <= brick.RightCor and self.bullet.y() >= brick.TopCor and self.bullet.y() <= brick.BotCor):
                if(brick.isEagel is True):
                    self.gameOver()
                brick.setPixmap(QPixmap("Image/P1"))
                self.removeItem(brick)
                niz.remove(brick)
                self.removeItem(self.bullet)
                self.bullet.active = False
                self.bullet.setPos(-5, -5)
        self.player1.game_update(self.keys_pressed)
        self.bullet.game_update(self.keys_pressed, self.player1)
        if(self.bullet.active):
            self.addItem(self.bullet)

        # Player 2 killing bricks
        if (self.bullet2.x() + 8 >= 985):
            self.removeItem(self.bullet2)
            self.bullet2.setPos(-5, -5)
            self.bullet2.active2 = False
        elif (self.bullet2.x() < 0):
            self.removeItem(self.bullet2)
            self.bullet2.setPos(-5, -5)
            self.bullet2.active2 = False
        elif (self.bullet2.y() < 0):
            self.removeItem(self.bullet2)
            self.bullet2.setPos(-5, -5)
            self.bullet2.active2 = False
        elif (self.bullet2.y() >= 800):
            self.removeItem(self.bullet2)
            self.bullet2.setPos(-5, -5)
            self.bullet2.active2 = False
        for brick in niz:
            if (self.bullet2.x() >= brick.LeftCor and self.bullet2.x() <= brick.RightCor and self.bullet2.y() >= brick.TopCor and self.bullet2.y() <= brick.BotCor):
                if (brick.isEagel is True):
                    self.gameOver()
                self.removeItem(brick)
                niz.remove(brick)
                self.removeItem(self.bullet2)
                self.bullet2.active2 = False
                self.bullet2.setPos(-5, -5)
        self.player2.game_update2(self.keys_pressed)
        self.bullet2.game_update2(self.keys_pressed, self.player2)
        if (self.bullet2.active2):
            self.addItem(self.bullet2)

        # Enemy killing bricks
        for enemy in enemies:
            if (enemy[1].x() + 8 >= 985):
                self.removeItem(enemy[1])
                enemy[1].setPos(-5, -5)
                enemy[1].active3 = False
            elif (enemy[1].x() < 0):
                self.removeItem(enemy[1])
                enemy[1].setPos(-5, -5)
                enemy[1].active3 = False
            elif (enemy[1].y() < 0):
                self.removeItem(enemy[1])
                enemy[1].setPos(-5, -5)
                enemy[1].active3 = False
            elif (enemy[1].y() >= 800):
                self.removeItem(enemy[1])
                enemy[1].setPos(-5, -5)
                enemy[1].active3 = False
            #Player 1
            if (enemy[1].x() <= self.player1.x()+50 and enemy[1].x() >= self.player1.x() and enemy[1].y() <= self.player1.y()+50 and enemy[1].y() >= self.player1.y() and enemy[0].isAlive is True and self.player1.lifes > 0):
                self.player1.lifes = self.player1.lifes - 1
                enemy[1].setPos(-5, -5)
                if(self.player1.lifes == 2):
                    self.player1Lifes.setPixmap(QPixmap("Image/2lifes"))
                elif(self.player1.lifes == 1):
                    self.player1Lifes.setPixmap(QPixmap("Image/1life"))
                if(self.player1.lifes >= 1):
                    self.removeItem(enemy[1])
                    enemy[1].active3 = False
                    self.player1.setPos((SCREEN_WIDTH-self.player1.pixmap().width())/5,(SCREEN_HEIGHT-self.player1.pixmap().height())/1)
                else:
                    self.removeItem(self.player1Lifes)
                    self.player1.lifes = 0
                    self.removeItem(self.player1)
                    self.removeItem(self.bullet)
                    self.player1.setPos(-60, -60)
                    self.removeItem(enemy[1])
                    enemy[1].setPos(-5,-5)
                    self.bullet.active = False
            #Player2
            if (enemy[1].x() <= self.player2.x()+50 and enemy[1].x() >= self.player2.x() and enemy[1].y() <= self.player2.y()+50 and enemy[1].y() >= self.player2.y() and enemy[0].isAlive is True and self.player2.lifes > 0):
                self.player2.lifes = self.player2.lifes - 1
                enemy[1].setPos(-5, -5)
                if (self.player2.lifes == 2):
                    self.player2Lifes.setPixmap(QPixmap("Image/2lifes"))
                elif (self.player2.lifes == 1):
                    self.player2Lifes.setPixmap(QPixmap("Image/1life"))
                if(self.player2.lifes >= 1):
                    self.removeItem(enemy[1])
                    enemy[1].active3 = False

                    self.player2.setPos((SCREEN_WIDTH - self.player2.pixmap().width()) / 3*2,(SCREEN_HEIGHT - self.player2.pixmap().height()) / 1)
                else:
                    self.removeItem(self.player2Lifes)
                    self.player2.lifes = 0
                    self.removeItem(self.player2)
                    self.removeItem(self.bullet2)
                    self.player2.setPos(-60,-60)
                    self.removeItem(enemy[1])
                    enemy[1].setPos(-5, -5)
                    self.bullet2.active = False

        #Player 1 killing enemy
        for enemyPlayer1 in enemies:
            if (self.bullet.x() <= enemyPlayer1[0].x()+50 and self.bullet.x() >= enemyPlayer1[0].x() and self.bullet.y() <= enemyPlayer1[0].y()+50 and self.bullet.y() >= enemyPlayer1[0].y() and enemyPlayer1[0].isAlive is True):
                self.player1.score = self.player1.score + 100
                self.player1ScoreLabel.setText("P1 : " + str(self.player1.score))
                self.removeItem(enemyPlayer1[0])
                self.removeItem(self.bullet)
                self.removeItem(enemyPlayer1[1])
                self.bullet.active = False
                enemyPlayer1[1].active3 = False
                enemyPlayer1[0].isAlive = False
                enemies.remove(enemyPlayer1)
                self.bullet.setPos(-5,-5)
                if(self.enemyCount > 0):
                    self.createEnemy()
                    self.enemyCount = self.enemyCount - 1

        #Player1 picks power up
        if(self.player1.x() <= self.powerUpImage.x()+50 and self.player1.x() >= self.powerUpImage.x() and self.player1.y() >= self.powerUpImage.y() and self.player1.y() <= self.powerUpImage.y()+50 or (self.player1.x()+50 <= self.powerUpImage.x()+50 and self.player1.x()+50 >= self.powerUpImage.x() and self.player1.y()+50 >= self.powerUpImage.y() and self.player1.y()+50 <= self.powerUpImage.y()+50)):
            self.removeItem(self.powerUpImage)
            self.powerUpImage.setPos(-50,-50)
            if(self.powerUpName == "Image/extraLife"):
                if(self.player1.lifes == 2):
                    self.player1.lifes = self.player1.lifes + 1
                    self.player1Lifes.setPixmap(QPixmap("Image/3lifes"))

                elif(self.player1.lifes == 1):
                    self.player1.lifes = self.player1.lifes + 1
                    self.player1Lifes.setPixmap(QPixmap("Image/2lifes"))


            print("NECA KUCKA")
            #self.powerUpQTimer.disconnect()
            #self.powerUpQTimer.timeout.connect(self.kurac)
            self.powerUpQTimer.start(1000)
            #print(str(self.powerUpQTimer.isActive()))

        # Player 2 killing enemy
        for enemyPlayer2 in enemies:
            if (self.bullet2.x() <= enemyPlayer2[0].x() + 50 and self.bullet2.x() >= enemyPlayer2[0].x() and self.bullet2.y() <= enemyPlayer2[0].y() + 50 and self.bullet2.y() >= enemyPlayer2[0].y() and enemyPlayer2[0].isAlive is True):
                self.player2.score = self.player2.score + 100
                self.player2ScoreLabel.setText("P2 : " + str(self.player2.score))
                self.removeItem(enemyPlayer2[0])
                self.removeItem(self.bullet2)
                self.removeItem(enemyPlayer2[1])
                self.bullet2.active2 = False
                enemyPlayer2[1].active3 = False
                enemyPlayer2[0].isAlive = False
                enemies.remove(enemyPlayer2)
                self.bullet2.setPos(-5, -5)

        #Game over, player1.lifev and player2.lifes = 0!
        if(self.player1.lifes == 0 and self.player2.lifes == 0):
            self.gameOver()

        for enemyBricks in enemies:
            for brick in niz:
                if (enemyBricks[1].x() >= brick.LeftCor and enemyBricks[1].x() <= brick.RightCor and enemyBricks[1].y() >= brick.TopCor and enemyBricks[1].y() <= brick.BotCor):
                    if (brick.isEagel is True):
                        self.gameOver()
                    self.removeItem(brick)
                    niz.remove(brick)
                    self.removeItem(enemyBricks[1])
                    enemyBricks[1].active3 = False
                    enemyBricks[1].setPos(-5, -5)

        for enemy in enemies:
            enemy[0].gameUpdate()
            enemy[1].game_update3(enemy[0], self.isGameOver)
            if (enemy[1].active3):
                self.addItem(enemy[1])
        #self.enemyBullet.game_update3(self.t, self.isGameOver)

        #if (self.enemyBullet.active3):
            #self.addItem(self.enemyBullet)

    """def enemyBulletTemp(self):
        for enemy in enemies:
            enemy[1].enemyBulletFlag = True"""

    def powerUpScene(self):
        print("DJOKARA FUKSA GLUPAVA")
        pool = multiprocessing.Pool(processes=1)
        result = pool.apply_async(powerUp, (910, SCREEN_HEIGHT - 50))
        self.cords = result.get(timeout=0.2)
        pool.close()

        self.powerUpImage.setPos(self.cords[0], self.cords[1])
        print(str(self.powerUpTimer))
        if (self.cords[2] == 0):
            self.powerUpName = "Image/extraLife"
            self.powerUpImage.setPixmap(QPixmap("Image/extraLife"))
        elif (self.cords[2] == 1):
            self.powerUpName = "Image/slow"
            self.powerUpImage.setPixmap(QPixmap("Image/slow"))
        self.addItem(self.powerUpImage)
        self.powerUpQTimer.stop()

    def gameOver(self):
        self.timer.stop()
        self.powerUpQTimer.stop()
        self.isGameOver = True
        startGameImage = QImage("Image/GameOver.png")
        sStartGameImage = startGameImage.scaled(QSize(1200, 800))
        self.bgGameOver = QGraphicsPixmapItem()
        self.bgGameOver.setPos(0, 0)
        self.bgGameOver.setPixmap(QPixmap(sStartGameImage))
        self.addItem(self.bgGameOver)

        self.removeItem(self.enemyBullet)
        self.enemyBullet.active3 = False
        self.removeItem(self.bullet)
        self.bullet.active = False
        self.player1.lifes = 0
        self.removeItem(self.bullet2)
        self.bullet2.active2 = False
        self.player2.lifes = 0

        self.playerWinsPic = QGraphicsPixmapItem()
        self.playerWinsPic.setPos(450, 600)
        if(self.player1.score > self.player2.score):
            self.playerWinsPic.setPixmap(QPixmap("Image/player1Wins"))
        elif(self.player2.score > self.player1.score):
            self.playerWinsPic.setPixmap(QPixmap("Image/player2Wins"))
        else:
            self.playerWinsPic.setPos(570, 600)
            self.playerWinsPic.setPixmap(QPixmap("Image/tie"))
        self.addItem(self.playerWinsPic)



def powerUp(a, b):
    x = randint(0,a)
    y = randint(0,b)
    z = randint(0,1)
    #print(str(z))
    cords = [x, y, z]
    return cords


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scene()
    sys.exit(app.exec_())
