from __future__ import annotations

from textual.app import ComposeResult
from textual.widgets import Input, Label, Static
from textual.widget import Widget
from textual.containers import Horizontal, Vertical
from textual.message import Message

class InputWithLabel(Widget):
    DEFAULT_CSS = """
    InputWithLabel {
        height: auto;
    }

    InputWithLabel #input-label {
        padding-top: 1;
        width: auto;
        text-align: right;
    }

    InputWithLabel Input {
        width: 1fr;
        height: 3;
    }

    InputWithLabel #failure-description {
        display: none;
        padding-left: 2;
    }

    InputWithLabel #horizontal-container {
        height: auto;
    }

    InputWithLabel #vertical-container {
        height: auto;
    }
    """

    class Changed(Message):
        def __init__(self, input: Input, is_valid: bool) -> "InputWithLabel.Changed":
            self.input = input
            self.is_valid = is_valid
            super().__init__()

    def __init__(self, input_label: str = "", label_width: int = -1, *args, **kwargs) -> "InputWithLabel":
        super().__init__()
        self.input_label = input_label
        self._args = args
        self._kwargs = kwargs

        self.label_width = label_width
        self.is_valid = kwargs.get("valid_empty", False)

    def compose(self) -> ComposeResult:
        with Horizontal(id="horizontal-container"):
            yield Label(self.input_label, id="input-label")
            with Vertical(id="vertical-container"):
                yield Input(*self._args, **self._kwargs)
                yield Static(id="failure-description")

    def on_mount(self):
        label = self.query_one(Label)

        if self.label_width != -1:
            label.styles.width = self.label_width

    def on_input_changed(self, event: Input.Changed):
        static = self.query_one("#failure-description", Static)
        input = self.query_one(Input)

        if not getattr(event.validation_result, "is_valid", True):
            self.is_valid = False
            failure_description = "\n".join(getattr(event.validation_result, "failure_descriptions", [])[:1])
            static.update(f"[red][i]{failure_description}")
            static.styles.display = "block"
        else:
            self.is_valid = True
            static.update("")
            static.styles.display = "none"

        self.post_message(self.Changed(input, self.is_valid))