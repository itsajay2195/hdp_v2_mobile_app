from test.functional.pageobjectmodel.locators.welcome_locator import WelcomeLocators
from test.functional.pageobjectmodel.pageobject import *
import time

class Welcome(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_account_url(self, account_url):
        self.__set__(WelcomeLocators.ACCOUNT_URL, account_url)
        time.sleep(5)
        self.click(WelcomeLocators.CONTINUE_BUTTON)
        time.sleep(5)

    def is_valid_account_url(self):
        return self.__get__(WelcomeLocators.WELCOME_RESULT) == 'Log In'

    def is_invalid_account_url(self):
        print("the result is : ", self.__get__(WelcomeLocators.INVALID_URL_DIALOG))
        return self.__get__(WelcomeLocators.INVALID_URL_DIALOG) == 'Invalid Account URL'
