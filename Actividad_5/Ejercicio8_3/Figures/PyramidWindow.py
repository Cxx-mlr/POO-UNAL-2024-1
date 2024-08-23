from __future__ import annotations

from textual.app import ComposeResult, on
from textual.widgets import Label, Static, Input, Button
from textual.containers import Horizontal, Container

from .Pyramid import Pyramid

class PyramidWindow(Static):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label("Base (cms):")
            yield Input(id="base")

        with Horizontal():
            yield Label("Altura (cms):")
            yield Input(id="height")

        with Horizontal():
            yield Label("Apotema (cms):")
            yield Input(id="apothem")

        with Container():
            yield Button("Calcular", id="calculate-button", disabled=True)

        yield Static("Volumen (cm3):\n\nSuperficie (cm2):", id="output")

    @on(Input.Changed)
    def on_input_changed(self, event: Input.Changed) -> None:
        base = self.query_one("#base", Input).value
        height = self.query_one("#height", Input).value
        apothem = self.query_one("#apothem", Input).value

        if all((base, height, apothem)):
            self.query_one("#calculate-button").disabled = False
        else:
            self.query_one("#calculate-button").disabled = True

    @on(Button.Pressed, "#calculate-button")
    def calculate(self, event: Button.Pressed) -> None:
        base = float(self.query_one("#base", Input).value)
        height = float(self.query_one("#height", Input).value)
        apothem = float(self.query_one("#apothem", Input).value)

        pyramid = Pyramid(base=base, height=height, apothem=apothem)

        ndigits = 4

        self.query_one("#output", Static).update(
            f"Volumen (cm3): {round(pyramid.get_volume(), ndigits=ndigits)}"
            f"\n\nSuperficie (cm2): {round(pyramid.get_surface_area(), ndigits=ndigits)}"
        )