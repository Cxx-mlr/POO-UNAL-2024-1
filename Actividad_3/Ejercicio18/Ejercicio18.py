from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static

from textual.containers import Container

from utils.widgets import InputWithLabel

from textual.validation import Number, Function

from Employee import Employee

class Ejercicio18(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingrese los datos del empleado, se determinará el salario bruto y el salario neto[/][/]", id="description-label")
            yield InputWithLabel(
                "[blue]Código del Empleado:[/]",
                label_width=22,
                type="text",
                id="id",
                valid_empty=True
            )
            yield InputWithLabel(
                "[blue]Nombre:[/]",
                label_width=22,
                type="text",
                id="name",
                valid_empty=True
            )
            yield InputWithLabel(
                "[blue]Horas Trabajadas al Mes:[/]",
                label_width=22,
                type="number",
                id="hours-worked-per-month",
                valid_empty=True,
                validators=[
                    Number(minimum=0, failure_description="Las Horas Trabajadas al Mes debe ser número entero no negativo.")
                ],
            )
            yield InputWithLabel(
                "[blue]Valor por Hora Trabajada:[/]",
                label_width=22,
                type="number",
                id="hourly-rate",
                validators=[
                    Number(minimum=1, failure_description="El Valor por Hora Trabajada debe ser un número real no negativo.")
                ],
                valid_empty=True
            )
            yield InputWithLabel(
                "[blue]Porcentaje de Retención de la Fuente (%):[/]",
                label_width=22,
                type="number",
                id="withholding-tax-percentage",
                validators=[
                    Number(minimum=0, maximum=100, failure_description="El Porcentaje debe ser un número real entre 0 y 100.")
                ],
                valid_empty=True
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        if not getattr(event.validation_result, "is_valid", True):
            return
        
        id_input = self.query_one("#id", Input)
        name_input = self.query_one("#name", Input)
        hours_worked_per_month_input = self.query_one("#hours-worked-per-month", Input)
        hourly_rate_input = self.query_one("#hourly-rate", Input)
        withholding_tax_percentage_input = self.query_one("#withholding-tax-percentage", Input)

        try:
            id = id_input.value
            name = name_input.value
            hours_worked_per_month = int(hours_worked_per_month_input.value)
            hourly_rate = float(hourly_rate_input.value)
            withholding_tax_percentage = float(withholding_tax_percentage_input.value)
        except ValueError:
            self.query_one("#result-label").update("")
        else:
            if all((
                    id_input.value,
                    name_input.value,
                    hours_worked_per_month_input.value,
                    hourly_rate_input.value,
                    withholding_tax_percentage_input.value)):
                employee: Employee = Employee(
                    id=id,
                    name=name,
                    hours_worked_per_month=hours_worked_per_month,
                    hourly_rate=hourly_rate,
                    withholding_tax_percentage=withholding_tax_percentage
                )
                renderable = f"[yellow]Se muestran los datos del empleado:[/]" \
                    f"\n\t[magenta]Código[/]       : [blue]{employee.id}[/]" \
                    f"\n\t[magenta]Nombre[/]       : [blue]{employee.name}[/]" \
                    f"\n\t[magenta]Salario Bruto[/]: [green]${employee.calculate_gross_salary():,}[/]" \
                    f"\n\t[magenta]Salario Neto[/] : [green]${employee.calculate_net_salary():,}[/]"
                
                self.query_one("#result-label").update(renderable)
            else:
                self.query_one("#result-label").update("")

    @staticmethod
    def main():
        app = Ejercicio18()
        app.run()