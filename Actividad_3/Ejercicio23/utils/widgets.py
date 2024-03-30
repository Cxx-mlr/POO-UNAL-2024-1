from textual.app import ComposeResult
from textual.widgets import Input, Label, Static
from textual.widget import Widget
from textual.containers import Horizontal, Vertical

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

    def __init__(self, input_label: str = "", label_width: int = -1, *args, **kwargs) -> "InputWithLabel":
        super().__init__()
        self.input_label = input_label
        self._args = args
        self._kwargs = kwargs

        self.label_width = label_width

    def compose(self) -> ComposeResult:
        with Horizontal(id="horizontal-container"):
            yield Label(self.input_label, id="input-label")
            with Vertical(id="vertical-container"):
                yield Input(*self._args, **self._kwargs)
                yield Static(id="failure-description")

    def on_mount(self):
        label = self.query_one("#input-label")

        if self.label_width > 0:
            label.styles.width = self.label_width

    def on_input_changed(self, event: Input.Changed):
        static = self.query_one("#failure-description", Static)

        if not getattr(event.validation_result, "is_valid", True):
            failure_description = "\n".join(getattr(event.validation_result, "failure_descriptions", []))
            static.update(f"[red][i]{failure_description}")
            static.styles.display = "block"
        else:
            static.update("")
            static.styles.display = "none"