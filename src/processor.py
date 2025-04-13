from pandas import DataFrame


class DataProcessor:
    """
    A class to process data for analysis.
    """

    def __init__(self, df) -> None:
        self.df: DataFrame = df

    def clean(self) -> DataFrame:
        """Fixes poorly/improperly named headers in hyperion csv file.
        Also converts pressure units from Pascal to mBar if applicable."""
        try:
            self.df.rename(
                columns={'Angular Intensity (mA/str)': 'Angular Intensity (mA/sr)'},
                inplace=True,
            )
        except:
            pass
        try:
            self.df.rename(
                columns={'Beam Voltage (kV)': 'Beam Voltage (V)'}, inplace=True
            )
        except:
            pass
        try:
            self.df.rename(
                columns={'Extractor Voltage (kV)': 'Extractor Voltage (V)'},
                inplace=True,
            )
        except:
            pass
        try:
            self.df.rename(
                columns={'Extractor Current (uA)': 'Extractor Current (μA)'},
                inplace=True,
            )
        except:
            pass
        try:
            self.df.rename(
                columns={'Beam Supply Current (uA)': 'Beam Supply Current (μA)'},
                inplace=True,
            )
        except:
            pass
        try:
            self.df.rename(
                columns={'Lens #1 Current (uA)': 'Lens Current (μA)'}, inplace=True
            )
        except:
            pass
        try:
            self.df.rename(
                columns={'Lens #1 Voltage (V)': 'Lens Voltage (V)'}, inplace=True
            )
        except:
            pass
        try:
            self.df.rename(
                columns={'Lens #1 Voltage (kV)': 'Lens Voltage (V)'}, inplace=True
            )
        except:
            pass

        return self.df

    def _check_for_time_header(self) -> bool:
        """Checks that 'Time' is in headers list"""
        has_time_header: bool = False
        strings: tuple[str] = ('Time',)
        for string in strings:
            if string in self.df.columns:
                has_time_header = True
        return has_time_header

    def strip_Time(self) -> list[str]:
        """Removes the 'Time' column header from the list of headers in the DataFrame."""
        df_headers: list[str] = self.df.columns.tolist()
        time_header: bool = self._check_for_time_header()
        if time_header is True:
            df_headers.remove('Time')
        return df_headers
