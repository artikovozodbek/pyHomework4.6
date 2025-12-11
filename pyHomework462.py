from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        h = QHBoxLayout()

        self.label = QLabel("Matn shu yerda ko'rinadi")

        left = QPushButton("Chapga")
        mid = QPushButton("O'rtaga")
        right = QPushButton("O'ngga")

        h.addWidget(left)
        h.addWidget(mid)
        h.addWidget(right)

        left.clicked.connect(lambda: self.label.setText("Chapga bosildi"))
        mid.clicked.connect(lambda: self.label.setText("O'rtaga bosildi"))
        right.clicked.connect(lambda: self.label.setText("O'ngga bosildi"))

        layout.addWidget(self.label)
        layout.addLayout(h)
        self.setLayout(layout)
