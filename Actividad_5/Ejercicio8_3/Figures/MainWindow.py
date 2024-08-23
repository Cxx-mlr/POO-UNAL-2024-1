from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane

from .CylinderWindow import CylinderWindow
from .PyramidWindow import PyramidWindow
from .SphereWindow import SphereWindow

class MainWindow(App[None]):
    CSS_PATH = "./main.tcss"

    def __init__(self, *args, **kwargs) -> MainWindow:
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        with TabbedContent(id="main-panel"):
            with TabPane("Cilindro"):
                yield CylinderWindow(classes="window")
            with TabPane("Esfera"):
                yield SphereWindow(classes="window")
            with TabPane("Pirámide"):
                yield PyramidWindow(classes="window")