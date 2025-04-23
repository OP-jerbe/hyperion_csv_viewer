from pandas import DataFrame
from PySide6.QtCore import QThread, Signal

from src.loader import DataLoader


class LoadDataWorker(QThread):
    finished = Signal(DataFrame)
    error_occurred = Signal(str)

    def __init__(self, file_list: list[str]) -> None:
        super().__init__()
        self.file_list = file_list

    def run(self) -> None:
        try:
            data_loader = DataLoader()
            data_loader.load_data(self.file_list)
            self.finished.emit(data_loader.df)
        except Exception as e:
            self.error_occurred.emit(str(e))
