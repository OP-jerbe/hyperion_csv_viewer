import pandas as pd
from pandas import DataFrame
from PySide6.QtWidgets import QFileDialog
import sys


class DataLoader:
    def __init__(self) -> None:
        self.df: DataFrame | None = None

    def _check_for_time_header(self) -> bool:
        """Checks that 'Time' is in headers list"""
        if self.df is None:
            return False
        for string in ('Time',):
            if string in self.df.columns:
                return True
        return False

    def get_file_paths(self) -> list[str]:
        """
        Open a file dialog to select a CSV file.

        Returns:
            str: The path to the selected CSV file. If no file is selected, an empty string is returned.

        Notes:
            The file dialog starts in the Production History directory and filters for CSV files.
            If no file is selected, the function will return an empty string.
        """
        if hasattr(sys, 'frozen'):  # Check if running from the bundled app
            dir = r'C:\\teststanddata'
        else:
            dir = r'\\opdata2\Company\PRODUCTION FOLDER\Production History'

        file_paths, _ = QFileDialog.getOpenFileNames(
            parent=None,
            caption='Choose CSV Files',
            dir=dir,
            filter='CSV Files (*.csv);;All Files (*)',
        )

        return file_paths

    def load_data(self, file_paths: list[str]) -> DataFrame | None:
        """
        Load CSV data from the specified file path.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            DataFrame | None: The loaded DataFrame or None.
        """

        try:
            self.df = pd.concat(map(pd.read_csv, file_paths), ignore_index=True)
        except Exception as e:
            print(f'Error loading CSV files: {e}')
            return

        if self._check_for_time_header() is False:
            raise ValueError(
                'No "Time" header in the CSV file. Please check the file format.'
            )

        rename_map = {
            'Angular Intensity (mA/str)': 'Angular Intensity (mA/sr)',
            'Beam Voltage (kV)': 'Beam Voltage (V)',
            'Extractor Voltage (kV)': 'Extractor Voltage (V)',
            'Extractor Current (uA)': 'Extractor Current (μA)',
            'Beam Supply Current (uA)': 'Beam Supply Current (μA)',
            'Lens #1 Current (uA)': 'Lens Current (μA)',
            'Lens #1 Voltage (V)': 'Lens Voltage (V)',
            'Lens #1 Voltage (kV)': 'Lens Voltage (V)',
            'Total Current (uA)': 'Total Current (A)',
        }

        self.df.rename(columns=rename_map, inplace=True, errors='ignore')

        return self.df

    def strip_time_from_headers(self) -> list[str] | None:
        """Removes the 'Time' column header from the list of headers in the DataFrame."""
        if self.df is None:
            return
        df_headers: list[str] = self.df.columns.tolist()
        time_header: bool = self._check_for_time_header()
        if time_header is True:
            df_headers.remove('Time')
        return df_headers
