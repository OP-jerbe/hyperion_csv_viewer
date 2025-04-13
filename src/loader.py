import pandas as pd
from pandas import DataFrame
from PySide6.QtWidgets import QFileDialog
import sys


class DataLoader:
    def _get_file_paths(self) -> list[str]:
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

        caption = 'Choose CSV Files'
        initial_dir = dir
        file_types = 'CSV Files (*.csv);;All Files (*)'
        # Open the file dialog
        file_paths, _ = QFileDialog.getOpenFileNames(
            None,  # Parent widget, can be None
            caption,  # Dialog title
            initial_dir,  # Initial directory
            file_types,  # Filter for file types
        )

        return file_paths

    def load_data(self, file_paths: list[str]) -> DataFrame | None:
        """
        Load CSV data from the specified file path.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            pd.DataFrame: The loaded DataFrame.
        """
        # Load the CSV file into a DataFrame
        file_paths = self._get_file_paths()
        if not file_paths:
            return None
        df = pd.concat(map(pd.read_csv, file_paths), ignore_index=True)

        return df
