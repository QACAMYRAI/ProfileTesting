from playwright.sync_api import Page, TimeoutError
import math

class BasePage:
    url = 'some url'
    link = "some links"

    def __init__(self, page:Page, link):
        self.page = page
        self.link = link


    def open(self):
        self.page.goto(self.url)

