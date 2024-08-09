# SSRF Port Scanner Script

This Python script performs port scanning using POST requests to test different ports on a specific domain. The scan results are saved in a JSON file named `scan_results.json`.
I developed this script while solving the [Editorial machine](https://app.hackthebox.com/machines/Editorial) on Hack The Box.


## Requirements

To run this script, you'll need Python 3 and the `requests` package. Additionally, `requests_toolbelt` is required to handle multipart encodings in requests.

You can install the necessary dependencies with:

```bash
pip3 install requests_toolbelt
```

## Usage

To use this script, follow these steps:

1. Open your terminal or command line.
2. Run the script with the command:

```bash
python3 port_scanner.py
```

3. When prompted, enter the initial port, the end port, and the URL where the POST requests will be sent.

## Features

The script will allow you to:

- Define a domain and a range of ports to scan.
- Make POST requests to each port within the specified range.
- Save the scan results, including the status code, the content length of the response, the response time, and a sample of the response content, in a JSON file.

## Example Output

The scan results will be saved in the file `scan_results.json` with the following format:

```json
[
    {
        "port": 80,
        "status_code": 200,
        "content_length": 1500,
        "response_time": 0.012,
        "sample_of_response": "<html>...</html>"
    },
    {
        "port": 81,
        "error": "Connection timed out"
    }
]
```

This format makes it easy to interpret and analyze the data further.

## Warnings

This script is intended for educational and testing purposes only in controlled environments. Make sure you have permission to scan the ports on the specified domain to avoid legal violations.

## Contributions

Contributions to the script are welcome. If you have suggestions for improvement or corrections, feel free to fork the repository and submit a pull request.
