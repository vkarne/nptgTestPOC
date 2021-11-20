from nptgPageObjects.sms_888_po import SMS888PO
from nptgUtilities.status_of_test import StatusOfTest
import pytest
import unittest


@pytest.mark.usefixtures("setup", "one_time_setup")
class SMS888TEST(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.sms888 = SMS888PO(self.driver)
        self.st = StatusOfTest(self.driver)

    @pytest.mark.run(order=1)
    def test_open_account(self):
        self.sms888.click_on_account_link()
        self.sms888.verify_show_chart_button()

    @pytest.mark.run(order=2)
    def test_list_active_accounts(self):
        self.sms888.select_active_account()
        result = self.sms888.verify_active_accounts_listed()
        self.st.mark_final('test_list_active_accounts', result, 'Active accounts listed failed')

    @pytest.mark.run(order=3)
    def test_open_account_details(self):
        self.sms888.open_active_account_details()
        result = self.sms888.verify_account_details_opened()
        self.st.mark_final('test_open_account_details', result, 'Selected active account details opened failed')

    @pytest.mark.run(order=4)
    def test_acc_info_fields(self):
        result = self.sms888.verify_account_info_fields()
        self.st.mark_final('test_acc_info_details', result, 'Selected account information fields missing')

    @pytest.mark.run(order=5)
    def test_address_info_fields(self):
        result = self.sms888.verify_address_info_fields()
        self.st.mark_final('test_acc_info_details', result, 'Selected address information fields missing')

    @pytest.mark.run(order=6)
    def test_billing_info_fields(self):
        result = self.sms888.verify_billing_info_fields()
        self.st.mark_final('test_billing_info_fields', result, 'Selected billing information fields missing')

    @pytest.mark.run(order=7)
    def test_contact_info_fields(self):
        result = self.sms888.verify_contact_info_fields()
        self.st.mark_final('test_contact_info_fields', result, 'Selected contact information fields missing')

    @pytest.mark.run(order=8)
    def test_territory_info_fields(self):
        result = self.sms888.verify_territory_info_fields()
        self.st.mark_final('test_territory_info_fields', result, 'Selected territory information fields missing')

    @pytest.mark.run(order=9)
    def test_goto_home_page(self):
        self.sms888.click_on_home_link()
        result = self.sms888.verify_default_page()
        self.st.mark_final('test_goto_home_page', result, ' Home page opening verification failed!')










