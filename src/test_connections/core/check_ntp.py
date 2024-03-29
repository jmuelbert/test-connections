from __future__ import annotations

import csv
import time
from time import ctime

import ntplib


def test_ntp(ntp_file, pdf_output):
    """Tests NTP time synchronization.

    Iterates through a list of NTP servers from a CSV file, attempts to connect
    to each one and get the time, and writes the results to a PDF file.

    Compares the NTP time to the system time and writes the difference.

    Args:
        ntp_file: Path to CSV file containing NTP servers.
        pdf_output: PDF file to write output to.

    """
    # Create a list to store the NTP servers
    ntps = []

    # Open the NTP file and read the NTP servers
    with open(ntp_file) as f:
        reader = csv.reader(f)
        for row in reader:
            # Assume the NTP server is in the first column of the CSV file
            ntp = row[0]
            # Append the NTP server to the list
            ntps.append(ntp)

    # Loop through each NTP server
    for ntp in ntps:
        # Try to get the time from the NTP server
        try:
            # Use ntplib to get the time from the NTP server
            c = ntplib.NTPClient()
            response = c.request(ntp)
            # Write the NTP server, time and system time to the PDF file
            pdf_output.write(5, f"NTP server: {ntp}\n")
            pdf_output.write(5, f"NTP time: {ctime(response.tx_time)}\n")
            pdf_output.write(5, f"System time: {ctime()}\n")
            # Compare the NTP time and system time and write the difference to PDF file
            diff = abs(response.tx_time - time.time())
            pdf_output.write(5, f"Difference: {diff} seconds\n")
            pdf_output.write(5, "\n")
        except Exception as e:
            # Write the error message to PDF file
            pdf_output.write(5, f"NTP error: {e}\n")
            pdf_output.write(5, "\n")
