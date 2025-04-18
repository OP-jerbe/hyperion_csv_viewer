import plotly.graph_objects as go
import plotly.io as pio
from pandas import DataFrame, to_datetime
from plotly.graph_objects import Figure


class Plotter:
    def __init__(
        self, title: str, x_axis: str, traces: list[str], data: DataFrame
    ) -> None:
        pio.renderers.default = 'browser'
        self.title = title
        self.x_axis = x_axis
        self.traces = traces
        self.df = data

    def create_fig(self) -> Figure:
        """Creates the plotly figure and applies standard formatting."""
        fig: Figure = Figure()

        data_to_plot = [
            (col, self.df[col].tolist() if col != 'None' else None)
            for col in self.traces
        ]

        time: list = []
        if self.x_axis == 'Time':
            self.df['Time'] = to_datetime(
                self.df['Time'], format='%m/%d/%Y %I:%M:%S %p'
            )
            time = self.df['Time'].tolist()

        axis_colors = ['red', 'white', 'limegreen', 'yellow']

        # Choose position values spaced slightly inside [0, 1]
        position_map = {
            0: 0.90,  # yaxis (right, offset inwards)
            1: 1.00,  # yaxis2 (right, base)
            2: 0.10,  # yaxis3 (left, offset inwards)
            3: 0.00,  # yaxis4 (left, base)
        }

        for i, (column_name, y_data) in enumerate(data_to_plot):
            yaxis_layout_key = 'yaxis' if i == 0 else f'yaxis{i + 1}'
            yaxis_name = f'y{i + 1}'  # y, y2, y3, etc.
            trace_yaxis = 'y' if i == 0 else yaxis_name
            overlaying = 'y' if i > 0 else None
            side = 'right' if i < 2 else 'left'
            anchor = 'x' if i % 2 == 0 else 'free'
            tickformat = '.2e' if column_name == 'Source Pressure (mBar)' else None
            visible = True if column_name != 'None' else False
            x_data = time if self.x_axis == 'Time' else self.df[self.x_axis].tolist()

            yaxis_layout_dict = dict(
                anchor=anchor,
                color=axis_colors[i],
                overlaying=overlaying,
                position=position_map[i],
                showgrid=False,
                side=side,
                tickfont=dict(color=axis_colors[i]),
                tickformat=tickformat,
                title=column_name,
                visible=visible,
                zeroline=False,
            )

            fig.add_trace(
                go.Scatter(
                    x=x_data,
                    y=y_data,
                    line=dict(color=axis_colors[i]),
                    mode='lines',
                    name=column_name,
                    yaxis=trace_yaxis,
                    visible=visible,
                )
            )

            fig.update_layout({yaxis_layout_key: yaxis_layout_dict})

        xaxis_title = self.x_axis
        if xaxis_title == 'Time':
            xaxis_title = None

        fig.update_layout(
            paper_bgcolor='rgba(132,132,132,1)',
            plot_bgcolor='black',
            legend_font_color='black',
            title=dict(text=self.title, font=dict(size=28), x=0.5),
            xaxis_title=xaxis_title,
            legend=dict(
                orientation='h',
                xanchor='center',
                x=0.5,
            ),
            xaxis=dict(domain=[0.05, 0.95], showgrid=False, color='black'),
        )

        return fig
