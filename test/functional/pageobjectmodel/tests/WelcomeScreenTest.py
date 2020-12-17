import unittest

from nose.case import Test

from test.functional.pageobjectmodel.specification.BaseSpecification import BaseSpecification
import random
import pytest

'''
This class will contain all common tests for the Welcome screenWhich includes:
1. Validation for account URL
2. Long click event
This class will give us better idea about page object model usage 
'''
EMAIL_ID = 'admin@gmail.com'
PASSWORD = 'admin@123'
ACCOUNT_URL = 'tempajay6.supporthive.com'
INVALID_ACCOUNT_URL = "dummy.ok.com"


# http://selenium-python.readthedocs.io/page-objects.html
# http://selenium-python.readthedocs.io/locating-elements.html
class WelcomeScreenTest(BaseSpecification):


    @pytest.mark.run(order=2)
    def test_with_valid_account_url(self):
        self.app.welcome.set_account_url(ACCOUNT_URL)
        assert self.app.welcome.is_valid_account_url()

    @pytest.mark.run(order=1)
    def test_with_invalid_account_url(self):
        self.app.welcome.set_account_url(INVALID_ACCOUNT_URL)
        assert self.app.welcome.is_invalid_account_url()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
