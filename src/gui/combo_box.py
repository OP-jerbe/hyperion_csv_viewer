from PySide6.QtWidgets import QComboBox, QVBoxLayout, QWidget


class ComboBox(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.combo_box = QComboBox(self)
        self.combo_box.setFixedHeight(40)
        self.combo_box.setStyleSheet('color: white;')

        layout = QVBoxLayout(self)
        layout.addWidget(self.combo_box)
        layout.setContentsMargins(0, 0, 0, 0)

    def populate(self, headers: list[str]) -> None:
        """Call this method to update the list of headers from the csv file."""
        self.combo_box.clear()
        self.combo_box.addItems(headers)
        self.combo_box.setEditable(False)

    def current_text(self) -> str:
        """Returns the current text selected in the combo box."""
        return self.combo_box.currentText()
