import sys

from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtGui import QAction, QIcon
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
from canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.installEventFilter(self)
        self.create_gui()

    def create_gui(self) -> None:
        window_width = 470
        window_height = 275
        input_box_width = 200
        input_box_height = 40
        button_width = 100
        button_height = 40
        combo_box_width = 100
        combo_box_height = 40
        self.setFixedSize(window_width, window_height)

        # Setup the title bar for the window
        self.setWindowTitle('Hyperion Test Data Viewer')
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

        # Create title label and input box
        self.title_label = QLabel('Serial Number')
        self.title_input = QLineEdit()
        self.title_input.setFixedSize(input_box_width, input_box_height)

        # Create the plot labels
        self.plot1_label = QLabel('Plot 1')
        self.plot1_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.plot2_label = QLabel('Plot 2')
        self.plot2_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.plot3_label = QLabel('Plot 3')
        self.plot3_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.plot4_label = QLabel('Plot 4')
        self.plot4_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create the plot combo boxes
        self.plot1_combo = QComboBox()
        self.plot1_combo.setFixedSize(combo_box_width, combo_box_height)
        self.plot2_combo = QComboBox()
        self.plot2_combo.setFixedSize(combo_box_width, combo_box_height)
        self.plot3_combo = QComboBox()
        self.plot3_combo.setFixedSize(combo_box_width, combo_box_height)
        self.plot4_combo = QComboBox()
        self.plot4_combo.setFixedSize(combo_box_width, combo_box_height)

        # Create the buttons
        self.select_csv_button = QPushButton('Select CSV Files')
        self.select_csv_button.setFixedSize(button_width, button_height)
        self.plot_button = QPushButton('Plot Data')
        self.plot_button.setFixedSize(button_width, button_height)

        # Create the canvas for displaying CSV data
        self.canvas = Canvas()
        self.canvas.display_csv_files(
            ['file1.csv', 'file2.csv', 'file3.csv']
        )  # example data for testing
