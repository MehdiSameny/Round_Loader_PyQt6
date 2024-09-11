# ///////////////////////////////////////////////////////////////
# Developer: Mehdi Sameni
# Designer: Mehdi Sameni
# PyQt6
# Python 3.10
# other module : perlin_noise
# ///////////////////////////////////////////////////////////////

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout
from PyQt6.QtGui import QColor
from RoundProgress import CircleProgressBar



class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.addWidget(CircleProgressBar(self))
        layout.addWidget(CircleProgressBar(self, color=QColor(255, 50, 150), clockwise=False))
        layout.addWidget(CircleProgressBar(self, styleSheet="""qproperty-color: rgb(50, 255, 150);"""))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
