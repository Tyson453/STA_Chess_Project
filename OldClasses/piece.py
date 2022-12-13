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
        self.setAlignment(Qt.AlignCenter)
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

        if self.parent().parent().parent().player.color != self.color:
            return

        drag = QDrag(self)
        mime = QMimeData()
        drag.setMimeData(mime)
        x = drag.exec_(Qt.MoveAction)
        if x == 2:
            self.parent().parent().parent().nextTurn()
            self.parent().deletePiece()

        self.parent().parent().unhighlightAll()

    def mousePressEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return

        if self.parent().parent().parent().player.color != self.color:
            return

        self.parent().highlightPossibleMoves()

    def mouseReleaseEvent(self, e):
        self.parent().parent().unhighlightAll()

    def occupiedHighlight(self):
        self.hideHighlight()
        self.setStyleSheet(
            f"""
            background-color: rgba(255, 255, 255, 0);
            border-radius: {self.width()//2}px;
            border: {self.width()//8}px solid rgba(170, 170, 170, 255);
            """
        )

    def emptyHighlight(self):
        self.hideHighlight()
        self.setStyleSheet(
            f"""
            background-color: rgba(170, 170, 170, 170);
            border-radius: {self.width()//2}px;
            border: {self.width()//2}px solid rgba(255, 255, 255, 0);
            """
        )

    def showHighlight(self, code):
        if code:
            self.occupiedHighlight()
        else:
            self.emptyHighlight()

        self.show()

    def hideHighlight(self):
        self.setStyleSheet("")

    def __repr__(self):
        return f"{self.code}"
