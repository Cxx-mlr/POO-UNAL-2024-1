from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static
from textual.containers import Container
from textual.validation import Number, Integer, Length

from Student import Student
from utils.widgets import InputWithLabel

import operator

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
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Integer(minimum=0, failure_description="El Número de Inscripción debe contener únicamente dígitos numéricos.")
                ]
            )
            yield InputWithLabel(
                "[blue]Nombre:",
                label_width=22,
                type="text",
                id="name",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio.")
                ]
            )
            yield InputWithLabel(
                "[blue]Patrimonio:",
                label_width=22,
                type="number",
                id="assets",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="El patrimonio debe ser un número real no negativo.")
                ]
            )
            yield InputWithLabel(
                "[blue]Estrato Social:",
                label_width=22,
                type="integer",
                id="social-stratum",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Integer(failure_description="El número ingresado es incorrecto."),
                    Integer(minimum=1, maximum=6, failure_description="El Estrato Social debe ser un número entero entre 1 y 6.")
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        result_label = self.query_one("#result-label", Static)
        if not all(map(operator.attrgetter("is_valid"), self.query(InputWithLabel))):
            result_label.update("")
            return

        registration_number = self.query_one("#registration-number", Input).value
        name = self.query_one("#name", Input).value
        assets = float(self.query_one("#assets", Input).value)
        social_stratum = float(self.query_one("#social-stratum", Input).value)

        student: Student = Student(
            registration_number=registration_number,
            name=name,
            assets=assets,
            social_stratum=social_stratum
        )
        result_label.update(
            f"El Estudiante con número de inscripción [yellow]{student.registration_number}[/] " \
            f"y nombre [yellow]{student.name}[/] debe pagar [green]${student.calculate_tuition_feed():,}[/]"
        )

    @staticmethod
    def main():
        app = Ejercicio10()
        app.run()