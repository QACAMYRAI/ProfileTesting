from .base_page import BasePage
from playwright.sync_api import expect
from .locators import ProfilePageLocators
import random


class ProfilePage(BasePage):
    url = ProfilePageLocators.Profile_Page_URL

    def random_budget(self):
        all_budget = [ProfilePageLocators.B2m, ProfilePageLocators.B23, ProfilePageLocators.B3m, ProfilePageLocators.B5m, ProfilePageLocators.B10m, ProfilePageLocators.B20m]
        random_budget = random.choice(all_budget)
        return random_budget

    def random_project(self):
        all_project = [ProfilePageLocators.Type_Complex, ProfilePageLocators.Type_Site, ProfilePageLocators.Type_Service, ProfilePageLocators.Type_Design, ProfilePageLocators.Type_Audit, ProfilePageLocators.Type_Branding]
        random_project = random.choice(all_project)
        return random_project

    def random_info(self):
        all_info = [ProfilePageLocators.Rating, ProfilePageLocators.Copi, ProfilePageLocators.Soc, ProfilePageLocators.Recommendation, ProfilePageLocators.Znal]
        random_info = random.choice(all_info)
        return random_info

    def all_data_valid(self):
        self.page.get_by_placeholder(ProfilePageLocators.Profile_PAGE_NAME).fill(ProfilePageLocators.valid_name)
        self.page.get_by_placeholder(ProfilePageLocators.Profile_Page_EMAIL).fill(ProfilePageLocators.valid_email)
        self.page.get_by_placeholder(ProfilePageLocators.Profile_Page_Number).fill(ProfilePageLocators.valid_number)
        self.page.get_by_placeholder(ProfilePageLocators.Profile_Page_Company).fill(ProfilePageLocators.valid_company)

        self.page.get_by_placeholder(ProfilePageLocators.Profile_Page_About_Project).fill(ProfilePageLocators.valid_about_project)

        #self.page.set_input_files("input[type='file']", ProfilePageLocators.file_path) Local file if you need it test change path in locators
        self.page.locator(ProfilePageLocators.Type_Complex).click()

        self.page.locator(self.random_project()).click()
        self.page.locator(self.random_budget()).click()
        self.page.locator(self.random_info()).click()

        self.page.locator(ProfilePageLocators.Profile_Accept).click()
        expect(self.page.get_by_text(ProfilePageLocators.Profile_Sending)).to_be_visible(), "Profile was send"
