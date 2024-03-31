from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static
from textual.containers import Container
from textual.validation import Number, Function, Length

from QuadraticEquation import QuadraticEquation
from utils.widgets import InputWithLabel

import operator
import math

class Ejercicio23(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingrese los coeficientes de una ecuación" \
                         " de segundo grado, se determinarán las raíces de dicha ecuación[/][/]", id="description-label")
            yield InputWithLabel(
                "[blue]Coeficiente a:[/]",
                label_width=22,
                type="number",
                id="coefficient-a",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Function(lambda x: x.strip() != "0", failure_description="Ingrese un número distinto de 0."),
                ]
            )
            yield InputWithLabel(
                "[blue]Coeficiente b:[/]",
                label_width=22,
                type="number",
                id="coefficient-b",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto.")
                ]
            )
            yield InputWithLabel(
                "[blue]Coeficiente c:[/]",
                label_width=22,
                type="number",
                id="coefficient-c",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto.")
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        result_label = self.query_one("#result-label", Static)
        if not all(map(operator.attrgetter("is_valid"), self.query(InputWithLabel))):
            result_label.update("")
            return
        
        a = float(self.query_one("#coefficient-a", Input).value)
        b = float(self.query_one("#coefficient-b", Input).value)
        c = float(self.query_one("#coefficient-c", Input).value)

        quadratic_equation = QuadraticEquation(a=a, b=b, c=c)
        discriminant = quadratic_equation.calculate_discriminant()

        if discriminant < 0:
            renderable = "[red]La ecuación no tiene solución en los números reales.[/]"
        else:
            x_1 = (-quadratic_equation.b + math.sqrt(discriminant))/(2 * quadratic_equation.a)
            if discriminant == 0:
                renderable = "[green]La solución a la ecuación de segundo grado es:[/]" \
                    f"[magenta]\n\tx_1 = {x_1}[/]"
            else:
                x_2 = (-quadratic_equation.b - math.sqrt(discriminant))/(2 * quadratic_equation.a)
                renderable = "[green]Las soluciones a la ecuación de segundo grado son:[/]" \
                    f"[magenta]\n\tx_1 = {x_1}" \
                    f"\n\tx_2 = {x_2}[/]"
        result_label.update(renderable)

    @staticmethod
    def main():
        app = Ejercicio23()
        app.run()