from __future__ import annotations

from textual.app import App, ComposeResult, on
from textual.widgets import Button, Input, Label, ListView
from textual.containers import Container, Horizontal

from faker import Faker

fake = Faker(["es_CO"])

from .PersonList import PersonList
from .Person import Person

class MainWindow(App[None]):
    CSS_PATH = "./main.tcss"

    def __init__(self, *args, **kwargs) -> MainWindow:
        super().__init__(*args, **kwargs)
        self.__person_list: PersonList = PersonList()

    def compose(self) -> ComposeResult:
        with Container(id="main-panel"):
            with Horizontal():
                yield Label("Nombre:", classes="label")
                yield Input(id="first-name", classes="input")

            with Horizontal():
                yield Label("Apellidos:", classes="label")
                yield Input(id="last-name", classes="input")

            with Horizontal():
                yield Label("Teléfono:", classes="label")
                yield Input(id="phone", classes="input")

            with Horizontal():
                yield Label("Dirección:", classes="label")
                yield Input(id="address", classes="input")

            with Horizontal(id="add-container"):
                yield Button("Añadir", id="add-button", disabled=True)
                yield Button("Random", id="random-button", variant="primary")

            yield self.__person_list

            with Horizontal(id="remove-container"):
                yield Button("Eliminar", id="remove-button", disabled=True)
                yield Button("Borrar Lista", id="clear-button", variant="error", disabled=True)

    @on(ListView.Selected)
    def on_person_selected(self, event: ListView.Selected) -> None:
        self.query_one("#remove-button", Button).disabled = False

    @on(Input.Changed)
    async def on_input_changed(self, event: Input.Changed) -> None:
        first_name = self.query_one("#first-name", Input).value
        last_name = self.query_one("#last-name", Input).value
        phone = self.query_one("#phone", Input).value
        address = self.query_one("#address", Input).value

        if all((first_name, last_name, phone, address)):
            self.query_one("#add-button").disabled = False
        else:
            self.query_one("#add-button").disabled = True

    @on(Button.Pressed, "#random-button")
    async def fill_random_person(self, event: Button.Pressed) -> None:
        self.query_one("#first-name", Input).value = fake.first_name()
        self.query_one("#last-name", Input).value = f"{fake.last_name()} {fake.last_name()}"
        self.query_one("#phone", Input).value = fake.phone_number()
        self.query_one("#address", Input).value = fake.address().translate(str.maketrans("\n", " "))

    @on(Button.Pressed, "#add-button")
    async def add_person(self, event: Button.Pressed) -> None:
        first_name_input = self.query_one("#first-name", Input)
        last_name_input = self.query_one("#last-name", Input)
        phone_input = self.query_one("#phone", Input)
        address_input = self.query_one("#address", Input)

        person = Person(
            first_name=first_name_input.value,
            last_name=last_name_input.value,
            phone=phone_input.value,
            address=address_input.value
        )

        await self.__person_list.add_person(person)

        first_name_input.value = ""
        last_name_input.value = ""
        phone_input.value = ""
        address_input.value = ""

        self.query_one("#clear-button", Button).disabled = False

    @on(Button.Pressed, "#remove-button")
    async def remove_currently_selected_person(self, event: Button.Pressed) -> None:
        await self.__person_list.remove_currently_selected_person()

        self.query_one("#clear-button", Button).disabled = self.__person_list.is_empty()

        if self.__person_list.is_empty():
            self.query_one("#remove-button", Button).disabled = True

    @on(Button.Pressed, "#clear-button")
    async def clear(self, event: Button.Pressed) -> None:
        self.__person_list.clear()

        self.query_one("#clear-button", Button).disabled = True
        self.query_one("#remove-button", Button).disabled = True