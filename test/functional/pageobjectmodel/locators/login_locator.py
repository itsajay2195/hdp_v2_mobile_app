from selenium.webdriver.common.by import By

"""
This class contains all common ID's of login page, with these id's we are executing tests 

"""


class LoginLocators:
    """ It contains all locators related to login page"""
    # # ACCOUNT_URL=(By.XPATH,'//android.widget.EditText[@text='ajaykumar.supporthive.com']')
    # ACCOUNT_URL1 = (By.XPATH, '//android.widget.EditText[@text='+ACCOUNT_URL+']')
    EMAIL_ID = (By.ID, 'email')
    PASSWORD_ID = (By.ID, 'password')
    SIGN_IN_ID = (By.ID, 'email_sign_in_button')
    LOGIN_RESULT = (By.ID, 'resultView')
