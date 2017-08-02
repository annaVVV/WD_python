import unittest
from selenium import webdriver
from lib import page


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.login_page = page.LoginPage(self.driver)
        self.driver.get(self.login_page.login_url)
        self.driver.maximize_window()

    def test_login_logout(self):
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_matches()
        login_page.login()
        assert login_page.is_title_matches()
        assert login_page.is_user_admin()
        login_page.logout()
        assert login_page.is_title_matches()
        assert login_page.is_login_button_displayed()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
