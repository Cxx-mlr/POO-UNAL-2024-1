from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Input, Label, Header, Static

from textual.containers import Container

class Ejercicio7(App[None]):
    CSS_PATH = "./main.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static(
                "[i]Ingrese dos números, se determinará si el " \
                "primer número ingresado es [green][u]mayor[/][/], " \
                "[red][u]menor[/][/] o [blue][u]igual[/][/] que el segundo número[/i]",
                id="description-label")
            yield Input(id="a", type="number", placeholder="Ingrese el primer número...", valid_empty=True)
            yield Input(id="b", type="number", placeholder="Ingrese el segundo número...", valid_empty=True)
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        if getattr(event.validation_result, "is_valid", True):
            pass
        else:
            self.notify("\n".join(getattr(event.validation_result, "failure_descriptions", [])), severity="error")
        
        a_input = self.query_one("#a", Input)
        b_input = self.query_one("#b", Input)

        try:
            a = float(a_input.value)
            b = float(b_input.value)
        except ValueError:
            self.query_one("#result-label", Static).update("")
        else:
            if all((a_input.value, b_input.value)):
                if float(a).is_integer(): a = int(a)
                if float(b).is_integer(): b = int(b)

                if a < b:
                    self.query_one("#result-label", Static).update(f"[i]{a} es [red][u]menor[/][/] que {b}[/]")
                elif a == b:
                    self.query_one("#result-label", Static).update(f"[i]{a} es [blue][u]igual[/][/] a {b}[/]")
                else:
                    self.query_one("#result-label", Static).update(f"[i]{a} es [green][u]mayor[/][/] que {b}[/]")
            else:
                self.query_one("#result-label", Static).update("")

    @staticmethod
    def main():
        app = Ejercicio7()
        app.run()