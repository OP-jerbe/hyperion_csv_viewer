import sys

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)
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

        # Set the icon for the window
        if hasattr(sys, 'frozen'):  # Check if running from the Pyinstaller EXE
            icon_path = sys._MEIPASS + '/assets/icon.ico'  # type: ignore
        else:
            icon_path = './assets/icon.ico'  # Use the local icon file in dev mode
        self.setWindowIcon(QIcon(icon_path))

        # Set the style of the window
        apply_stylesheet(self, theme='dark_lightgreen.xml', invert_secondary=True)
        self.setStyleSheet(
            self.styleSheet() + """QLineEdit, QTextEdit {color: lightgreen;}"""
        )

        # Create the menu bar
        self.menu_bar = self.menuBar()

        # Create the menu bar items
        self.file_menu = self.menu_bar.addMenu('File')
        self.save_menu = self.menu_bar.addMenu('Save')
        self.help_menu = self.menu_bar.addMenu('Help')

        # Create the QAction objects for the menus
        self.exit_option = QAction('Exit', self)
        self.save_3D_surface_option = QAction('Save Plot as HTML', self)
        self.open_quick_start_guide = QAction('Quick Start Guide', self)

        # Add the action objects to the menu bar items
        self.file_menu.addAction(self.exit_option)
        self.save_menu.addAction(self.save_3D_surface_option)
        self.help_menu.addAction(self.open_quick_start_guide)
