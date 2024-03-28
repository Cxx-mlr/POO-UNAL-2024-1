from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static

from textual.containers import Container
from textual.validation import Number

from utils.widgets import InputWithLabel

from Employee import Employee

class Ejercicio22(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingrese los datos del empleado, se determinará el salario mensual[/][/]",
                id="description-label")
            yield InputWithLabel(
                "[blue]Nombre:[/]",
                label_width=22,
                type="text",
                id="name",
                valid_empty=True
            )
            yield InputWithLabel(
                "[blue]Salario Básico por Hora:[/]",
                label_width=22,
                type="number",
                id="hourly-rate",
                valid_empty=True,
                validators=[
                    Number(minimum=0, failure_description="El Salario Básico por Hora debe ser un número real no negativo.")
                ]
            )
            yield InputWithLabel(
                "[blue]Número de Horas Trabajadas en el Mes:[/]",
                label_width=22,
                type="integer",
                id="hours-worked-per-month",
                valid_empty=True,
                validators=[
                    Number(minimum=0, failure_description="Las Horas Trabajadas en el Mes debe ser un número entero no negativo.")
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        if getattr(event.validation_result, "is_valid", True):
            pass
        else:
            self.notify("\n".join(getattr(event.validation_result, "failure_descriptions", [])), severity="error")
            return
        
        name_input = self.query_one("#name", Input)
        hourly_rate_input = self.query_one("#hourly-rate", Input)
        hours_worked_per_month_input = self.query_one("#hours-worked-per-month", Input)

        try:
            name = name_input.value
            hourly_rate = float(hourly_rate_input.value)
            hours_worked_per_month = int(hours_worked_per_month_input.value)
        except ValueError as e:
            self.query_one("#result-label", Static).update("")
        else:
            if all((name_input.value, hourly_rate_input.value, hours_worked_per_month_input.value)):
                employee: Employee = Employee(
                    name=name,
                    hourly_rate=hourly_rate,
                    hours_worked_per_month=hours_worked_per_month
                )

                net_salary = employee.calculate_net_salary()

                renderable = f"[yellow]Se muestra la información del empleado:[/]" \
                    f"\n\t[magenta]Nombre:[/] [blue]{employee.name}[/]"
                
                if net_salary > 450_000:
                    renderable += f"\n\t[magenta]Salario Mensual:[/] [green]${net_salary}[/]"

                self.query_one("#result-label", Static).update(renderable)
            else:
                self.query_one("#result-label", Static).update("")

    @staticmethod
    def main():
        app = Ejercicio22()
        app.run()