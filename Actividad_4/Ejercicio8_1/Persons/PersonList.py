from __future__ import annotations

from textual.app import ComposeResult
from textual.widgets import ListView, ListItem, Label

from textual.widget import Widget

from .Person import Person

from rich.text import Text
from rich.console import Group

import itertools

class PersonList(Widget):
    DEFAULT_CSS = """
        PersonList {
            border: solid gray;
            background: white;
        }

        .row-even {
            background: #f2f2f2;
        }

        .row-odd {
            background: #ffffff;
        }
    """
    def __init__(self, *args, **kwargs) -> PersonList:
        super().__init__(*args, **kwargs)
        self.__person_list: Person = ListView()
        self.__classes = itertools.cycle(("row-even", "row-odd"))

    def compose(self) -> ComposeResult:
        yield self.__person_list

    async def add_person(self, person: Person) -> None:
        self.__person_list.mount(
            ListItem(
                Label(
                    Group(
                        Text(f"{person.first_name} {person.last_name}\t-\t{person.phone}"),
                        Text(f"{person.address}")
                    ),
                    expand=True,
                ),
                classes=f"{next(self.__classes)}"
            ),
            before=0
        )

        if self.__person_list.index is not None:
            self.__person_list.index += 1

    async def remove_currently_selected_person(self) -> None:
        index = self.__person_list.index = min(self.__person_list.index, len(self.__person_list) - 1)
        await self.__person_list.pop(self.__person_list.index)
        self.__person_list.index = index

    def clear(self) -> None:
        self.__person_list.clear()

    def is_empty(self) -> bool:
        return len(self.__person_list) == 0