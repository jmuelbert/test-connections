from __future__ import annotations

import csv
import time

from time import ctime

import requests


def test_urls(url_file, pdf_output):
    # Create a list to store the URLs
    urls = []


    # Open the URL file and read the URLs
    with open(url_file) as f:
        reader = csv.reader(f)
        for row in reader:
            # Assume the URL is in the first column of the CSV file
            url = row[0]
            # Append the URL to the list
            urls.append(url)

    # Loop through each URL
    for url in urls:
        # Try to get the response from the URL
        try:
            response = requests.get(url)
            # If successful, write the status code and the content length to the PDF file
            pdf_output.write(5, f"URL: {url}\n")
            pdf_output.write(5, f"Status: {response.status_code}\n")
            pdf_output.write(5, f"Content length: {len(response.content)}\n")
            pdf_output.write(5, "\n")
        # If not successful, catch the error and write the message to the PDF file
        except Exception as e:
            pdf_output.write(5, f"URL: {url}\n")
            pdf_output.write(5, f"Error: {e}\n")
            pdf_output.write(5, "\n")
