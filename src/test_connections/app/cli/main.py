# Import the required libraries
from __future__ import annotations

import configparser
from logging import getLogger
from logging.config import fileConfig as logConfig

import click
from fpdf import FPDF
from test_connections.core.check_ntp import test_ntp
from test_connections.core.check_urls import test_urls

logConfig("./logging.conf", disable_existing_loggers=False)
logger = getLogger(__name__)


def create_pdf() -> FPDF:
    """Creates a new PDF object.

    Creates and configures a new FPDF object, adds a blank page,
    sets the font, and returns the PDF object.

    Returns
    -------
        FPDF: The initialized PDF object.

    """
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    return pdf


@click.command()
@click.version_option()
@click.option(
    "-u",
    "--urldata",
    default="url.csv",
    help="the file contents the URLs to be tested",
)
@click.option(
    "-n",
    "--ntpdata",
    default="ntp.csv",
    help="the file contents the NTP servers to be tested",
)
@click.option(
    "-o",
    "--outputfile",
    default="output.pdf",
    help="the name of the output file",
)
def main(ntpdata: str, urldata: str, outputpath: str) -> int:
    r"""cli, generate separate files from datafile.

    Args:
    ----
        ntpdata: the file contents the URLs to be tested
        urldata: the file contents the NTP servers to be tested
        outputfile: the name of the output file

    Returns:
    -------
        Status as int (0 is good)

    """
    config = configparser.ConfigParser()

    config["Path"] = {
        "url_file_name": "url.csv",
        "ntp_file_name": "ntp.csv",
        "pdf_file_name": "result.pdf",
    }

    with open("test-connections.ini", "w", encoding="utf-8") as configfile:
        config.write(configfile)

    url_file = config.get("Path", "url_file_name", fallback="url.csv")
    ntp_file = config.get("Path", "ntp_file_name", fallback="ntp.csv")
    pdf_file = config.get("Path", "pdf_file_name", fallback="output.csv")

    pdf = create_pdf()

    # Make the tests
    test_urls(url_file, pdf)
    test_ntp(ntp_file, pdf)

    # Save PDF file
    pdf.output(pdf_file)

    return 0


if __name__ == "__main__":
    main()
