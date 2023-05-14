"""Sphinx configuration."""
from __future__ import annotations


project = "test-connections"
author = "Jürgen Mülbert"
copyright = "2023, Jürgen Mülbert"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
