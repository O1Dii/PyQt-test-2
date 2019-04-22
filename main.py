import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import randint


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Window')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def mousePressEvent(self, QMouseEvent):
        global points_main, last_point, mouse_over, points
        if not mouse_over:
            x = QMouseEvent.x()
            y = QMouseEvent.y()
            print(x, y)
            points_main.append((x, y))
            last_point = (x, y)
        else:
            points.clear()
            points_main.clear()
            mouse_over = False

    def drawPoints(self, qp):
        global points

        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        for x, y in points_main:
            qp.drawPoint(x, y)
        for x, y in points:
            qp.drawPoint(x, y)

    def keyPressEvent(self, QKeyEvent):
        global mouse_over
        mouse_over = True


def fract():
    global points, last_point, points_main, mouse_over
    if mouse_over:
        r = randint(0, len(points_main) - 1)
        x = (last_point[0] + points_main[r][0]) / 2
        y = (last_point[1] + points_main[r][1]) / 2
        points.add((x, y))
        last_point = (x, y)
    ex.update()


points = set()
points_main = list()
last_point = (0, 0)
mouse_over = False

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()

    timer = QTimer()
    timer.timeout.connect(fract)
    timer.start(0.001)

    sys.exit(app.exec_())
