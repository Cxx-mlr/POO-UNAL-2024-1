from textual.widget import Widget
from textual.widgets import Input, Label
from textual.app import ComposeResult

class InputWithLabel(Widget):
    DEFAULT_CSS = """
    InputWithLabel {
        layout: horizontal;
        height: auto;
    }

    InputWithLabel Label {
        padding: 1;
        width: auto;
        text-align: right;
    }

    InputWithLabel Input {
        width: 1fr;
    }
    """

    def __init__(self, input_label: str = "", label_width: int = -1, *args, **kwargs) -> "InputWithLabel":
        super().__init__()
        self.input_label = input_label
        self._args = args
        self._kwargs = kwargs

        self.label_width = label_width

    def compose(self) -> ComposeResult:
        yield Label(self.input_label)
        yield Input(*self._args, **self._kwargs)

    def on_mount(self):
        label = self.query_one(Label)

        if self.label_width != -1:
            label.styles.width = self.label_width