from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import QPoint


class HighlightManager(QPainter):
    white = QColor(175, 175, 175)
    green = QColor(70, 110, 50)

    def __init__(self, parent):
        super().__init__(parent)

    @staticmethod
    def highlight(self, tile):
        color = self.getColor(tile)

        brush = QBrush(color)
        pen = QPen(color)
        pen.setBrush(brush)

        self.setPen(pen)

        self.drawRect(tile.x(), tile.y(), tile.width(), tile,height())

    def getColor(self, tile):
        if tile.color == '#ffffff':
            return self.white
        return self.green
