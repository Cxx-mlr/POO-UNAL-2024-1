from __future__ import annotations

from textual.app import ComposeResult, on
from textual.widgets import Label, Static, Input, Button
from textual.containers import Horizontal, Container

from .Cylinder import Cylinder

class CylinderWindow(Static):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label("Radio (cms):")
            yield Input(id="radius")

        with Horizontal():
            yield Label("Altura (cms):")
            yield Input(id="height")

        with Container():
            yield Button("Calcular", id="calculate-button", disabled=True)

        yield Static("Volumen (cm3):\n\nSuperficie (cm2):", id="output")

    @on(Input.Changed)
    def on_input_changed(self, event: Input.Changed) -> None:
        radius = self.query_one("#radius", Input).value
        height = self.query_one("#height", Input).value

        if all((radius, height)):
            self.query_one("#calculate-button").disabled = False
        else:
            self.query_one("#calculate-button").disabled = True

    @on(Button.Pressed, "#calculate-button")
    def calculate(self, event: Button.Pressed) -> None:
        radius = float(self.query_one("#radius", Input).value)
        height = float(self.query_one("#height", Input).value)

        cylinder = Cylinder(radius=radius, height=height)

        ndigits = 4

        self.query_one("#output", Static).update(
            f"Volumen (cm3): {round(cylinder.get_volume(), ndigits=ndigits)}"
            f"\n\nSuperficie (cm2): {round(cylinder.get_surface_area(), ndigits=ndigits)}"
        )