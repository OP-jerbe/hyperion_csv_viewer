from PySide6.QtCore import QThread, Signal
from plotly.graph_objects import Figure
from plotter import Plotter


class PlotWorker(QThread):
    finished = Signal(Figure)

    def __init__(
        self,
        title: str,
        traces: list[str],
        data,
        show: bool = True,
        write_html: bool = False,
        save_loc: str | None = None,
    ) -> None:
        super().__init__()
        self.title = title
        self.traces = traces
        self.data = data
        self.show = show
        self.write_html = write_html
        self.save_loc = save_loc

    def run(self) -> None:
        plotter = Plotter(self.title, self.traces, self.data)
        fig = plotter.create_fig()
        if self.show:
            fig.show()
        if self.write_html:
            fig.write_html(self.save_loc)
        self.finished.emit(fig)
