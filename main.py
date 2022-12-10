import sys

from PyQt5.QtWidgets import QApplication

from window import Window


def getDimensions(app, w, h):
    screen = app.primaryScreen()
    screen_width, screen_height = screen.size().width(), screen.size().height()

    x = screen_width//2 - w//2
    y = screen_height//2 - h//2

    return x, y


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w, h = (app.primaryScreen().size().width()//2,
            app.primaryScreen().size().height()//2)
    x, y = getDimensions(app, w, h)
    window = Window(w, h, x, y)
    sys.exit(app.exec_())
