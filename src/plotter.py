import plotly.graph_objects as go
import plotly.io as pio
from plotly.graph_objects import Figure
import gui.main_window

pio.renderers.default = 'browser'


class Plotter:
    def __init__(self, title: str, traces: list[str]) -> None:
        self.title = title
        self.traces = traces

    def create_fig(self) -> Figure:
        """Creates the plotly figure and applies standard formatting."""
        fig: Figure = Figure()
        fig.update_layout(
            paper_bgcolor='rgba(132,132,132,1)',
            plot_bgcolor='black',
            legend_font_color='black',
            title=dict(text=self.title, font=dict(size=28), x=0.5),
            legend=dict(
                orientation='h',
                xanchor='center',
                x=0.5,  # value must be between 0 to 1.
            ),
            xaxis=dict(domain=[0, 1], showgrid=False, color='black'),
        )
        return fig
