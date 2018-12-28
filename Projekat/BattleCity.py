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
PLAYER_BULLET_X_OFFSETS = [25,45]
PLAYER_BULLET_Y         = 15
BULLET_SPEED            = 10  # pix/frame
BULLET_FRAMES           = 90
FRAME_TIME_MS           = 16  # ms/frame

class Player(QGraphicsPixmapItem):
    def __init__(self, image, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(image))
        self.image = "Image/tankTop"
        self.image2 = "Image/tank2Top"

    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_Left in keys_pressed:
            dx -= PLAYER_SPEED
            self.setimage("Image/tankLeft")
        elif Qt.Key_Right in keys_pressed:
            dx += PLAYER_SPEED
            self.setimage("Image/tankRight")
        elif Qt.Key_Up in keys_pressed:
            dy -= PLAYER_SPEED
            self.setimage("Image/tankTop")
        elif Qt.Key_Down in keys_pressed:
            dy += PLAYER_SPEED
            self.setimage("Image/tankBottom")
        self.setPos(self.x()+dx, self.y()+dy)

    def game_update2(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_A in keys_pressed:
            dx -= PLAYER_SPEED
            self.setimage2("Image/tank2Left")
        elif Qt.Key_D in keys_pressed:
            dx += PLAYER_SPEED
            self.setimage2("Image/tank2Right")
        elif Qt.Key_W in keys_pressed:
            dy -= PLAYER_SPEED
            self.setimage2("Image/tank2Top")
        elif Qt.Key_S in keys_pressed:
            dy += PLAYER_SPEED
            self.setimage2("Image/tank2Bottom")
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
        self.setPixmap(QPixmap("Image/bulet"))
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.active = False
        self.active2 = False
        self.frames = 0
        self.frames2 = 0
        self.bulletDirection = 0
        self.bulletDirection2 = 0

    def game_update(self, keys_pressed, player):
        if not self.active:
            if Qt.Key_Space in keys_pressed:
                #print(player.image)
                if player.getimage() == "Image/tankTop":
                    self.bulletDirection = 0
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage() == "Image/tankRight":
                    self.bulletDirection = 1
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage() == "Image/tankBottom":
                    self.bulletDirection = 2
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage() == "Image/tankLeft":
                    self.bulletDirection = 3
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)

                self.active = True
                self.frames = BULLET_FRAMES

        else:
            #print(self.bulletDirection)
            if self.bulletDirection == 0:
                self.setPos(self.x(),self.y()-BULLET_SPEED)
            elif self.bulletDirection == 2:
                self.setPos(self.x(), self.y() + BULLET_SPEED)
            self.frames -= 1
            if self.frames <= 0:
                self.active = False
                self.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)

    def game_update2(self, keys_pressed, player):
        if not self.active2:
            if Qt.Key_Control in keys_pressed:
                print(player.getimage2())
                if player.getimage2() == "Image/tank2Top":
                    self.bulletDirection2 = 0
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage2() == "Image/tank2Right":
                    self.bulletDirection2 = 1
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage2() == "Image/tank2Bottom":
                    self.bulletDirection2 = 2
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)
                elif player.getimage2() == "Image/tank2Left":
                    self.bulletDirection2 = 3
                    self.setPos(player.x() + self.offset_x, player.y() + self.offset_y)

                self.active2 = True
                self.frames2 = BULLET_FRAMES

        else:
            if self.bulletDirection2 == 0:
                self.setPos(self.x(),self.y()-BULLET_SPEED)
            elif self.bulletDirection2 == 2:
                self.setPos(self.x(), self.y() + BULLET_SPEED)
            self.frames2 -= 1
            if self.frames2 <= 0:
                self.active2 = False
                self.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)

class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(-1,-1,SCREEN_WIDTH+2,SCREEN_HEIGHT+2)
        bg.setBrush(QBrush(Qt.black))
        self.addItem(bg)

        self.player1 = Player("Image/tankTop")
        self.player1.setPos((SCREEN_WIDTH-self.player1.pixmap().width())/4,
                           (SCREEN_HEIGHT-self.player1.pixmap().height())/4)
        self.player2 = Player("Image/tank2Top")
        self.player2.setPos((SCREEN_WIDTH - self.player2.pixmap().width()) / 2,
                            (SCREEN_HEIGHT - self.player2.pixmap().height()) / 2)

        self.bullets = [Bullet(PLAYER_BULLET_X_OFFSETS[0],PLAYER_BULLET_Y)]
        for b in self.bullets:
            b.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)
            self.addItem(b)
        self.addItem(self.player1)
        self.addItem(self.player2)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player1.game_update(self.keys_pressed)
        for b in self.bullets:
            b.game_update(self.keys_pressed, self.player1)
        self.player2.game_update2(self.keys_pressed)
        for b in self.bullets:
            b.game_update2(self.keys_pressed, self.player2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scene()
    sys.exit(app.exec_())
