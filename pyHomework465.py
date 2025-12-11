from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.price = {
            "Olma": 5000,
            "Banan": 7000,
            "Uzum": 8000
        }

        self.c1 = QCheckBox("Olma – 5000")
        self.c2 = QCheckBox("Banan – 7000")
        self.c3 = QCheckBox("Uzum – 8000")

        self.label = QLabel("Umumiy narx: 0 so'm")

        for c in (self.c1, self.c2, self.c3):
            c.stateChanged.connect(self.update_price)
            layout.addWidget(c)

        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_price(self):
        total = 0
        if self.c1.isChecked(): total += 5000
        if self.c2.isChecked(): total += 7000
        if self.c3.isChecked(): total += 8000
        self.label.setText(f"Umumiy narx: {total} so'm")
