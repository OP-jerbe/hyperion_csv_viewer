from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget


class Canvas(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('CSV Display')
        self.resize(400, 250)

        layout = QVBoxLayout(self)

        self.label = QLabel('Selected csv files:')
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("""
            background-color: white;
            border: 2px ridge gray;
        """)
        self.text_display.setFixedHeight(200)

        layout.addWidget(self.label)
        layout.addWidget(self.text_display)

    def display_csv_files(self, file_list) -> None:
        """Call this method to update the display with a list of CSV filenames."""
        self.text_display.clear()
        self.text_display.append('\n'.join(file_list))
