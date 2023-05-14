"""Command line interface"""
from __future__ import annotations

import click


@click.command()
@click.version_option()
def main() -> None:
    """test-connections"""


if __name__ == "__main__":
    main(prog_name="test-connections")  # pragma: no cover
