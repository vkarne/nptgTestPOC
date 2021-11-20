"""
@package base
Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class need to be inherited by all the page classes
This should not be used by creating object instance
Example:
     Class LoginPage(BasePage)
"""
from selenium.common.exceptions import *
from nptgBase.selenium_driver import SeleniumDriver
from traceback import print_stack
from nptgUtilities.utility import Utility


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
               Inits BasePage class

               Returns:
                   None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.utility = Utility()

    def verify_page_title(self, title_to_verify):
        """
            Verifies the page title

            parameters:
                title_to_verify: title on the page that needs to be verified
        """
        try:
            actual_title = self.get_page_title()
            return self.utility.verify_list_contains(actual_title, title_to_verify)
        except NoSuchElementException as err:
            self.log.error(str(err) + "Failed to get page title")
            print_stack()
            return False
















