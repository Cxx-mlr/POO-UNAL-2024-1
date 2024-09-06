from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

class ContactManagerSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="contact_manager_")

    contacts_directory: Path = Path(__file__).parent.resolve()
    contacts_file_name: str = "contacts.txt"
    app_name: str = "Contact Manager"

    @property
    def contacts_file_path(self) -> Path:
        return self.contacts_directory / self.contacts_file_name

settings = ContactManagerSettings()