from __future__ import annotations
from .config import settings

class ContactService:
    def __init__(self, parent) -> ContactService:
        self._parent = parent

    def __enter__(self):
        if not settings.contacts_directory.exists():
            settings.contacts_directory.mkdir(parents=True)

        if not settings.contacts_file_path.exists():
            settings.contacts_file_path.touch()

        self._file = open(settings.contacts_file_path, "r+")
        # self._contacts_backup = self._read_contacts()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if exc_type is not None:
        #     self._write_contacts(self._contacts_backup)
        #     print("An error occurred, changes have been discarded.")

        if self._file:
            self._file.close()

    def _read_contacts(self):
        self._file.seek(0)
        contacts = {}
        for line in self._file:
            name, phone_number = line.strip().split(",")
            contacts[name] = phone_number
        return contacts

    def _write_contacts(self, contacts):
        self._file.seek(0)
        self._file.truncate()
        for name, phone_number in contacts.items():
            self._file.write(f"{name},{phone_number}\n")
        self._file.flush()

    def add_contact(self, name: str, phone_number: str):
        contacts = self._read_contacts()
        if name in contacts:
            self._parent.notify(f"Contact with name {name!r} already exists.")
        else:
            contacts[name] = phone_number
            self._write_contacts(contacts)
            self._parent.notify(f"Added contact: {name!r} - {phone_number}")

    def display_contact(self, name: str):
        contacts = self._read_contacts()

        if name in contacts:
            return contacts[name]
        else:
            self._parent.notify(f"No contact found with the name {name!r}.")
            return ""

    def delete_contact(self, name: str):
        contacts = self._read_contacts()
        if name in contacts:
            del contacts[name]
            self._write_contacts(contacts)
            self._parent.notify(f"Deleted contact: {name!r}")
        else:
            self._parent.notify(f"No contact found with the name {name!r}.")

    def update_contact(self, name: str, new_phone_number: str):
        contacts = self._read_contacts()
        if name in contacts:
            contacts[name] = new_phone_number
            self._write_contacts(contacts)
            self._parent.notify(f"Updated contact: {name!r} - {new_phone_number}")
        else:
            self._parent.notify(f"No contact found with the name {name!r}.")