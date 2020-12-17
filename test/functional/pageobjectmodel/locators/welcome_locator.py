from selenium.webdriver.common.by import By

"""
This class contains all common ID's of login page, with these id's we are executing tests 

"""


class WelcomeLocators:
    ACCOUNT_URL = (By.CLASS_NAME, 'android.widget.EditText')
    CONTINUE_BUTTON = (By.XPATH, '//android.view.ViewGroup[@clickable="true" and @index="5"]')
    WELCOME_RESULT = (By.CLASS_NAME, 'android.widget.TextView')
    INVALID_URL_DIALOG = (By.ID, 'android:id/message')
