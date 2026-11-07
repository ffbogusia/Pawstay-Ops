# PawStay Ops

PawStay Ops is a small command-line application for monitoring rooms in a fictional dog hotel.

I built this project to consolidate and practice my Python skills, drawing on my background in IT. Instead of working on isolated exercises, I wanted one practical application that brings many topics together: JSON files, validation, classes, logging, command-line arguments, environment variables, API requests, retries, subprocesses, automated tests, and more.

It is a learning project, but I approached it like a real tool: separate modules, input validation, configuration through environment variables, logging, and tests.

## What the application does

Step by step, the application:

- loads room data from a JSON file;
- validates the input data;
- converts valid data into `Room` objects;
- finds rooms whose cameras need attention;
- filters rooms by camera status;
- checks an external HTTP service;
- retries failed API requests;
- performs a basic Python system check;
- generates a text report;
- writes operational information to a log file.

## Technologies

- Python 3.13
- Requests
- pytest
- argparse
- pathlib
- logging
- subprocess

## Project structure

```text
pawstay_ops/
├── data/
│   └── rooms.json
├── tests/
│   ├── test_room_service.py
│   └── test_validation.py
├── api_client.py
├── config_io.py
├── main.py
├── models.py
├── report_builder.py
├── room_service.py
├── system_check.py
├── validation.py
├── requirements.txt
└── README.md
```

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Running the application

Run the application with its default settings:

```powershell
python main.py
```

Filter rooms by camera status:

```powershell
python main.py --status failed
```

Available statuses are:

```text
all
healthy
failed
unknown
```

Choose a custom report filename:

```powershell
python main.py --report-name night_report.txt
```

Arguments can also be combined:

```powershell
python main.py --status failed --report-name failed_rooms.txt
```

Display command-line help:

```powershell
python main.py --help
```

## Environment variables

The application supports the following environment variables:

| Variable | Purpose | Default |
|---|---|---|
| `PAWSTAY_HOTEL` | Hotel name displayed in the report | `PawStay` |
| `PAWSTAY_ENVIRONMENT` | Application environment | `development` |
| `PAWSTAY_LOG_LEVEL` | Logging level | `INFO` |
| `PAWSTAY_MAX_ROOMS` | Maximum expected room capacity | `10` |
| `PAWSTAY_API_URL` | URL used for the external service check | HTTP 200 test endpoint |
| `PAWSTAY_API_TIMEOUT` | API request timeout in seconds | `5` |

Example for PowerShell:

```powershell
$env:PAWSTAY_HOTEL = "PawStay Wroclaw"
$env:PAWSTAY_LOG_LEVEL = "DEBUG"
python main.py
```

## Tests

Run all tests:

```powershell
python -m pytest -v
```

The current test suite covers room filtering and room-data validation, and I plan to extend it as the project grows.

## What's next

I may keep developing this project as I explore new areas. Ideas I'm considering include broader test coverage, more robust error handling, and additional report features.

Feedback and suggestions are always welcome! 🙂