import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
import UI


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.ui = UI.Ui_Form()
        self.ui.setupUi(self)
        qp = QPainter()
        qp.begin(self)
        self.ui.btn.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag:
            self.flag = False
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            a = randint(5, 200)
            qp.drawEllipse(randint(5, 200), randint(5, 200), a, a)
            qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
