#
# SPDX-FileCopyrightText: 2024 Jürgen Mülbert <juergen.muelbert@outlook.de>
#
# SPDX-License-Identifier: EUPL-1.2
#
"""Command-line interface."""

from __future__ import annotations

import sys

from test_connections.app.cli import main as cli

if __name__ == "__main__":
    cli(*args)

if getattr(sys, "frozen", False):
    cli(sys.argv[1:])
