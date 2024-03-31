from __future__ import annotations

from click.testing import CliRunner
from test_connections.app.cli.main import main


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
