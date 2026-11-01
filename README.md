# Playwright Automation Testing with Python

A hands-on automation testing project developed while learning **Playwright with Python and pytest**.

## Technologies Used

- Python
- Playwright
- pytest
- pytest-playwright
- Pytest HTML Reports
- OpenPyXL
- JSON

## Project Highlights

- Browser automation using Playwright.
- Page Object Model (POM) implementation.
- Pytest fixtures and test execution.
- Data-driven testing using Excel and JSON files.
- Test parameterization using `pytest.mark.parametrize`.
- API testing using Playwright's request capabilities.
- HTML test report generation.

## Project Structure

```text
Playwright_demo/
│
├── pages/
├── tests/
├── test_data/
│   ├── Data.xlsx
│   └── data.json
├── utils/
├── reports/
├── pytest.ini
└── README.md
```

## Setup and Execution

1. Clone the repository:

```bash
git clone https://github.com/AbarnaSelv/Playwright-Automation-Testing
```

2. Navigate to the project directory:

```bash
cd Playwright_demo
```

3. Install dependencies:

```bash
pip install pytest playwright pytest-playwright pytest-html openpyxl
```

4. Install Playwright browsers:

```bash
playwright install
```

5. Run the tests:

```bash
pytest -v
```

## Learning Outcome

This project helped me gain practical experience with Python-based browser automation, pytest, Page Object Model, data-driven testing, and API testing.

**Note:** This is a learning project, and I plan to continue expanding it by exploring more Playwright features and automation testing practices.