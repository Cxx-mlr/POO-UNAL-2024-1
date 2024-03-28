from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static

from textual.containers import Container
from textual.validation import Number

from utils.widgets import InputWithLabel

from EquilateralTriangle import EquilateralTriangle

class Ejercicio19(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingrese el lado de un triángulo equilátero, se determinará el perímetro, la altura y el área[/][/]",
                id="description-label")
            yield InputWithLabel(
                "[blue]Lado del Triángulo Equilátero:[/]",
                label_width=22,
                type="number",
                id="side-length",
                valid_empty=True,
                validators=[
                    Number(minimum=0, failure_description="El lado del triángulo debe ser un número real no negativo.")
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        if getattr(event.validation_result, "is_valid", True):
            pass
        else:
            self.notify("\n".join(getattr(event.validation_result, "failure_descriptions", [])), severity="error")
            return

        side_length_input = self.query_one("#side-length")

        try:
            side_length = float(side_length_input.value)
        except ValueError:
            self.query_one("#result-label", Static).update("")
        else:
            if side_length_input.value:
                eq_triangle: EquilateralTriangle = EquilateralTriangle(side_length=side_length)
                renderable =  f"[yellow]Se muestra la información del Triángulo Equilátero:[/]" \
                    f"\n\t[magenta]Perímetro[/]: [green]{eq_triangle.calculate_perimeter()}[/]" \
                    f"\n\t[magenta]Altura   [/]: [green]{eq_triangle.calculate_height()}[/]" \
                    f"\n\t[magenta]Área     [/]: [green]{eq_triangle.calculate_area()}[/]"
                self.query_one("#result-label", Static).update(renderable)
            else:
                self.query_one("#result-label", Static).update("")

    @staticmethod
    def main():
        app = Ejercicio19()
        app.run()