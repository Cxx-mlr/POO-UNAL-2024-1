from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static

from textual.containers import Container
from textual.validation import Number, Function

from utils.widgets import InputWithLabel

from QuadraticEquation import QuadraticEquation
import math

class Ejercicio23(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingrese los coeficientes de una ecuación" \
                         " de segundo grado, se determinarán las raíces de dicha ecuación[/][/]",
                id="description-label")
            yield InputWithLabel(
                "[blue]Coeficiente a:[/]",
                label_width=22,
                type="number",
                id="coefficient-a",
                valid_empty=True,
                validators=[
                    Function(lambda x: not Ejercicio23.is_zero(x), failure_description="El coeficiente 'a' debe ser distinto de cero.")
                ]
            )
            yield InputWithLabel(
                "[blue]Coeficiente b:[/]",
                label_width=22,
                type="number",
                id="coefficient-b",
                valid_empty=True,
            )
            yield InputWithLabel(
                "[blue]Coeficiente c:[/]",
                label_width=22,
                type="number",
                id="coefficient-c",
                valid_empty=True,
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        if getattr(event.validation_result, "is_valid", True):
            pass
        else:
            self.notify("\n".join(getattr(event.validation_result, "failure_descriptions", [])), severity="error")
            return
        
        a_input = self.query_one("#coefficient-a", Input)
        b_input = self.query_one("#coefficient-b", Input)
        c_input = self.query_one("#coefficient-c", Input)

        try:
            a = float(a_input.value)
            b = float(b_input.value)
            c = float(c_input.value)
        except ValueError:
            self.query_one("#result-label", Static).update("")
        else:
            if all((a_input.value, b_input.value, c_input.value)):
                quadratic_equation = QuadraticEquation(a=a, b=b, c=c)
                discriminant = quadratic_equation.calculate_discriminant()

                renderable = ""

                if discriminant < 0:
                    renderable += "[red]La ecuación no tiene solución en los números reales.[/]"
                else:
                    x_1 = (-quadratic_equation.b + math.sqrt(discriminant))/(2 * quadratic_equation.a)
                    if discriminant == 0:
                        renderable += "[green]La solución a la ecuación de segundo grado es:[/]" \
                            f"[magenta]\n\tx_1 = {x_1}[/]"
                    else:
                        x_2 = (-quadratic_equation.b - math.sqrt(discriminant))/(2 * quadratic_equation.a)
                        renderable += "[green]Las soluciones a la ecuación de segundo grado son:[/]" \
                            f"[magenta]\n\tx_1 = {x_1}" \
                            f"\n\tx_2 = {x_2}[/]"
                self.query_one("#result-label", Static).update(renderable)
            else:
                self.query_one("#result-label", Static).update("")

    @staticmethod
    def is_zero(value: str) -> bool:
        try:
            value_f = float(value)
        except ValueError:
            return False
        else:
            return value_f == 0

    @staticmethod
    def main():
        app = Ejercicio23()
        app.run()