from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static
from textual.containers import Container
from textual.validation import Number, Length

from utils.widgets import InputWithLabel

import operator

class Ejercicio7(App[None]):
    CSS_PATH = "./main.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static(
                "[i]Ingrese dos números, se determinará si el " \
                "primer número ingresado es [green][u]mayor[/][/], " \
                "[red][u]menor[/][/] o [blue][u]igual[/][/] que el segundo número[/i]",
                id="description-label"
            )
            yield InputWithLabel(
                id="first",
                type="number",
                placeholder="Ingrese el primer número...",
                validators=[
                    Length(
                        minimum=1,
                        failure_description="Este campo es obligatorio."
                    ),
                    Number(
                        failure_description="El número ingresado es incorrecto."
                    )
                ]
            )
            yield InputWithLabel(
                id="second",
                type="number",
                placeholder="Ingrese el segundo número...",
                validators=[
                    Length(
                        minimum=1,
                        failure_description="Este campo es obligatorio."
                    ),
                    Number(
                        failure_description="El número ingresado es incorrecto."
                    )
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        result_label = self.query_one("#result-label", Static)
        if not all(map(operator.attrgetter("is_valid"), self.query(InputWithLabel))):
            result_label.update("")
            return
        
        first = float(self.query_one("#first", Input).value)
        second = float(self.query_one("#second", Input).value)

        if first.is_integer(): first = int(first)
        if second.is_integer(): second = int(second)

        if first < second:
            result_label.update(f"[i]{first} es [red][u]menor[/][/] que {second}[/]")
        elif first == second:
            result_label.update(f"[i]{first} es [blue][u]igual[/][/] a {second}[/]")
        else:
            result_label.update(f"[i]{first} es [green][u]mayor[/][/] que {second}[/]")

    @staticmethod
    def main():
        app = Ejercicio7()
        app.run()