from Projekat.MapItems import *
from Projekat.Tanks import *
import sys

import multiprocessing
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
import _thread





class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        self.enemyCount = ENEMY_NUMBER - 6

        self.bg = QGraphicsRectItem()
        self.bg.setRect(-1,-1,992,SCREEN_HEIGHT)
        self.bg.setBrush(QBrush(Qt.black))
        self.addItem(self.bg)
        self.level = 1

        self.powerUpTimer = 0

        pool = multiprocessing.Pool(processes=1)
        result = pool.apply_async(loadMap, ())
        maps = result.get(timeout=1)
        pool.close()

        self.enemySpeedScene = 2
        self.enemyBulletSpeed = 10
        self.minEnemyBulletTimer = 3000
        self.maxEnemyBulletTimer = 6000

        self.temp = []

        row = 0
        col = 0
        for i in maps:
            col = 0
            for j in i:
                if(j==1):
                    brick = Brick("Image/brick")
                    brick.setPos(col * 32, row * 32)
                    self.addItem(brick)
                    brick.LeftCor = col * 32
                    brick.RightCor = col * 32 + 32
                    brick.TopCor = row * 32
                    brick.BotCor = row * 32 + 32

                    niz.append(brick)

                elif(j==2):
                    eagle = Eagle("Image/eagle")
                    eagle.setPos(col * 32, row * 32)
                    self.addItem(eagle)
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
        self.player2ScoreLabel.setText("P2 : " + str(self.player2.score))
        self.player2ScoreLabel.setPos(1020, 290)
        self.player2ScoreLabel.setBrush(QBrush(Qt.black))
        self.player2ScoreLabel.setFont(self.player2ScoreFont)
        self.addItem(self.player2ScoreLabel)

        self.enemyNumber = 6

        for i in range(0,6):
            self.createEnemy()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        #PowerUp
        self.powerUpQTimer = QTimer()
        self.powerUpQTimer.timeout.connect(self.powerUpScene)
        self.powerUpQTimer.start(randint(9000,10000))

        self.powerUpImage = QGraphicsPixmapItem()
        self.powerUpName = ""

        self.threadFinished = False
        _thread.start_new_thread(self.enemyNumberCalculate, ())
        while not self.threadFinished:
            continue
        self.threadFinished = False

        self.view = QGraphicsView(self)

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0 ,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.view.setWindowTitle("Battle City")
        self.view.setGeometry(400,150,0,0)



    def enemyNumberCalculate(self):
        x = 350
        z = self.enemyCount
        for i in range(0,6):
            x = x + 45
            if (z == 0):
                break
            for j in range (0,4):
                if(z == 0):
                    break
                self.enemyNumberPic = QGraphicsPixmapItem()
                self.enemyNumberPic.setPos(1020+(j*37), x)
                self.enemyNumberPic.setPixmap(QPixmap("Image/enemyTank32"))
                self.temp.append(self.enemyNumberPic)
                self.addItem(self.temp[j+i*4])

                z = z - 1

        self.threadFinished = True

    def createEnemy(self):
        global enemyTankNumber
        self.t = Enemy("Image/enemyTankTop")
        self.t.setPos(enemyTankNumber*120, 1)
        self.t.enemySpeed = self.enemySpeedScene
        self.t.bulletSpeed = self.enemyBulletSpeed
        self.addItem(self.t)
        self.isGameOver = False

        self.enemyBullet = Bullet(PLAYER_BULLET_X_OFFSETS, PLAYER_BULLET_Y)
        self.enemyBullet.setPos(-1, -1)
        self.addItem(self.enemyBullet)

        self.t.timerEnemy.start(randint(self.minEnemyBulletTimer,self.maxEnemyBulletTimer))
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
        self.game_update()
        self.update()

    def game_update(self):
        if(len(enemies) == 0):
            self.timer.stop()
            self.powerUpQTimer.stop()
            self.removeItem(self.player1Lifes)
            self.removeItem(self.player2Lifes)
            self.removeItem(self.player1)
            self.removeItem(self.bullet)
            self.removeItem(self.player2)
            self.removeItem(self.bullet2)
            for i in range(0,len(niz)):
                niz[-1].setPos(-50, -50)
                self.removeItem(niz[-1])
                niz.remove(niz[-1])
            self.newLevel()

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

        # Enemy bullet can't leave map
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
                self.player1.playerSpeed = 3
                self.p1.setPixmap(QPixmap("Image/P1"))

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
                self.player2.playerSpeed2 = 3
                self.p2.setPixmap(QPixmap("Image/P2"))

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
                self.bullet.active = False
                self.bullet.setPos(-5, -5)
                self.removeItem(self.bullet)
                self.removeItem(enemyPlayer1[1])

                enemyPlayer1[1].active3 = False
                enemyPlayer1[0].isAlive = False
                enemies.remove(enemyPlayer1)

                if(self.enemyCount > 0):
                    self.createEnemy()
                    self.enemyCount = self.enemyCount - 1
                    if(self.enemyCount <= 24):
                        self.removeItem(self.temp[-1])
                        self.temp.remove(self.temp[-1])


        #Player1 picks power up
        if((self.player1.x() <= self.powerUpImage.x()+50 and self.player1.x() >= self.powerUpImage.x() or self.player1.x()+50 <= self.powerUpImage.x()+50 and self.player1.x()+50 >= self.powerUpImage.x()) and (self.player1.y() >= self.powerUpImage.y() and self.player1.y() <= self.powerUpImage.y()+50 or self.player1.y()+50 >= self.powerUpImage.y() and self.player1.y()+50 <= self.powerUpImage.y()+50)):
            self.removeItem(self.powerUpImage)
            self.powerUpImage.setPos(-50,-50)
            if(self.powerUpName == "Image/extraLife"):
                if(self.player1.lifes == 2):
                    self.player1.lifes = self.player1.lifes + 1
                    self.player1Lifes.setPixmap(QPixmap("Image/3lifes"))

                elif(self.player1.lifes == 1):
                    self.player1.lifes = self.player1.lifes + 1
                    self.player1Lifes.setPixmap(QPixmap("Image/2lifes"))

            if (self.powerUpName == "Image/slow"):
                tempRand = randint(0,1)
                if(tempRand == 0):
                    self.player1.playerSpeed = 2
                    self.p1.setPixmap(QPixmap("Image/P1slow"))
                else:
                    self.player1.playerSpeed = 4
                    self.p1.setPixmap(QPixmap("Image/P1_fire"))

        #Player2 picks power up
        if ((self.player2.x() <= self.powerUpImage.x() + 50 and self.player2.x() >= self.powerUpImage.x() or self.player2.x() + 50 <= self.powerUpImage.x() + 50 and self.player2.x() + 50 >= self.powerUpImage.x()) and (self.player2.y() >= self.powerUpImage.y() and self.player2.y() <= self.powerUpImage.y() + 50 or self.player2.y() + 50 >= self.powerUpImage.y() and self.player2.y() + 50 <= self.powerUpImage.y() + 50)):
            self.removeItem(self.powerUpImage)
            self.powerUpImage.setPos(-50, -50)
            if (self.powerUpName == "Image/extraLife"):
                if (self.player2.lifes == 2):
                    self.player2.lifes = self.player2.lifes + 1
                    self.player2Lifes.setPixmap(QPixmap("Image/3lifes"))

                elif (self.player2.lifes == 1):
                    self.player2.lifes = self.player2.lifes + 1
                    self.player2Lifes.setPixmap(QPixmap("Image/2lifes"))

            if (self.powerUpName == "Image/slow"):
                tempRand2 = randint(0, 1)
                if(tempRand2 == 0):
                    self.player2.playerSpeed2 = 2
                    self.p2.setPixmap(QPixmap("Image/P2 slow"))
                else:
                    self.player2.playerSpeed2 = 4
                    self.p2.setPixmap(QPixmap("Image/P2_fire"))

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
                if (self.enemyCount > 0):
                    self.createEnemy()
                    self.enemyCount = self.enemyCount - 1
                    if (self.enemyCount <= 24):
                        self.removeItem(self.temp[-1])
                        self.temp.remove(self.temp[-1])




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

    def powerUpScene(self):
        self.cords = [randint(0,910), randint(0,SCREEN_HEIGHT - 50), randint(0,1)]

        self.powerUpImage.setPos(self.cords[0], self.cords[1])
        if (self.cords[2] == 0):
            self.powerUpName = "Image/extraLife"
            self.powerUpImage.setPixmap(QPixmap("Image/extraLife"))
        elif (self.cords[2] == 1):
            self.powerUpName = "Image/slow"
            self.powerUpImage.setPixmap(QPixmap("Image/slow"))
        self.addItem(self.powerUpImage)

    def newLevel(self):
        self.timer.start(FRAME_TIME_MS, self)

        self.powerUpQTimer.start(5000)

        global ENEMY_NUMBER
        self.enemySpeedScene = self.enemySpeedScene + 0.5
        self.enemyBulletSpeed = self.enemyBulletSpeed + 1
        if(self.minEnemyBulletTimer > 1000 and self.maxEnemyBulletTimer >1500):
            self.minEnemyBulletTimer = self.minEnemyBulletTimer - 200
            self.maxEnemyBulletTimer = self.maxEnemyBulletTimer - 200
        self.player1.playerSpeed = 3
        self.player2.playerSpeed2 = 3
        ENEMY_NUMBER = ENEMY_NUMBER + 2

        self.temp = []

        self.enemyCount = ENEMY_NUMBER - 6

        self.bg = QGraphicsRectItem()
        self.bg.setRect(-1, -1, 992, SCREEN_HEIGHT)
        self.bg.setBrush(QBrush(Qt.black))
        self.addItem(self.bg)
        self.level = self.level + 1

        self.powerUpTimer = 0

        pool = multiprocessing.Pool(processes=1)
        result = pool.apply_async(loadMap, ())
        maps = result.get(timeout=1)
        pool.close()

        row = 0
        col = 0
        for i in maps:
            col = 0
            for j in i:
                if (j == 1):
                    brick = Brick("Image/brick")
                    brick.setPos(col * 32, row * 32)
                    self.addItem(brick)
                    self.update()
                    brick.LeftCor = col * 32
                    brick.RightCor = col * 32 + 32
                    brick.TopCor = row * 32
                    brick.BotCor = row * 32 + 32

                    niz.append(brick)

                elif (j == 2):
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

        if(self.player1.lifes > 0):
            self.player1.setPos((SCREEN_WIDTH - self.player1.pixmap().width()) / 5,
                                (SCREEN_HEIGHT - self.player1.pixmap().height()) / 1)
            self.bullet.setPos(-1, -1)
            self.addItem(self.bullet)
            self.addItem(self.player1)

        if(self.player2.lifes > 0):
            self.player2.setPos((SCREEN_WIDTH - self.player2.pixmap().width()) / 3 * 2,
                                (SCREEN_HEIGHT - self.player2.pixmap().height()) / 1)
            self.bullet2.setPos(-1, -1)
            self.addItem(self.bullet2)
            self.addItem(self.player2)

        self.p1.setPos(1020, 50)
        self.p1.setPixmap(QPixmap("Image/P1"))
        self.addItem(self.p1)
        self.player1Lifes.setPos(1070, 50)
        if self.player1.lifes == 3:
            self.player1Lifes.setPixmap(QPixmap("Image/3lifes"))
            self.addItem(self.player1Lifes)
        elif self.player1.lifes == 2:
            self.player1Lifes.setPixmap(QPixmap("Image/2lifes"))
            self.addItem(self.player1Lifes)
        elif self.player1.lifes == 1:
            self.player1Lifes.setPixmap(QPixmap("Image/1life"))
            self.addItem(self.player1Lifes)

        self.p2.setPos(1020, 150)
        self.p2.setPixmap(QPixmap("Image/P2"))
        self.addItem(self.p2)
        self.player2Lifes.setPos(1070, 150)
        if self.player2.lifes == 3:
            self.player2Lifes.setPixmap(QPixmap("Image/3lifes"))
            self.addItem(self.player2Lifes)
        elif self.player2.lifes == 2:
            self.player2Lifes.setPixmap(QPixmap("Image/2lifes"))
            self.addItem(self.player2Lifes)
        elif self.player2.lifes == 1:
            self.player2Lifes.setPixmap(QPixmap("Image/1life"))
            self.addItem(self.player2Lifes)

        self.levelFlag.setPos(1020, 750)
        self.levelFlag.setPixmap(QPixmap("Image/levelFlag"))
        self.addItem(self.levelFlag)

        self.levelNumberFont.setPixelSize(25)
        self.levelNumberFont.setBold(1)
        self.levelNumber.setText(str(self.level))
        self.levelNumber.setPos(1060, 755)
        self.levelNumber.setBrush(QBrush(Qt.black))
        self.levelNumber.setFont(self.levelNumberFont)
        self.addItem(self.levelNumber)

        self.player1ScoreFont.setPixelSize(35)
        self.player1ScoreFont.setBold(1)
        self.player1ScoreLabel.setText("P1 : " + str(self.player1.score))
        self.player1ScoreLabel.setPos(1020, 230)
        self.player1ScoreLabel.setBrush(QBrush(Qt.black))
        self.player1ScoreLabel.setFont(self.player1ScoreFont)
        self.addItem(self.player1ScoreLabel)

        self.player2ScoreFont.setPixelSize(35)
        self.player2ScoreFont.setBold(1)
        self.player2ScoreLabel.setText("P2 : " + str(self.player2.score))
        self.player2ScoreLabel.setPos(1020, 290)
        self.player2ScoreLabel.setBrush(QBrush(Qt.black))
        self.player2ScoreLabel.setFont(self.player2ScoreFont)
        self.addItem(self.player2ScoreLabel)

        self.enemyNumber = 6

        for i in range(0, 6):
            self.createEnemy()

        self.powerUpImage = QGraphicsPixmapItem()
        self.powerUpName = ""

        self.threadFinished = False
        _thread.start_new_thread(self.enemyNumberCalculate, ())
        while not self.threadFinished:
            continue
        self.threadFinished = False

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
        self.removeItem(self.bullet2)
        self.bullet2.active2 = False


        self.winnerFont = QFont()
        self.winnerFont.setPixelSize(35)
        self.winnerFont.setBold(1)
        self.winner = QGraphicsSimpleTextItem()

        self.winner.setPos(450, 600)
        self.winner.setBrush(QBrush(Qt.white))
        self.winner.setFont(self.winnerFont)


        if(self.player1.lifes > 0 and self.player2.lifes > 0):
            if(self.player1.score > self.player2.score):
                self.winner.setText("PLAYER 1 WINS")
            elif(self.player2.score > self.player1.score):
                self.winner.setText("PLAYER 2 WINS")
            else:
                self.winner.setPos(590, 600)
                self.winner.setText("TIE")

            self.addItem(self.winner)
        elif(self.player1.lifes > 0 and self.player2.lifes == 0):
            self.winner.setText("PLAYER 1 WINS")
            self.addItem(self.winner)
        elif(self.player1.lifes == 0 and self.player2.lifes > 0):
            self.winner.setText("PLAYER 2 WINS")
            self.addItem(self.winner)


def loadMap():
    gameLevel = randint(0, 2)
    gamelevelString = "maps" + str(gameLevel) + ".txt"
    f = open(gamelevelString, 'r')
    maps = [[int(num) for num in line.split(',')] for line in f]
    return maps

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scene()
    sys.exit(app.exec_())