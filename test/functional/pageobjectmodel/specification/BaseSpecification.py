import unittest

from appium import webdriver

import test.functional.pageobjectmodel.util.desired_capabilities as desired_capabilities
from test.functional.pageobjectmodel.util.application import Application

"""
This class is responsible for creating driver connection with appium server
"""


class BaseSpecification(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('app-release.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.app = Application(self.driver)

    def tearDown(self):
        self.driver.quit()
