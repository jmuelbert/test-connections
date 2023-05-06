"""Command line interface"""
import click

@click.command()
@click.version_option()
def main() -> None:
    """test-connection"""
    
if __name__ == "__main__":
    main(prog_name="test-connection") # pragma: no cover
