from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static
from textual.containers import Container
from textual.validation import Number, Length

from Employee import Employee
from utils.widgets import InputWithLabel

import operator

class Ejercicio22(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static(
                "[i][magenta]Ingrese los datos del empleado, " \
                "se determinará el salario mensual[/][/]",
                id="description-label"
            )
            yield InputWithLabel(
                "[blue]Nombre:[/]",
                label_width=22,
                type="text",
                id="name",
                validators=[
                    Length(
                        minimum=1,
                        failure_description="Este campo es obligatorio"
                    )
                ]
            )
            yield InputWithLabel(
                "[blue]Salario Básico por Hora:[/]",
                label_width=22,
                type="number",
                id="hourly-rate",
                validators=[
                    Length(
                        minimum=1,
                        failure_description="Este campo es obligatorio."
                    ),
                    Number(
                        failure_description="El número ingresado es incorrecto."
                    ),
                    Number(
                        minimum=0,
                        failure_description="El Salario Básico por Hora " \
                                            "debe ser un número real no negativo."
                    )
                ]
            )
            yield InputWithLabel(
                "[blue]Número de Horas Trabajadas en el Mes:[/]",
                label_width=22,
                type="number",
                id="hours-worked-per-month",
                validators=[
                    Length(
                        minimum=1,
                        failure_description="Este campo es obligatorio."
                    ),
                    Number(
                        failure_description="El número ingresado es incorrecto."
                    ),
                    Number(
                        minimum=0,
                        failure_description="Las Horas Trabajadas en el Mes " \
                                            "deben ser un número real no negativo."
                    )
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        result_label = self.query_one("#result-label", Static)
        if not all(map(operator.attrgetter("is_valid"), self.query(InputWithLabel))):
            result_label.update("")
            return
        
        name = self.query_one("#name", Input).value
        hourly_rate = float(self.query_one("#hourly-rate", Input).value)
        hours_worked_per_month = float(self.query_one("#hours-worked-per-month", Input).value)

        employee: Employee = Employee(
            name=name,
            hourly_rate=hourly_rate,
            hours_worked_per_month=hours_worked_per_month
        )

        net_salary = employee.calculate_net_salary()

        #renderable = f"[yellow]Se muestra la información del empleado:[/]" \
        renderable = f"[magenta]Nombre:[/] [blue]{employee.name}[/]"
        
        if net_salary > 450_000:
            renderable += f"\n[magenta]Salario Mensual:[/] [green]${net_salary}[/]"

        result_label.update(renderable)

    @staticmethod
    def main():
        app = Ejercicio22()
        app.run()