from PySide6.QtWidgets import QComboBox


class ComboBox(QComboBox):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedHeight(40)
        self.setStyleSheet('color: lightgreen;')
        self.addItems(['None'])

    def populate(self, headers: list[str]) -> None:
        """Call this method to update the list of headers from the csv file."""
        self.clear()
        self.addItems(headers)
        self.setEditable(False)
