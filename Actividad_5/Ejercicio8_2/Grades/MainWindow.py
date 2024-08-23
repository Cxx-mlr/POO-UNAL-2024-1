from __future__ import annotations

from textual.app import App, ComposeResult, on
from textual.widgets import Button, Input, Label, Static
from textual.containers import Container, Horizontal

from .Grades import Grades

class MainWindow(App[None]):
    CSS_PATH = "./main.tcss"

    def __init__(self, *args, **kwargs) -> MainWindow:
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        with Container(id="main-panel"):
            with Horizontal():
                yield Label("Nota 1:", classes="label")
                yield Input(id="grade-1", classes="input", type="number", valid_empty=True)

            with Horizontal():
                yield Label("Nota 2:", classes="label")
                yield Input(id="grade-2", classes="input", type="number", valid_empty=True)

            with Horizontal():
                yield Label("Nota 3:", classes="label")
                yield Input(id="grade-3", classes="input", type="number", valid_empty=True)

            with Horizontal():
                yield Label("Nota 4:", classes="label")
                yield Input(id="grade-4", classes="input", type="number", valid_empty=True)

            with Horizontal():
                yield Label("Nota 5:", classes="label")
                yield Input(id="grade-5", classes="input", type="number", valid_empty=True)

            with Horizontal(id="grade-button-container"):
                yield Button("Calcular", id="compute-grade-button", disabled=True)
                yield Button("Limpiar", id="clear-grade-button", variant="error", disabled=True)

            yield Static(
                "Promedio:"
                "\n\nDesviación estándar:"
                "\n\nValor mayor:"
                "\n\nValor menor:",
                id="output"
            )

    @on(Input.Changed)
    async def on_input_changed(self, event: Input.Changed) -> None:
        grade_1 = self.query_one("#grade-1", Input).value
        grade_2 = self.query_one("#grade-2", Input).value
        grade_3 = self.query_one("#grade-3", Input).value
        grade_4 = self.query_one("#grade-4", Input).value
        grade_5 = self.query_one("#grade-5", Input).value

        if all((grade_1, grade_2, grade_3, grade_4, grade_5)):
            self.query_one("#compute-grade-button").disabled = False
        else:
            self.query_one("#compute-grade-button").disabled = True

        if any((grade_1, grade_2, grade_3, grade_4, grade_5)):
            self.query_one("#clear-grade-button").disabled = False
        else:
            self.query_one("#clear-grade-button").disabled = True

    @on(Button.Pressed, "#compute-grade-button")
    async def calculate(self, event: Button.Pressed) -> None:
        grade_1 = float(self.query_one("#grade-1", Input).value)
        grade_2 = float(self.query_one("#grade-2", Input).value)
        grade_3 = float(self.query_one("#grade-3", Input).value)
        grade_4 = float(self.query_one("#grade-4", Input).value)
        grade_5 = float(self.query_one("#grade-5", Input).value)

        grades = Grades()
        grades.grade_list[0] = grade_1
        grades.grade_list[1] = grade_2
        grades.grade_list[2] = grade_3
        grades.grade_list[3] = grade_4
        grades.grade_list[4] = grade_5

        ndigits = 4

        self.query_one("#output", Static).update(
            f"Promedio: {round(grades.calculate_average(), ndigits=ndigits)}"
            f"\n\nDesviación estándar: {round(grades.calculate_standard_deviation(), ndigits=ndigits)}"
            f"\n\nValor mayor: {round(grades.calculate_max(), ndigits=ndigits)}"
            f"\n\nValor menor: {round(grades.calculate_min(), ndigits=ndigits)}"
        )

    @on(Button.Pressed, "#clear-grade-button")
    async def clear(self, event: Button.Pressed) -> None:
        self.query_one("#grade-1", Input).value = ""
        self.query_one("#grade-2", Input).value = ""
        self.query_one("#grade-3", Input).value = ""
        self.query_one("#grade-4", Input).value = ""
        self.query_one("#grade-5", Input).value = ""

        self.query_one("#output", Static).update(
            "Promedio:"
            "\n\nDesviación estándar:"
            "\n\nValor mayor:"
            "\n\nValor menor:",
        )