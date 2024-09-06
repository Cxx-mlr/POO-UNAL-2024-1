from __future__ import annotations

from textual.app import App, ComposeResult, on
from textual.widgets import Button, Input, Label
from textual.containers import Container, Horizontal, Vertical

from .ContactService import ContactService

class MainWindow(App[None]):
    CSS_PATH = "./main.tcss"

    def __init__(self, *args, **kwargs) -> MainWindow:
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        with Container(id="main-panel"):
            with Horizontal():
                yield Label("Name:", classes="label")
                yield Input(id="name", classes="input", type="text", valid_empty=True)

            with Horizontal():
                yield Label("Phone Number:", classes="label")
                yield Input(id="phone-number", classes="input", type="text", valid_empty=True)

            with Vertical(id="buttons-container"):
                with Horizontal(id="crud-buttons-container"):
                    yield Button("Create", id="create-button", variant="primary", disabled=True)
                    yield Button("Read", id="read-button", variant="primary", disabled=True)
                    yield Button("Update", id="update-button", variant="primary", disabled=True)
                    yield Button("Delete", id="delete-button", variant="error", disabled=True)
                yield Button("Clear", id="clear-button", variant="default")

    @on(Input.Changed)
    async def on_input_changed(self, event: Input.Changed) -> None:
        name: str = self.query_one("#name", Input).value
        phone_number: str = self.query_one("#phone-number", Input).value

        def is_empty(value: str):
            return value == ""

        self.query_one("#create-button", Button).disabled = is_empty(name) or is_empty(phone_number)
        self.query_one("#update-button", Button).disabled = is_empty(name) or is_empty(phone_number)

        self.query_one("#read-button", Button).disabled = is_empty(name)
        self.query_one("#clear-button", Button).disabled = is_empty(name)
        self.query_one("#delete-button", Button).disabled = is_empty(name)

    @on(Button.Pressed, "#create-button")
    async def add_contact(self, event: Button.Pressed) -> None:
        with ContactService(parent=self) as contact_service:
            contact_service.add_contact(
                name=self.query_one("#name", Input).value,
                phone_number=self.query_one("#phone-number", Input).value,
            )

    @on(Button.Pressed, "#read-button")
    async def read_contact(self, event: Button.Pressed) -> None:
        phone_number_input = self.query_one("#phone-number", Input)
        name = self.query_one("#name", Input).value

        with ContactService(parent=self) as contact_service:
            contacts = contact_service._read_contacts()
            phone_number_input.value = contact_service.display_contact(name) or phone_number_input.value

    @on(Button.Pressed, "#update-button")
    async def update_contact(self, event: Button.Pressed) -> None:
        with ContactService(parent=self) as contact_service:
            contact_service.update_contact(
                name=self.query_one("#name", Input).value,
                new_phone_number=self.query_one("#phone-number", Input).value,
            )

    @on(Button.Pressed, "#delete-button")
    async def delete_contact(self, event: Button.Pressed) -> None:
        with ContactService(parent=self) as contact_service:
            contact_service.delete_contact(
                name=self.query_one("#name", Input).value,
            )

    @on(Button.Pressed, "#clear-button")
    async def clear(self, event: Button.Pressed) -> None:
        self.query_one("#name", Input).value = ""
        self.query_one("#phone-number", Input).value = ""