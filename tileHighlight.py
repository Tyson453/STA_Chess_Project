from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint


class HighlightManager(QPainter):
    white = QColor(175, 175, 175)
    green = QColor(70, 110, 50)

    def __init__(self, parent):
        super().__init__(parent)

    def highlight(self, tile):
        if tile.piece.code:
            self.highlightOccupied(tile)
        else:
            self.highlightEmpty(tile)

    def highlightOccupied(self, tile):
        x, y = tile.x, tile.y

        center = self.getCenter(tile)

        self.setPen(self.getColor(tile))
        self.drawEllipse(center, tile.length//2, tile.length//2)

        self.setPen(QColor(tile.color))
        self.drawEllipse(center, tile.length//2 - tile.length //
                         20, tile.length//2 - tile.length//20)

    def highlightEmpty(self, tile):
        x, y = tile.x, tile.y

        self.setPen(self.getColor(tile))

        self.drawEllipse(self.getCenter(tile), tile.length//6, tile.length//6)

    def getColor(self, tile):
        if tile.color == '#ffffff':
            return self.white
        return self.green

    def getCenter(self, tile):
        x = tile.length * (tile.x+0.5)
        y = tile.length * (tile.y+0.5)

        return QPoint(x, y)
