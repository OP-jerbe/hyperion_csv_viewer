from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget


class Canvas(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('Selected csv files:')
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("""
            background-color: gray;
            border: 2px ridge gray;
        """)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.text_display)

    def display_csv_files(self, file_list) -> None:
        """Call this method to update the display with a list of CSV filenames."""
        self.text_display.clear()
        self.text_display.append('\n'.join(file_list))
