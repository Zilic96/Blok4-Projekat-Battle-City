import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


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
PLAYER_BULLET_X_OFFSETS = 23
PLAYER_BULLET_Y         = 15
BULLET_SPEED            = 10  # pix/frame
BULLET_FRAMES           = 90
FRAME_TIME_MS           = 16  # ms/frame
playerPositions = [(0,0),(0,0)]

maps = []
f = open('maps0.txt', 'r')
maps = [[int(num) for num in line.split(',')] for line in f]
niz = []

class Player(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.image = "Image/tankTop"
        self.image2 = "Image/tank2Top"
        self.lifes = 3
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
            if self.y() >= 746:
                dy -= 0
            elif(canMove):
                dy += PLAYER_SPEED
            self.setimage2("Image/tank2Bottom")
        playerPositions[1] = (self.x() + dx, self.y() + dy)
        #print(self.playerPositions[1])
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

class Bullet(QGraphicsPixmapItem):
    def __init__(self, offset_x, offset_y, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.imageBullet = "Image/bulet"
        self.imageBullet2 = "Image/bulet"
        self.setPixmap(QPixmap(self.imageBullet))
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.active = False
        self.active2 = False
        self.frames = 0
        self.frames2 = 0
        self.bulletDirection = 0
        self.bulletDirection2 = 0

    def setBulletImage(self, image):
        self.imageBullet = image
        self.setPixmap(QPixmap(self.imageBullet))

    def setBulletImage2(self, image):
        self.imageBullet2 = image
        self.setPixmap(QPixmap(self.imageBullet2))

    def game_update(self, keys_pressed, player):
        if not self.active:
            if Qt.Key_Space in keys_pressed:
                #print(player.image)
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
            #print(self.bulletDirection)
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
            if Qt.Key_Control in keys_pressed:
                print(player.getimage2())
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

class Brick(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.LeftCor = 0
        self.RightCor = 0
        self.TopCor = 0
        self.BotCor = 0

class Eagle(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.LeftCor = 0
        self.RightCor = 0
        self.TopCor = 0
        self.BotCor = 0


class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(-1,-1,992,SCREEN_HEIGHT)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)
        self.gameLevel = 1


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

        self.bullet.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.addItem(self.bullet)

        self.bullet2 = Bullet(PLAYER_BULLET_X_OFFSETS, PLAYER_BULLET_Y)
        self.bullet2.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.addItem(self.bullet2)

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

        self.levelNumber = QGraphicsSimpleTextItem()
        self.levelNumber.setText(str(self.gameLevel))
        self.levelNumber.setPos(1040,770)
        self.levelNumber.setBrush(QBrush(Qt.black))
        self.addItem(self.levelNumber)

        self.enemyNumberPic = QGraphicsPixmapItem()
        self.enemyNumberPic.setPos(1020, 400)
        self.enemyNumberPic.setPixmap(QPixmap("Image/enemyTankTop"))
        self.addItem(self.enemyNumberPic)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.view.setWindowTitle("Battle City")

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player1.game_update(self.keys_pressed)
        self.bullet.game_update(self.keys_pressed, self.player1)
        self.player2.game_update2(self.keys_pressed)
        self.bullet2.game_update2(self.keys_pressed, self.player2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scene()
    sys.exit(app.exec_())
