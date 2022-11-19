from PyQt5.QtGui import QColor


class RGB(QColor):
    def __init__(self, r, g, b):
        super().__init__(r, g, b)

        self.r = r
        self.g = g
        self.b = b
