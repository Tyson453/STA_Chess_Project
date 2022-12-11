from PyQt5.QtGui import QColor

# Class for handling RGB colors


class RGB(QColor):
    def __init__(self, r, g, b):
        super().__init__(r, g, b)

        self.r = r
        self.g = g
        self.b = b

    def __sub__(self, other):
        r = self.r - other.r
        g = self.g - other.g
        b = self.b - other.b

        r = max(r, 0)
        g = max(g, 0)
        b = max(b, 0)

        return RGB(r, g, b)

    def __add__(self, other):
        r = self.r + other.r
        g = self.g + other.g
        b = self.b + other.b

        r = min(r, 255)
        g = min(g, 255)
        b = min(b, 255)

        return RGB(r, g, b)

    def __repr__(self):
        return f"RGB({self.r}, {self.g}, {self.b})"
