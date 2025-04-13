# Store Monitoring Report Generator

This project provides a REST API to trigger and generate reports based on store status data. The generated reports are saved in CSV format and can be downloaded via the API. Reports are generated asynchronously, and their status can be queried.

## Features

- **Trigger Reports**: Trigger the generation of a report with a `POST` request.
- **Check Report Status**: Check the current status of a report with a `GET` request.
- **Download Reports**: Download the generated report once complete.

## Project Structure

- **`app.py`**: Main Flask application that handles the API endpoints.
- **`generate_report.py`**: Logic for generating the reports.
- **`shared_state.py`**: Shared state for tracking report generation status.
- **`scheduler.py`**: Auto triggers the report generation every hour.
- **`reports/`**: Directory where the generated reports are stored.

## Installation

### Requirements

- Python 3.x
- Flask
- pandas
- schedule
- requests
- pytz

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/store-monitoring-report-generator.git
    cd store-monitoring-report-generator
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `reports/` directory to store the generated reports:

    ```bash
    mkdir reports
    ```

### Run the Flask Application

Run the Flask app with the following command:

```bash
python app.py
