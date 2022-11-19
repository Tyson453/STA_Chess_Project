import sys

from PyQt5.QtWidgets import QApplication

from game import Game


def getDimensions(app, w, h):
    screen = app.primaryScreen()
    screen_width, screen_height = screen.size().width(), screen.size().height()

    # x = screen_width//2 - w//2
    # y = screen_height//2 - h//2
    x = screen_width//2
    y = 20

    return x, y


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w, h = (app.primaryScreen().size().width()//2,
            app.primaryScreen().size().height()//2 - 20)
    x, y = getDimensions(app, w, h)
    game = Game(w, h, x, y)
    sys.exit(app.exec_())
