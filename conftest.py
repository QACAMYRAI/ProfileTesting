import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
                                      )
        page: Page = context.new_page()
        page.add_init_script("""
        navigator.webdriver = false
        Object.defineProperty(navigator, 'webdriver', {
        get: () => false
        })
        """
                             )
        page.set_viewport_size({'height': 1080, 'width': 1920})
        print('Browser is opened')
        yield page
        context.close()
        browser.close()
        print("Browser is closed")