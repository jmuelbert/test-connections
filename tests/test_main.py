from __future__ import annotations

from unittest import TestCase

import pytest

from click.testing import CliRunner
from test_connections.cli.app import main


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
