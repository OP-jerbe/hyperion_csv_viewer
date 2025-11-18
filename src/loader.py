import sys
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from PySide6.QtWidgets import QFileDialog


class DataLoader:
    def __init__(self) -> None:
        self.df: DataFrame | None = None

    @staticmethod
    def _check_csv_headers(file_paths: list[str]) -> tuple[bool, list[str] | None]:
        """
        Validates that all provided CSV files contain a header row and that
        the headers are identical across all files.

        Args:
            file_paths (list[str]): A list of file paths (as strings) to CSV files.

        Returns:
            tuple[bool, list[str] | None]:
                - A tuple where the first element is True if all CSV files contain
                a header and share the same structure, otherwise False.
                - The second element is the list of headers if validation passed,
                or None if it failed.
        """
        reference_headers: list[str] | None = None

        for path_str in file_paths:
            try:
                headers = pd.read_csv(path_str, nrows=0).columns.tolist()
                if reference_headers is None:
                    reference_headers = headers
                elif headers != reference_headers:
                    return False, None

            except Exception as e:
                print(f'Error reading headers from "{path_str}": {str(e)}\n')
                return False, None

        return True, reference_headers

    @staticmethod
    def _check_for_time_header(headers: list[str] | None) -> bool:
        """
        Checks if the provided list of headers contains a 'Time' column.

        Args:
            headers (list[str] | None): A list of column headers or None.

        Returns:
            bool: True if 'Time' is present in the headers, otherwise False.
        """
        if headers is None:
            return False
        if 'Time' not in headers:
            return False

        return True

    @staticmethod
    def get_file_paths() -> list[str]:
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

    @staticmethod
    def get_total_file_size(file_paths: list[str]) -> float:
        """
        Calculate the total size (in megabytes) of all files specified in the file path list.

        Args:
            file_paths (list[str]): List of file paths.

        Returns:
            float: Combined file size in megabytes (MB).
        """
        paths = [Path(path) for path in file_paths]
        total_size_bytes = sum(p.stat().st_size for p in paths)
        return total_size_bytes / (1024**2)

    def load_data(self, file_paths: list[str]) -> DataFrame | None:
        """
        Load CSV data from the specified file path.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            DataFrame | None: The loaded DataFrame or None.
        """

        has_headers, headers = self._check_csv_headers(file_paths)

        if has_headers is False:
            raise ValueError(
                'Inconsistent headers in the CSV files. Please check the file format.'
            )

        if self._check_for_time_header(headers) is False:
            raise ValueError('"Time" header not found in csv file.')

        try:
            self.df = pd.concat(map(pd.read_csv, file_paths), ignore_index=True)
        except Exception as e:
            print(f'Error loading CSV files: {e}')
            return

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
