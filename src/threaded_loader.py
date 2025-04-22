from pandas import DataFrame
from PySide6.QtCore import QThread, Signal

from src.loader import DataLoader


class LoadDataWorker(QThread):
    finished = Signal(DataFrame)

    def __init__(self, file_list: list[str]) -> None:
        super().__init__()
        self.file_list = file_list

    def run(self) -> None:
        data_loader = DataLoader()
        data_loader.load_data(self.file_list)
        self.finished.emit(data_loader.df)
