from __future__ import annotations

from configparser import ConfigParser
from os import getenv
from typing import Any

"""Settings class to handle configuration."""


class Settings:
    __slots__ = ["config_parser", "env"]
    config_parser: ConfigParser
    env: str

    def __init__(self, file: str = "settings.conf") -> None:
        """Initializes the Settings class.

        Reads in the configuration from the provided file path.
        Sets the ENV environment variable to 'dev' if not already set.
        """
        self.config_parser = ConfigParser()
        self.config_parser.read(file)
        self.env = getenv("ENV", "dev")

    def get(self, name: str, default_value: Any = None) -> Any:
        """Gets the value for the given setting name from the environment
        configuration.

        First checks the configuration for the current ENV environment.
        If not found, checks the 'default' environment configuration.
        If still not found, returns the provided default value.

        Args:
        ----
            name: The name of the setting to get.
            default_value: The value to return if no value found for the setting.

        Returns:
        -------
            The value for the setting, or the default value if not found.

        """
        return self._get_from_section(self.env, name) or self._get_from_section("default", name) or default_value

    def _get_from_section(self, section: str, var: str) -> Any:
        """Gets the value for the given setting name from the given config
        section.

        Checks if the given section exists in the config parser and if the
        given setting name exists in that section. If found, returns the
        setting value. Otherwise returns None.

        Args:
        ----
            section: The section in the config to check.
            var: The name of the setting to get.

        Returns:
        -------
            The setting value if found, else None.

        """
        if section in self.config_parser and var in self.config_parser[section]:
            return self.config_parser[section][var]
        return None


"""Initializes a Settings instance.

Creates a new instance of the Settings class, which will load and parse
the configuration from the default settings file.
"""
settings = Settings()
