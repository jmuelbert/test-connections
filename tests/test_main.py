#
# Copyright (C) 2023-2024 Jürgen Mülbert.
# SPDX-FileCopyrightText: 2023-2024 Jürgen Mülbert <juergen.muelbert@outlook.de>.
# SPDX-License-Identifier: EUPL-1.2

from __future__ import annotations

from checkconnect.cli import checkconnect

from click.testing import CliRunner


def test_main_succeeds() -> None:
  """It exits with a status code of zero."""
  runner = CliRunner()
  result = runner.invoke(checkconnect, ['--version'])
  assert result.exit_code == 0
