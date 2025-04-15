from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys
from typing import NoReturn


def run_app() -> NoReturn:
    version = '2.0.0'
    app = QApplication([])
    window = MainWindow(version=version)  # Create the main window from main_window.py
    window.show()  # Show the window
    sys.exit(app.exec())  # Start the application's event loop


if __name__ == '__main__':
    run_app()
