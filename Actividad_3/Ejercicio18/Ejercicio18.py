from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static
from textual.containers import Container
from textual.validation import Number, Integer, Length

from Employee import Employee
from utils.widgets import InputWithLabel

import operator

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
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Integer(minimum=0, failure_description="El Código del Empleado debe contener únicamente dígitos numéricos.")
                ]
            )
            yield InputWithLabel(
                "[blue]Nombre:[/]",
                label_width=22,
                type="text",
                id="name",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio.")
                ]
            )
            yield InputWithLabel(
                "[blue]Horas Trabajadas al Mes:[/]",
                label_width=22,
                type="number",
                id="hours-worked-per-month",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="Las Horas Trabajadas al Mes deben ser un número real no negativo.")
                ]
            )
            yield InputWithLabel(
                "[blue]Valor por Hora Trabajada:[/]",
                label_width=22,
                type="number",
                id="hourly-rate",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="El Valor por Hora Trabajada debe ser un número real no negativo.")
                ]
            )
            yield InputWithLabel(
                "[blue]Porcentaje de Retención de la Fuente (%):[/]",
                label_width=22,
                type="number",
                id="withholding-tax-percentage",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, maximum=100, failure_description="El Porcentaje de Retención debe ser un número real entre 0 y 100.")
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        result_label = self.query_one("#result-label", Static)
        if not all(map(operator.attrgetter("is_valid"), self.query(InputWithLabel))):
            result_label.update("")
            return
        
        id = self.query_one("#id", Input).value
        name = self.query_one("#name", Input).value
        hours_worked_per_month = float(self.query_one("#hours-worked-per-month", Input).value)
        hourly_rate = float(self.query_one("#hourly-rate", Input).value)
        withholding_tax_percentage = float(self.query_one("#withholding-tax-percentage", Input).value)

        employee: Employee = Employee(
            id=id,
            name=name,
            hours_worked_per_month=hours_worked_per_month,
            hourly_rate=hourly_rate,
            withholding_tax_percentage=withholding_tax_percentage
        )
        #renderable = f"[yellow]Se muestran los datos del empleado:[/]" \
        renderable = f"[magenta]Código[/]       : [blue]{employee.id}[/]" \
            f"\n[magenta]Nombre[/]       : [blue]{employee.name}[/]" \
            f"\n[magenta]Salario Bruto[/]: [green]${employee.calculate_gross_salary():,}[/]" \
            f"\n[magenta]Salario Neto[/] : [green]${employee.calculate_net_salary():,}[/]"
        
        result_label.update(renderable)

    @staticmethod
    def main():
        app = Ejercicio18()
        app.run()