from pathlib import Path

from PySide6.QtWidgets import QLabel, QTextEdit, QVBoxLayout, QWidget

from src.loader import DataLoader


class Canvas(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.label = QLabel('0 files selected (0 MB)')
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
        data_size: float = DataLoader.get_total_file_size(file_list)
        filenames: list[str] = [Path(path).name for path in file_list]
        self.text_display.append('\n'.join(filenames))
        if len(file_list) == 1:
            self.label.setText(f'{len(file_list)} file selected ({data_size:.2f} MB)')
        else:
            self.label.setText(f'{len(file_list)} files selected ({data_size:.2f} MB)')
