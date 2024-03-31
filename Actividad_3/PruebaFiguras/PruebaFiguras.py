from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static
from textual.containers import Container
from textual.validation import Number, Length

from Círculo import Círculo
from Rectángulo import Rectángulo
from Cuadrado import Cuadrado
from TriánguloRectángulo import TriánguloRectángulo
from utils.widgets import InputWithLabel

import operator

class PruebaFiguras(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingresa los datos para crear las figuras geométricas[/][/]", id="description-label")

            yield Static("[blue on black]Círculo")
            yield InputWithLabel(
                "[blue]Radio:[/]",
                label_width=22,
                type="number",
                id="circle-radius",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="Ingrese un número real no negativo.")
                ]
            )

            yield Static("[yellow on black]Rectángulo")
            yield InputWithLabel(
                "[yellow]Base:[/]",
                label_width=22,
                type="number",
                id="rectangle-base",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="Ingrese un número real no negativo.")
                ]
            )
            yield InputWithLabel(
                "[yellow]Altura:[/]",
                label_width=22,
                type="number",
                id="rectangle-height",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="Ingrese un número real no negativo.")
                ]
            )

            yield Static("[green on black]Cuadrado")
            yield InputWithLabel(
                "[green]Lado:[/]",
                label_width=22,
                type="number",
                id="square-side",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="Ingrese un número real no negativo.")
                ]
            )

            yield Static("[red on black]Triángulo Rectángulo")
            yield InputWithLabel(
                "[red]Base:[/]",
                label_width=22,
                type="number",
                id="triangle-base",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="Ingrese un número real no negativo.")
                ]
            )
            yield InputWithLabel(
                "[red]Altura:[/]",
                label_width=22,
                type="number",
                id="triangle-height",
                validators=[
                    Length(minimum=1, failure_description="Este campo es obligatorio."),
                    Number(failure_description="El número ingresado es incorrecto."),
                    Number(minimum=0, failure_description="Ingrese un número real no negativo.")
                ]
            )
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        result_label = self.query_one("#result-label", Static)
        if not all(map(operator.attrgetter("is_valid"), self.query(InputWithLabel))):
            result_label.update("")
            return

        circle_radius = float(self.query_one("#circle-radius", Input).value)
        rectangle_base = float(self.query_one("#rectangle-base", Input).value)
        rectangle_height = float(self.query_one("#rectangle-height", Input).value)
        square_side = float(self.query_one("#square-side", Input).value)
        triangle_base = float(self.query_one("#triangle-base", Input).value)
        triangle_height = float(self.query_one("#triangle-height", Input).value)

        círculo: Círculo = Círculo(circle_radius)
        rectángulo: Rectángulo = Rectángulo(rectangle_base, rectangle_height)
        cuadrado: Cuadrado = Cuadrado(square_side)
        triángulo_rectángulo: TriánguloRectángulo = TriánguloRectángulo(triangle_base, triangle_height)

        renderable = f"El área del círculo es = {círculo.calcularÁrea()}" \
            f"\nEl perímetro del círculo es = {círculo.calcularPerímetro()}"

        renderable += f"\n\nEl área del rectángulo es = {rectángulo.calcularÁrea()}" \
            f"\nEl perímetro del rectángulo es = {rectángulo.calcularPerímetro()}"

        renderable += f"\n\nEl área del cuadrado es = {cuadrado.calcularÁrea()}" \
            f"\nEl perímetro del cuadrado es = {cuadrado.calcularPerímetro()}"
        
        renderable += f"\n\nEl área del triángulo es = {triángulo_rectángulo.calcularÁrea()}" \
            f"\nEl perímetro del triángulo es = {triángulo_rectángulo.calcularPerímetro()}"
        renderable += f"\n{triángulo_rectángulo.determinarTipoTriángulo()}"
        result_label.update(renderable)

    @staticmethod
    def main():
        app = PruebaFiguras()
        app.run()