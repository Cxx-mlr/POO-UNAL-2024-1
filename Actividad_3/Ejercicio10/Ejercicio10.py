from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static

from textual.containers import Container

from Student import Student
from utils.widgets import InputWithLabel

from textual.validation import Number, Function

class Ejercicio10(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingrese los datos del estudiante, se determinará el costo de matrícula[/][/]", id="description-label")
            yield InputWithLabel(
                "[blue]Número de Inscripción:[/]",
                label_width=22,
                type="text",
                id="registration-number",
                validators=[
                   Function(Ejercicio10.is_valid_integer, "El Número de Inscripción debe contener únicamente dígitos numéricos.")
                ],
                valid_empty=True
            )
            yield InputWithLabel(
                "[blue]Nombre:",
                label_width=22,
                type="text",
                id="name",
                valid_empty=True
            )
            yield InputWithLabel(
                "[blue]Patrimonio:",
                label_width=22,
                type="number",
                id="assets",
                valid_empty=True,
                validators=[
                    Number(minimum=0, failure_description="El patrimonio debe ser un número real no negativo.")
                ]
            )
            yield InputWithLabel(
                "[blue]Estrato Social:",
                label_width=22,
                type="integer",
                id="social-stratum",
                validators=[
                    Number(minimum=1, maximum=6, failure_description="El Estrato Social debe ser un número entero entre 1 y 6.")
                ],
                valid_empty=True
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        if not getattr(event.validation_result, "is_valid", True):
            return

        registration_number_input = self.query_one("#registration-number", Input)
        name_input = self.query_one("#name", Input)
        assets_input = self.query_one("#assets", Input)
        social_stratum_input = self.query_one("#social-stratum", Input) 

        try:
            registration_number = registration_number_input.value
            name = name_input.value
            assets = float(assets_input.value)
            social_stratum = int(social_stratum_input.value)
        except:
            self.query_one("#result-label", Static).update("")
        else:
            if all((registration_number_input.value, name_input.value, assets_input.value, social_stratum_input.value)):
                student: Student = Student(
                    registration_number=registration_number,
                    name=name,
                    assets=assets,
                    social_stratum=social_stratum
                )
                self.query_one("#result-label", Static).update(
                    f"El Estudiante con número de inscripción [yellow]{student.registration_number}[/] " \
                    f"y nombre [yellow]{student.name}[/] debe pagar [green]${student.calculate_tuition_feed():,}[/]"
                )
            else:
                self.query_one("#result-label", Static).update("")

    @staticmethod
    def is_valid_integer(value: str) -> bool:
        try:
            _ = int(value)
        except ValueError:
            return False
        else:
            return _ >= 0

    @staticmethod
    def main():
        app = Ejercicio10()
        app.run()