from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.r1 = QRadioButton("Qizil")
        self.r2 = QRadioButton("Yashil")
        self.r3 = QRadioButton("Ko'k")

        self.r1.toggled.connect(lambda: self.change_color("red"))
        self.r2.toggled.connect(lambda: self.change_color("green"))
        self.r3.toggled.connect(lambda: self.change_color("blue"))

        layout.addWidget(self.r1)
        layout.addWidget(self.r2)
        layout.addWidget(self.r3)

        self.setLayout(layout)

    def change_color(self, color):
        if self.sender().isChecked():
            pal = self.palette()
            pal.setColor(QPalette.Window, QColor(color))
            self.setAutoFillBackground(True)
            self.setPalette(pal)
