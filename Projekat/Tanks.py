from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
from Projekat.Imports import *

class Player(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.image = "Image/tankTop"
        self.image2 = "Image/tank2Top"
        self.lifes = 3
        self.score = 0
        self.playerSpeed = 3
        self.playerSpeed2 = 3
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
                dx -= self.playerSpeed
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
                dx += self.playerSpeed
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
                dy -= self.playerSpeed
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
                dy += self.playerSpeed
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
                dx -= self.playerSpeed2
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
                dx += self.playerSpeed2
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
                dy -= self.playerSpeed2
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
                dy += self.playerSpeed2
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
        self.isAlive = True
        self.timerEnemy = QTimer()
        self.timerEnemy.timeout.connect(self.enemyBulletTemp)
        self.enemyBulletFlag = False
        self.timerEnemyMove = QTimer()
        self.timerEnemyMove.timeout.connect(self.enemyMoveTemp)
        self.enemyMoveFlag = False
        self.enemySpeed = 2
        self.bulletSpeed = 10

    def enemyMoveTemp(self):
        self.enemyMoveFlag = True

    def enemyBulletTemp(self):
        self.enemyBulletFlag = True


    def gameUpdate(self):
        dx = 0
        dy = 0
        canMove = True
        if(self.enemyMoveFlag is True):
            self.rand = randint(0,3)
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
                dx -= self.enemySpeed
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
                dy -= self.enemySpeed
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
                dx += self.enemySpeed
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
                dy += self.enemySpeed
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
                    self.setPos(self.x(), self.y() - player.bulletSpeed)
                elif self.bulletDirection3 == 2:
                    self.setPos(self.x(), self.y() + player.bulletSpeed)
                elif self.bulletDirection3 == 1:
                    self.setPos(self.x() + player.bulletSpeed, self.y())
                elif self.bulletDirection3 == 3:
                    self.setPos(self.x() - player.bulletSpeed, self.y())
                self.frames3 -= 1
                if self.frames3 <= 0:
                    self.active3 = False
                    self.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
