from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static

from textual.containers import Container
from textual.validation import Number, Length

from utils.widgets import InputWithLabel

from EquilateralTriangle import EquilateralTriangle
import operator

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
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="El lado del triángulo debe ser un número real no negativo.")
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        result_label = self.query_one("#result-label", Static)
        if not all(map(operator.attrgetter("is_valid"), self.query(InputWithLabel))):
            result_label.update("")
            return

        side_length = float(self.query_one("#side-length").value)

        eq_triangle: EquilateralTriangle = EquilateralTriangle(side_length=side_length)
        #renderable =  f"[yellow]Se muestra la información del Triángulo Equilátero:[/]" \
        renderable = f"[magenta]Perímetro[/]: [green]{eq_triangle.calculate_perimeter()}[/]" \
            f"\n[magenta]Altura   [/]: [green]{eq_triangle.calculate_height()}[/]" \
            f"\n[magenta]Área     [/]: [green]{eq_triangle.calculate_area()}[/]"
        result_label.update(renderable)

    @staticmethod
    def main():
        app = Ejercicio19()
        app.run()