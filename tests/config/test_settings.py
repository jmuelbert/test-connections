from __future__ import annotations

import os
from unittest import TestCase, mock

from test_connections.config.settings import Settings

"""Tests for reading configuration settings from a file.

This suite of tests verifies that the Settings class can:

- Read values from a settings file and make them available
- Return a default when a setting is not found
- Parse settings as int, float, etc. based on type
- Read environment-specific overrides
"""


class SettingsTest(TestCase):
    """Tests for reading configuration settings from a file.

    This test suite verifies that the Settings class can:

    - Read values from a settings file and make them available
    - Return a default when a setting is not found
    - Parse settings as int, float, etc. based on type
    - Read environment-specific overrides

    The tests are organized into unit tests for each of these behaviors.
    """

    """Tests for reading configuration settings from a file.

    This test suite verifies that the Settings class can:

    - Read values from a settings file and make them available
    - Return a default when a setting is not found
    - Parse settings as int, float, etc. based on type
    - Read environment-specific overrides

    The tests are organized into unit tests for each of these behaviors.
    """
    """Tests for reading configuration settings from a file.

    This test suite verifies that the Settings class can:

    - Read values from a settings file and make them available
    - Return a default when a setting is not found
    - Parse settings as int, float, etc. based on type
    - Read environment-specific overrides

    The tests are organized into unit tests for each of these behaviors.
    Tests for reading configuration settings from a file.

    This test suite verifies that the Settings class can:

    - Read values from a settings file and make them available
    - Return a default when a setting is not found
    - Parse settings as int, float, etc. based on type
    - Read environment-specific overrides

    The tests are organized into unit tests for each of these behaviors.
    """
    """Tests for reading configuration settings from a file.

    This test suite verifies that the Settings class can:

    - Read values from a settings file and make them available
    - Return a default when a setting is not found
    - Parse settings as int, float, etc. based on type
    - Read environment-specific overrides

    The tests are organized into unit tests for each of these behaviors.
    """

    """Sets up the Settings instance to test.

        Creates a Settings instance initialized with the
        settings_to_test.conf file for testing purposes.
        """

    def setUp(self) -> None:
        self.settings = Settings(file="./tests/config/settings_to_test.conf")

    def test_get_setting_value_with_success(self):
        """Tests that the get() method returns the correct
        setting value for a given setting key. Verifies
        the get() method returns the expected value for
        a valid setting key.
        """
        self.assertEqual(self.settings.get("app_name"), "app-name")

    """Tests that the get() method returns the default value
    when the setting key is not found in the settings file.
    Verifies get() returns the expected default value when
    given an invalid setting name.
    """

    def test_get_default_value_when_setting_not_found_with_success(self):
        self.assertEqual(self.settings.get("not_found_var", "default_value"), "default_value")

    def test_get_setting_int_value_with_success(self):
        """Tests that the get() method parses and returns
        integer values correctly. Verifies that get() will
        cast the setting value to an integer if the setting
        type is int.
        """
        self.assertEqual(int(self.settings.get("sample_of_int_var")), 10)

    def test_get_setting_float_value_with_success(self):
        """Tests that the get() method parses and returns
        float values correctly. Verifies that get() will
        cast the setting value to a float if the setting
        type is float."""
        self.assertEqual(float(self.settings.get("sample_of_float_var")), 10.10)

    @mock.patch.dict(os.environ, {"ENV": "prod"}, clear=True)
    def test_get_setting_value_from_production_env_with_success(self):
        """Creates a Settings instance initialized for the production
        environment, loading config from the given file path.
        """
        prod_settings = Settings(file="./tests/config/settings_to_test.conf")
        self.assertEqual(prod_settings.get("app_var"), "prod-app-var")

    """Creates a Settings instance initialized for the QA
    environment, loading config from the given file path."""

    @mock.patch.dict(os.environ, {"ENV": "qa"}, clear=True)
    def test_get_setting_value_from_qa_env_with_success(self):
        qa_settings = Settings(file="./tests/config/settings_to_test.conf")
        self.assertEqual(qa_settings.get("app_var"), "qa-app-var")

    """Creates a Settings instance initialized for the test
       environment, loading config from the given file path."""

    @mock.patch.dict(os.environ, {"ENV": "test"}, clear=True)
    def test_get_setting_value_from_test_env_with_success(self):
        test_settings = Settings(file="./tests/config/settings_to_test.conf")
        self.assertEqual(test_settings.get("app_var"), "test-app-var")

    """Creates a Settings instance initialized for the dev
    environment, loading config from the given file path."""

    @mock.patch.dict(os.environ, {"ENV": "dev"}, clear=True)
    def test_get_setting_value_from_dev_env_with_success(self):
        dev_settings = Settings(file="./tests/config/settings_to_test.conf")
        self.assertEqual(dev_settings.get("app_var"), "dev-app-var")
