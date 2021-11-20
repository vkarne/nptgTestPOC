from nptgBase.base_page import BasePage
import nptgUtilities.custom_logger as cl
import logging


class SMS889PO(BasePage):
    log = cl.customer_logging(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    # ----------

    _new_button_xpath = '//button[@aria-label="New"]'
    _show_chart_btn_id = 'ShowChartPane-button'
    _new_account_header_xpath = '//h1[@title="New Account"]'
    _summary_tab_css = 'li[aria-label="Summary"]'
    _owner_xpath = '//a[normalize-space()="Venkanna Karne"]'
    _owner_textfield_css = '[data-id="ownerid.fieldControl-LookupResultsDropdown_ownerid_selected_tag_text"]'
    _account_address_id = 'tab1_4'
    _contacts_xpath = '//li[@title="Contacts"]'
    _manage_accounts_xpath = '//li[@title="Managed Accounts"]'
    _child_accounts_xpath = '//li[@title="Child Accounts"]'
    _attribute = '"aria-label"'
    _title_attribute = '"title"'

    def click_on_new_button(self):
        self.element_click(self._new_button_xpath, locator_type="XPATH")

    def verify_summary_tab_visible(self):
        summary_tab_element = self.wait_for_element_visible(self._summary_tab_css, locator_type="CSS")
        is_visible = self.is_element_displayed(element=summary_tab_element)
        if is_visible:
            self.log.info('Summary tab is Displayed as expected - TEST PASSED')
            return True
        else:
            self.log.error('Summary tab is NOT Displayed - TEST FAILED')
            return False

    def verify_owner(self):
        owner_element = self.wait_for_element_visible(self._owner_xpath, locator_type="XPATH")
        owner = self.get_text(element=owner_element)
        print(owner)
        if owner:
            self.log.info("Owner is present - TEST PASSED" + owner)
            return True
        else:
            self.log.error("Owner value is not populated - TEST FAILED")
            return False

    def verify_owner_text(self):
        self.web_scroll(direction="down")
        owner_field_element = self.wait_for_element_visible(self._owner_textfield_css, locator_type="CSS")
        owner_text = self.get_text(element=owner_field_element)
        if owner_text:
            self.log.info("Owner field value is present - TEST PASSED " + owner_text)
            return True
        else:
            self.log.error("Owner field value capture failed - TEST FAILED")
            return False
