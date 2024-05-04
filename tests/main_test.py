# SPDX-FileCopyrightText: © 2023-2024 Jürgen Mülbert
#
# SPDX-License-Identifier: EUPL-1.2

from __future__ import annotations

from click.testing import CliRunner

from checkconnect.cli import checkconnect


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    runner = CliRunner()
    result = runner.invoke(checkconnect, ["--version"])
    assert result.exit_code == 0
