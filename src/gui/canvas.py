from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget
from pathlib import Path


class Canvas(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('Selected csv files: (0)')
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_display.setStyleSheet("""
            color: lightgreen;
        """)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.text_display)

    def display_csv_files(self, file_list) -> None:
        """Call this method to update the display with a list of CSV filenames."""
        self.text_display.clear()
        filenames = [Path(path).name for path in file_list]
        self.text_display.append('\n'.join(filenames))
        self.label.setText(f'Selected csv files: ({len(file_list)})')
