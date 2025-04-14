import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from qt_material import apply_stylesheet

from gui.canvas import Canvas
from gui.combo_box import ComboBox
from loader import DataLoader
from plotter import Plotter


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.installEventFilter(self)
        self.create_gui()

    def create_gui(self) -> None:
        # Set the size of the main window
        self.setFixedSize(420, 500)

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
            self.styleSheet()
            + """QLineEdit, QTextEdit, QCombobox {color: lightgreen;}"""
        )

        # Create the menu bar
        self.menu_bar: QMenuBar = self.menuBar()

        # Create the menu bar items
        self.file_menu: QMenu = self.menu_bar.addMenu('File')
        self.save_menu: QMenu = self.menu_bar.addMenu('Save')
        self.help_menu: QMenu = self.menu_bar.addMenu('Help')

        # Create the QAction objects for the menus
        self.exit_option: QAction = QAction('Exit', self)
        self.save_3D_surface_option: QAction = QAction('Save Plot as HTML', self)
        self.open_quick_start_guide: QAction = QAction('Quick Start Guide', self)

        # Add the action objects to the menu bar items
        self.file_menu.addAction(self.exit_option)
        self.save_menu.addAction(self.save_3D_surface_option)
        self.help_menu.addAction(self.open_quick_start_guide)

        # Create title label and input box
        self.title_label: QLabel = QLabel('Title:')
        self.title_label.setContentsMargins(0, 0, 5, 0)
        self.title_label.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred
        )
        self.title_label.setStyleSheet('font-size: 16pt;')
        self.title_input: QLineEdit = QLineEdit()
        self.title_input.setFixedHeight(40)

        # Create the plot labels
        self.plot1_label: QLabel = QLabel('Plot 1')
        self.plot1_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.plot2_label: QLabel = QLabel('Plot 2')
        self.plot2_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.plot3_label: QLabel = QLabel('Plot 3')
        self.plot3_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.plot4_label: QLabel = QLabel('Plot 4')
        self.plot4_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Create the plot combo boxes
        self.plot1_combo: ComboBox = ComboBox()
        self.plot2_combo: ComboBox = ComboBox()
        self.plot3_combo: ComboBox = ComboBox()
        self.plot4_combo: ComboBox = ComboBox()
        self.combo_boxes: list[ComboBox] = [
            self.plot1_combo,
            self.plot2_combo,
            self.plot3_combo,
            self.plot4_combo,
        ]

        # Create the buttons
        self.select_csv_button: QPushButton = QPushButton('Select CSV Files')
        self.select_csv_button.setFixedSize(150, 40)
        self.select_csv_button.clicked.connect(self.handle_select_csv)
        self.plot_button: QPushButton = QPushButton('Plot Data')
        self.plot_button.setFixedSize(150, 40)
        self.plot_button.clicked.connect(self.handle_plot)

        # Create the canvas for displaying CSV data
        self.canvas: Canvas = Canvas()

        # Create the layout for the main window
        self.h_title_layout: QHBoxLayout = QHBoxLayout()
        self.h_title_layout.addWidget(self.title_label, stretch=0)
        self.h_title_layout.addWidget(self.title_input, stretch=1)
        self.h_title_layout.setContentsMargins(10, 0, 10, 0)
        self.h_title_layout.setSpacing(0)

        self.g_combo_box_layout: QGridLayout = QGridLayout()
        spacer_widget = QWidget()
        spacer_widget.setFixedHeight(5)
        self.g_combo_box_layout.addWidget(self.plot1_label, 0, 0)
        self.g_combo_box_layout.addWidget(self.plot2_label, 0, 1)
        self.g_combo_box_layout.addWidget(self.plot1_combo, 1, 0)
        self.g_combo_box_layout.addWidget(self.plot2_combo, 1, 1)
        self.g_combo_box_layout.addWidget(spacer_widget, 2, 0, 1, 2)
        self.g_combo_box_layout.addWidget(self.plot3_label, 3, 0)
        self.g_combo_box_layout.addWidget(self.plot4_label, 3, 1)
        self.g_combo_box_layout.addWidget(self.plot3_combo, 4, 0)
        self.g_combo_box_layout.addWidget(self.plot4_combo, 4, 1)
        self.g_combo_box_layout.setColumnStretch(0, 1)
        self.g_combo_box_layout.setColumnStretch(1, 1)
        self.g_combo_box_layout.setContentsMargins(10, 10, 10, 0)
        self.g_combo_box_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_button_layout: QVBoxLayout = QVBoxLayout()
        self.v_button_layout.addWidget(self.select_csv_button)
        self.v_button_layout.addWidget(self.plot_button)
        self.v_button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v_button_layout.setContentsMargins(0, 10, 0, 0)

        self.v_canvas_layout: QVBoxLayout = QVBoxLayout()
        self.v_canvas_layout.addWidget(self.canvas)
        self.v_canvas_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_main_layout: QVBoxLayout = QVBoxLayout()
        self.v_main_layout.addLayout(self.h_title_layout)
        self.v_main_layout.addLayout(self.g_combo_box_layout)
        self.v_main_layout.addLayout(self.v_button_layout)
        self.v_main_layout.addLayout(self.v_canvas_layout)

        container: QWidget = QWidget()
        container.setLayout(self.v_main_layout)

        self.setCentralWidget(container)

    def handle_select_csv(self) -> None:
        data_loader = DataLoader()
        file_paths = data_loader.get_file_paths()
        if not file_paths:
            return

        self.df = data_loader.load_data(file_paths)
        if self.df is None:
            QMessageBox.critical(
                self, 'Error', 'Failed to load data from the selected files.'
            )
            return

        headers = self.df.columns.tolist()
        headers[headers.index('Time')] = 'None'

        for combo in self.combo_boxes:
            combo.populate(headers)

        self.canvas.display_csv_files(file_paths)

    def handle_plot(self) -> None:
        combo_box_selections: list[str] = [
            combo.current_text() for combo in self.combo_boxes
        ]

        print(combo_box_selections)

        if all(selection == 'None' for selection in combo_box_selections):
            QMessageBox.warning(
                self, '\nNo Data Selected', 'Please select at least one column to plot.'
            )
            return

        if self.df is None:
            QMessageBox.critical(
                self, 'Error', 'No data loaded. Please load a CSV file first.'
            )
            return
        plotter = Plotter(
            title=self.title_input.text(), traces=combo_box_selections, data=self.df
        )
        fig = plotter.create_fig()

        fig.show()
