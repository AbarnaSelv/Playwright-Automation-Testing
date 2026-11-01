import re
from playwright.sync_api import expect


def test_google_search(page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/ncr")
    
    print("Before cookie check")
    try:
        page.get_by_role(
        "combobox", name="Search"
         ).fill("Playwright Python")

        print("Cookie consent button clicked")
    except Exception as e:
        print("No popup to accept")
        print("Reason:", e)
    
    print("After cookie check")

    

    
    

    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
    