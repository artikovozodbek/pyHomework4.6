from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Python", "C++", "Java"])

        self.label = QLabel("Til tanlanmagan")

        self.combo.currentTextChanged.connect(self.update_text)

        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_text(self, val):
        self.label.setText("Tanlangan til: " + val)
