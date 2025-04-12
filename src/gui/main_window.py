import sys

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.installEventFilter(self)
        self.create_gui()

    def create_gui(self) -> None:
        window_width = 470
        window_height = 275
        button_width = 100
        button_height = 40
        dropdown_width = 100
        dropdown_height = 40
        self.setFixedSize(window_width, window_height)
        self.setWindowTitle('Hyperion Test Data Viewer')
        if hasattr(sys, 'frozen'):  # Check if running from the Pyinstaller EXE
            icon_path = sys._MEIPASS + '/assets/icon.ico'  # type: ignore
        else:
            icon_path = './assets/icon.ico'  # Use the local icon file in dev mode
        self.setWindowIcon(QIcon(icon_path))
        apply_stylesheet(self, theme='dark_lightgreen.xml', invert_secondary=True)
        self.setStyleSheet(
            self.styleSheet() + """QLineEdit, QTextEdit {color: lightgreen;}"""
        )
