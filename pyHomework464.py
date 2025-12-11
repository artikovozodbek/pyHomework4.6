from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.input = QLineEdit()
        self.btn = QPushButton("Qo'shish")
        self.combo = QComboBox()

        self.btn.clicked.connect(self.add_word)

        layout.addWidget(self.input)
        layout.addWidget(self.btn)
        layout2 = QVBoxLayout()
        layout2.addLayout(layout)
        layout2.addWidget(self.combo)

        self.setLayout(layout2)

    def add_word(self):
        text = self.input.text()
        if text:
            self.combo.addItem(text)
            self.input.clear()
