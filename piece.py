from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QDrag
from PyQt5.QtCore import Qt, QMimeData


class Piece(QLabel):
    def __init__(self, parent, color, piece):
        self.color = color
        self.piece = piece
        try:
            self.code = piece + color
        except TypeError:
            self.code = None

        if color and piece:
            self.imagePath = f"images/Chess_{self.piece}{self.color}t60.png"
        else:
            self.imagePath = None

        self.length = parent.length
        super().__init__(parent)
        self.setGeometry(0, 0, self.length, self.length)
        if self.imagePath:
            self.pixmap = QPixmap(self.imagePath).scaledToWidth(
                self.length).scaledToHeight(self.length)
            self.pixmap.imagePath = self.imagePath
            self.setPixmap(self.pixmap)
        else:
            self.pixmap = QPixmap(None)
            self.pixmap.imagePath = None
            self.setPixmap(self.pixmap)

        self.show()

# https://www.pythonguis.com/faq/pyqt-drag-drop-widgets/
    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return

        if self.parent().parent().parent().currentPlayer.color != self.color:
            return

        self.parent().displayPossibleMoves()

        drag = QDrag(self)
        mime = QMimeData()
        drag.setMimeData(mime)
        x = drag.exec_(Qt.MoveAction)
        if x == 2:
            self.parent().deletePiece()
