# Copyright (C) 2023-2024 Jürgen Mülbert.
# SPDX-FileCopyrightText: 2023-2024 Jürgen Mülbert <juergen.muelbert@outlook.de>.
# SPDX-License-Identifier: EUPL-1.2


"""Connect to NTP servers and get the time.

    this function connects to a list of NTP servers and gets the time.
"""

from __future__ import annotations

import csv
import locale
import os
import time
from time import ctime
from typing import TYPE_CHECKING, Any, TypeAlias

import ntplib

if TYPE_CHECKING:
  import fpdf

  BasePathLike = os.PathLike[Any]
else:
  BasePathLike = os.PathLike

FileName: TypeAlias = str | bytes | BasePathLike


def test_ntp(ntp_file: FileName, pdf_output: fpdf) -> None:
  """Tests NTP time synchronization.

  Iterates through a list of NTP servers from a CSV file, attempts to connect
  to each one and get the time, and writes the results to a PDF file.

  Compares the NTP time to the system time and writes the difference.

  Args:
  ----
      ntp_file: Path to CSV file containing NTP servers.
      pdf_output: PDF file to write output to.

  """
  # Create a list to store the NTP servers
  ntps = []

  # Open the NTP file and read the NTP servers
  with open(ntp_file, encoding=locale.getpreferredencoding(False)) as f:
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
      response = c.request(ntp, timeout=10)
      # Write the NTP server, time and system time to the PDF file
      pdf_output.write(5, f'NTP server: {ntp}\n')
      pdf_output.write(5, f'NTP time: {ctime(response.tx_time)}\n')
      pdf_output.write(5, f'System time: {ctime()}\n')
      # Compare the NTP time and system time and write the difference to PDF file
      diff = abs(response.tx_time - time.time())
      pdf_output.write(5, f'Difference: {diff} seconds\n')
      pdf_output.write(5, '\n')
    except response.exceptions.RequestException as e:
      # Write the error message to PDF file
      pdf_output.write(5, f'NTP error: {e}\n')
      pdf_output.write(5, '\n')
