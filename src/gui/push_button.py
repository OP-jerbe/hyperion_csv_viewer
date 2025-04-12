from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class PushButton(QWidget):
    def __init__(self, label: str | None = None) -> None:
        super().__init__()

        if not label:
            label = 'Button'
        self.button = QPushButton(label, self)
        self.button.setFixedSize(150, 40)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.setContentsMargins(0, 0, 0, 0)
