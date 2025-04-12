import pandas as pd


class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.filepath, parse_dates=True)
        return df
