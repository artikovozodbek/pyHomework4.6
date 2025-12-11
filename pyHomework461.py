from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.btn1 = QPushButton("Tugma 1")
        self.btn2 = QPushButton("Tugma 2")
        self.btn3 = QPushButton("Tugma 3")

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)

        self.btn1.clicked.connect(lambda: print("Tugma 1 bosildi"))
        self.btn2.clicked.connect(lambda: print("Tugma 2 bosildi"))
        self.btn3.clicked.connect(lambda: print("Tugma 3 bosildi"))

        self.setLayout(layout)

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
