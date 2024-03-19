"""test_connections"""

# ruff: noqa
__version__ = "0.1.0dev"

from typing import Any

# Necessary as mypy would see expr as the module alt.expr although due to how
# the imports are set up it is expr in the alt.expr module
expr: Any

# The content of __all__ is automatically written by
# tools/update_init_file.py. Do not modify directly.
__all__ = []
