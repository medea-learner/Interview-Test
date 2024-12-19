# README

## Overview
This script uses Selenium to perform a Google search for the query "hello world," using `Chrome Browser` extracts the top 10 search results (title, description, and URL), and saves them to an Excel file named `search_results.xlsx`.

## Prerequisites
Ensure you have the following installed before running the script:

1. **Python**: Version 3.7 or later
2. **Google Chrome**: Version compatible with the installed ChromeDriver
3. **ChromeDriver**: Place the executable relevant to your system (https://googlechromelabs.github.io/chrome-for-testing/#stable) in an accessible path (update the EXECUTABLE_PATH in the script if necessary).

## Installation

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Dependencies
The script requires the following Python packages:

- `selenium`: For interacting with the web browser
- `openpyxl`: For creating and editing Excel files

## Running the Script

1. Again update the `EXECUTABLE_PATH` in the script to point to your ChromeDriver location.
2. Run the script:

   ```bash
   python main.py
   ```

3. The results will be saved in an Excel file named `search_results.xlsx` in the project directory.

## Notes
- Ensure that ChromeDriver matches the version of your installed Google Chrome browser. You can download the correct version from [ChromeDriver](https://sites.google.com/chromium.org/driver/).
- If the structure of Google's search results changes, update the selectors in the script accordingly.

## License
This project is licensed under the MIT License.
