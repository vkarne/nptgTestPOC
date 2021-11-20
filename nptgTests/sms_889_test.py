from nptgPageObjects.sms_888_po import SMS888PO
from nptgPageObjects.sms_889_po import SMS889PO
from nptgUtilities.status_of_test import StatusOfTest
import pytest
import unittest


@pytest.mark.usefixtures("setup", "one_time_setup")
class Sms889Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.sms888 = SMS888PO(self.driver)
        self.sms889 = SMS889PO(self.driver)
        self.st = StatusOfTest(self.driver)

    @pytest.mark.run(order=1)
    def test_verify_new_account_opened(self):
        self.sms888.click_on_account_link()
        self.sms888.verify_show_chart_button()
        self.sms889.click_on_new_button()
        result = self.ac.verify_summary_tab_visible()
        self.st.mark_final('test_verify_new_account_opened', result, 'new account opened failed')

    @pytest.mark.run(order=2)
    def test_verify_owner(self):
        result = self.sms889.verify_owner()
        self.st.mark_final('test_verify_owner', result, ' Owner value verification failed')

    @pytest.mark.run(order=3)
    def test_verify_owner_text(self):
        result = self.sms889.verify_owner_text()
        self.st.mark_final('test_verify_owner_text', result, ' Owner field value verification failed')

    @pytest.mark.run(order=4)
    def test_open_home_page(self):
        self.sms888.click_on_home_link()
        result = self.sms888.verify_default_page()
        self.st.mark_final('test_open_home_page', result, ' Home page opening verification done!')
