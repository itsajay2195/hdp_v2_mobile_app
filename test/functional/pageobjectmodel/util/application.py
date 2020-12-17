from test.functional.pageobjectmodel.pageobject.login import Login
from test.functional.pageobjectmodel.pageobject.welcome import Welcome
"""
This class will be responsible for creating a instance of page object

Note: In future this class will hold all common properties related application
"""


class Application:
    def __init__(self, driver):
        self.welcome = Welcome(driver)

        self.login = Login(driver)


