
from nptgBase.base_page import BasePage
import nptgUtilities.custom_logger as cl
import logging
import random
import string
import time


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class SMS914PO(BasePage):
    log = cl.customer_logging(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    # ----------

    # Account information web elements
    _summary_section_css = '[data-id="tabpanel-tab_9"]'
    _account_name_css = 'input[data-id="name.fieldControl-text-box-text"]'
    _account_type_css = 'select[data-id="customertypecode.fieldControl-option-set-select"]'
    _account_ownership_css = 'select[data-id="ntg_ownership.fieldControl-option-set-select"]'
    _account_main_telephone_css = 'input[data-id="address1_line1.fieldControl-text-box-text"]'

    # Address information web elements
    _address_street1_css = 'input[data-id="address1_line1.fieldControl-text-box-text"]'
    _address_city_css = 'input[data-id="address1_city.fieldControl-text-box-text"]'
    _address_state_province_css = 'input[data-id="address1_stateorprovince.fieldControl-text-box-text"]'
    _address_zip_code_css = 'input[data-id="address1_postalcode.fieldControl-text-box-text"]'
    _address_country_css = '[data-id="address1_country.fieldControl-text-box-text"]'
    _address_county_css = '[data-id="address1_county.fieldControl-text-box-text"]'
    _address_county_wrapper_css = '[data-id="WebResource_countyselect-webResourceLabelControlWrapper"]'
    _address_country_frame = 'iframe[id="WebResource_countyselect"]'
    _address_count_value_css = 'select[id="countySelect"]'

    # contact information web elements
    _primary_contact_css = 'input[data-id="primarycontactid.fieldControl-LookupResultsDropdown_primarycontactid_' \
                           'textInputBox_with_filter_new"]'
    _maintenance_contract_contact_css = '[data-id="ntg_maintenancecontractcontact.fieldControl-' \
                                        'LookupResultsDropdown_ntg_maintenancecontractcontact_selected_tag_text"]'
    _rma_po_contact_css = '[data-id="ntg_rmapocontact.fieldControl' \
                          '-LookupResultsDropdown_ntg_rmapocontact_selected_tag_text"]'

    _save_button_css = 'data-id="account|NoRelationship|Form|Mscrm.Form.account.Save"'
    _save_close_button_css = 'data-id="account|NoRelationship|Form|Mscrm.Form.account.SaveAndClose"'
    _new_account_header_css = 'data-id="header_title"'

    # Test Data information
    _account_name = "Test_Account_" + random_generator(size=5)
    _account_type_value = "Direct Customer"
    _main_telephone = "512-876-9567"
    _owner_ship = "Investor Owned"
    _primary_contact = "972"
    _maintenance_contract_contact = "919"
    _rma_po_contact = "962"
    _address_street1 = "257 Bloomfield Ave"
    _address_city = "Austin"
    _address_state = "Texas"
    _address_zip_code = "78945"
    _address_country = "USA"
    _address_county = "AUSTIN"

    # Action methods

    def enter_account_name(self):
        self.element_click(self._account_name, locator_type="CSS")
        time.sleep(1)
        self.enter_data(self._account_name, locator=self._account_name_css, locator_type="CSS")

    def select_account_type(self):
        self.select_dropdown_item_text(self._account_type_value, self._account_type_css, locator_type="CSS")

    def select_owner_ship(self):
        self.select_dropdown_item_text(self._owner_ship, self._account_ownership_css, locator_type="CSS")

    def enter_main_telephone(self):
        self.web_page_down(self._summary_section_css, locator_type="CSS")
        self.element_click(self._account_main_telephone_css, locator_type="CSS")
        time.sleep(0.5)
        self.enter_data(self._main_telephone, self._account_main_telephone_css, locator_type="CSS")

    def enter_contact_information(self):
        self.element_click(self._primary_contact_css, locator_type="CSS")
        self.enter_data(self._primary_contact, self._primary_contact_css, locator_type="CSS")
        time.sleep(0.5)
        self.press_down_arrow()
        self.press_enter_key()
        time.sleep(0.5)
        self.element_click(self._maintenance_contract_contact_css, locator_type="CSS")
        self.enter_data(self._maintenance_contract_contact, self._maintenance_contract_contact_css, locator_type="CSS")
        time.sleep(0.5)
        self.press_down_arrow()
        self.press_enter_key()
        time.sleep(0.5)
        self.element_click(self._rma_po_contact_css, locator_type="CSS")
        self.enter_data(self._rma_po_contact, self._rma_po_contact_css, locator_type="CSS")
        time.sleep(0.5)
        self.press_down_arrow()
        self.press_enter_key()
        time.sleep(0.5)

    def enter_address_information(self):
        self.web_page_down(self._summary_section_css, locator_type="CSS")
        time.sleep(1)
        self.element_click(locator=self._address_street1_css, locator_type="CSS")
        self.enter_data(self._address_street1, locator=self._address_street1_css, locator_type="CSS")
        time.sleep(0.5)
        self.element_click(locator=self._address_city_css, locator_type="CSS")
        self.enter_data(self._address_city, locator=self._address_city_css, locator_type="CSS")
        time.sleep(0.5)
        self.element_click(self._address_state, locator_type="CSS")
        self.enter_data(self._address_state, self._address_state_province_css, locator_type="CSS")
        time.sleep(0.5)
        self.element_click(self._address_zip_code_css, locator_type="CSS")
        self.enter_data(self._address_zip_code, self._address_zip_code_css, locator_type="CSS")
        time.sleep(0.5)
        self.element_click(self._address_country_css, locator_type="CSS")
        self.enter_data(self._address_country, self._address_country_css, locator_type="CSS")
        time.sleep(0.5)
        self.select_dropdown_item_text(self._address_county, self._address_county_css, locator_type="CSS")
        time.sleep(0.5)

    def save_new_account(self):
        self.element_click(self._save_button_css, locator_type="CSS")
        self.wait_for_element_visible(self._new_account_header_css, locator_type="CSS", time_out=50)

    def verify_new_account_information(self):
        new_account_name = self.get_text(self._account_name_css, locator_type="CSS")


