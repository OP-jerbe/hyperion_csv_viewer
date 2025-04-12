from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('My Time Series Project')
        self.setGeometry(100, 100, 800, 600)
