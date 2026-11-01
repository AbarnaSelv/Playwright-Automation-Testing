import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_home_page import HomePage


def test_example(page: Page) -> None: 
    #Page = blueprint 
    #page = the actual thing built from that blueprint(object)
    page.route(
    "**/core/i18n/messages*",
    lambda route: route.continue_(
        url=route.request.url + (
            "&locale=en_US"
            if "?" in route.request.url
            else "?locale=en_US"
        )
    )
)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    login_page.login("Admin","admin123")
    page.wait_for_url("**/dashboard/index")
    

    
    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.click_dashboard()
    
     