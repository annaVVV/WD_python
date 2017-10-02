from lib.element import BasePageElement
from lib.locators import LoginPageLocators
from lib.locators import MainViewPageLocators
from lib.utils import SmartSearch
from lib.utils import Config
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.smart_driver = SmartSearch(self.driver)
        self.config = Config()
        self.base_url = self.config.domain
        self.user = self.config.user
        self.password = self.config.password


    def wait_for_element_displayed(self, element, timeout=60, msg="[error] element is not found" ):
      for i in range(timeout):
        try:
          if element.is_displayed(): break
        except:
          pass
        time.sleep(1)
      else:
        #self.fail(msg)
        print msg


class LoginPage(BasePage):

    search_text_element = SearchTextElement()
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.login_url = self.base_url

    def is_title_matches(self):
        return "OrangeHRM" in self.driver.title

    def is_user_admin(self):
        element = self.driver.find_element(*LoginPageLocators.USER)
        return ("Welcome Admin" in element.text)

    def is_login_button_displayed(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        return element.is_displayed()

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()

    def logout(self):
        element = self.driver.find_element(*LoginPageLocators.USER)
        element.click()
        time.sleep(3)
        element = self.driver.find_element(*LoginPageLocators.LOGOUT_BUTTON)
        element.click()

    def put_text_to_username_field(self, text):
        element = self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)
        element.send_keys(text)

    def put_text_to_password_field(self, text):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.send_keys(text)

    def login(self):
        self.put_text_to_username_field(self.user)
        self.put_text_to_password_field(self.password)
        self.click_login_button()


"""
class SearchResultsPage(BasePage):
    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
"""
