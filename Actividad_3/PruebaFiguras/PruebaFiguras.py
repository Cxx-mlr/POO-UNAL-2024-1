from __future__ import annotations

from textual.app import App, ComposeResult
from textual.widgets import Input, Header, Static

from textual.containers import Container
from textual.validation import Number

from utils.widgets import InputWithLabel


from Círculo import Círculo
from Rectángulo import Rectángulo
from Cuadrado import Cuadrado
from TriánguloRectángulo import TriánguloRectángulo

class PruebaFiguras(App[None]):
    CSS_PATH = "./main.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="main-panel"):
            yield Static("[i][magenta]Ingresa los datos para crear las figuras geométricas[/][/]", id="description-label")

            yield Static("[blue on black]Círculo")
            yield InputWithLabel("[blue]Radio:[/]", label_width=22, type="number", id="circle-radius", validators=[Number(minimum=0, failure_description="El {} debe ser un número real no negativo.")], valid_empty=True)

            yield Static("[yellow on black]Rectángulo")
            yield InputWithLabel("[yellow]Base:[/]", label_width=22, type="number", id="rectangle-base", validators=[Number(minimum=0, failure_description="El {} debe ser un número real no negativo.")], valid_empty=True)
            yield InputWithLabel("[yellow]Altura:[/]", label_width=22, type="number", id="rectangle-height", validators=[Number(minimum=0, failure_description="El {} debe ser un número real no negativo.")], valid_empty=True)

            yield Static("[green on black]Cuadrado")
            yield InputWithLabel("[green]Lado:[/]", label_width=22, type="number", id="square-side", validators=[Number(minimum=0, failure_description="El {} debe ser un número real no negativo.")], valid_empty=True)

            yield Static("[red on black]Triángulo Rectángulo")
            yield InputWithLabel("[red]Base:[/]", label_width=22, type="number", id="triangle-base", validators=[Number(minimum=0, failure_description="El {} debe ser un número real no negativo.")], valid_empty=True)
            yield InputWithLabel("[red]Altura:[/]", label_width=22, type="number", id="triangle-height", validators=[Number(minimum=0, failure_description="El {} debe ser un número real no negativo.")], valid_empty=True)
            
            yield Static(id="result-label")

    def on_input_changed(self, event: Input.Changed):
        if getattr(event.validation_result, "is_valid", True):
            pass
        else:
            self.notify("\n".join(getattr(event.validation_result, "failure_descriptions", [])), severity="error")

        circle_radius_input = self.query_one("#circle-radius", Input)
        rectangle_base_input = self.query_one("#rectangle-base", Input)
        rectangle_height_input = self.query_one("#rectangle-height", Input)
        square_side_input = self.query_one("#square-side", Input)
        triangle_base_input = self.query_one("#triangle-base", Input)
        triangle_height_input = self.query_one("#triangle-height", Input)

        try:
            circle_radius = float(circle_radius_input.value)
            rectangle_base = float(rectangle_base_input.value)
            rectangle_height = float(rectangle_height_input.value)
            square_side = float(square_side_input.value)
            triangle_base = float(triangle_base_input.value)
            triangle_height = float(triangle_height_input.value)
        except ValueError:
            self.query_one("#result-label").update("")
        else:
            if all((circle_radius_input.value,
                    rectangle_base_input.value,
                    rectangle_height_input.value,
                    square_side_input.value,
                    triangle_base_input.value,
                    triangle_height_input.value)):
                
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
                self.query_one("#result-label").update(renderable)
            else:
                self.query_one("#result-label").update("")
        

    @staticmethod
    def main():
        app = PruebaFiguras()
        app.run()