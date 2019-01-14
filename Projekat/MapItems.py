from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



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