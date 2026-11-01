import re
from playwright.sync_api import Page, expect
import pytest

def load_excel_data() -> list:
    from openpyxl import load_workbook

    data = []
    workbook = load_workbook("./test_data/Data.xlsx")
    sheet = workbook.active

    if sheet is not None:
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)

    workbook.close()
    return data
def get_json_data() -> list:
    import json
    with open("./test_data/data.json","r") as file:
        data = json.load(file)
    return data


@pytest.mark.parametrize(
    "username,password",
    load_excel_data()+ get_json_data() + [
        ("Admin", "admin123"),
    ],
)
def test_example(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").press("CapsLock")
    page.get_by_role("textbox", name="Username").fill("A")
    page.get_by_role("textbox", name="Username").press("CapsLock")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
