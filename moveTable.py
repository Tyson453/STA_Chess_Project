from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QSize

class MoveTable(QTableWidget):
    def __init__(self, parent, x, y, w, h):
        super().__init__(parent)

        self.currentRow = 0
        self.currentCol = 0

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setStyleSheet("border: 2px solid black; font-size: 14pt;")

        self.setRowCount(0)
        self.setColumnCount(2)

        self.setHorizontalHeaderItem(0, QTableWidgetItem("Player 1"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Player 2"))

        self.colHeader = self.horizontalHeader()
        self.colHeader.setSectionResizeMode(0, QHeaderView.Stretch)
        self.colHeader.setSectionResizeMode(1, QHeaderView.Stretch)
        self.colHeader.setStyleSheet("border-width: 2px; border-style: solid; border-color: white white black white")

        self.rowHeader = self.verticalHeader()
        self.rowHeader.hide()

    def addMove(self, move):
        self.setRowCount(self.currentRow+1)
        self.setItem(self.currentRow, self.currentCol, QTableWidgetItem(move))
        self.item(self.currentRow, self.currentCol).setTextAlignment(Qt.AlignCenter)
        self.scrollToBottom()

        if self.currentCol == 0:
            self.currentCol += 1
        elif self.currentCol == 1:
            self.currentCol = 0
            self.currentRow += 1
