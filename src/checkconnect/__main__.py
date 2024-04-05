# Copyright (C) 2023-2024 Jürgen Mülbert.
# SPDX-FileCopyrightText: 2023-2024 Jürgen Mülbert <juergen.muelbert@outlook.de>.
# SPDX-License-Identifier: EUPL-1.2

"""Main entry point for the module.

This calls the main() function from the cli module
if the script is executed directly.

Calls the main function from the module
    app.cli.cli
"""

import sys

if __name__ == '__main__':
  from checkconnect.cli import main

  sys.exit(main())


if getattr(sys, 'frozen', False):
  """Check if the script is frozen (e.g. pyinstaller executable)."""

  sys.exit(main(sys.argv[1:]))
