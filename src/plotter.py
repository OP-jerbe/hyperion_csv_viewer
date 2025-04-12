import plotly.express as px


class Plotter:
    def __init__(self, df) -> None:
        self.df = df

    def plot(self, x_col: str, y_col: str) -> None:
        fig = px.line(self.df, x=x_col, y=y_col, title='Time Series Plot')
        fig.show()
