from .pages.profile_page import ProfilePage

def test_e2e_profile_page_with_valid_data(page):
    Profile_Page = ProfilePage(page,ProfilePage.url)
    Profile_Page.open()
    Profile_Page.all_data_valid()


