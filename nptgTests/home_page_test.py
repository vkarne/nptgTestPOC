from nptgPageObjects.home_page import OpenAccountPage
from nptgUtilities.status_of_test import StatusOfTest
import pytest
import unittest
import time


@pytest.mark.usefixtures("setup", "one_time_setup")
class OpenAccountTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ac = OpenAccountPage(self.driver)
        self.st = StatusOfTest(self.driver)

    def test_open_account_page(self):
        self.ac.click_on_menu_icon()
        time.sleep(1)
        self.ac.click_on_menu_icon()
        time.sleep(1)
        self.ac.click_on_account_link()
        self.ac.verify_show_chart_button()
        self.ac.click_on_home_link()
        result = self.ac.verify_default_page()
        self.st.mark_final('test_open_account_page', result, ' Home page opening verification done!')
