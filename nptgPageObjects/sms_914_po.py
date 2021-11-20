from nptgBase.base_page import BasePage
import nptgUtilities.custom_logger as cl
import logging
import random
import string


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

    _save_button_xpath = '//button[@aria-label="Save (CTRL+S)"]'
    _save_close_button_xpath = '//button[@aria-label="Save & Close"]'

    # Test Data information
    _account_name = "Test_Account_" + random_generator()
    _account_type_value = "Direct Customer"
    _owner_ship = "Investor Owned"
    _primary_contact = "972"
    _maintenance_contract_contact = "919"
    _rma_po_contact = "962"

    # Action methods

    def enter_account_name(self):
        self.enter_data(self._account_name, locator=self._account_name_css, locator_type="CSS")

    def select_account_type(self):
        self.select_dropdown_item_text(self._account_type_value, self._account_type_css, locator_type="CSS")

    def select_owner_ship(self):
        self.select_dropdown_item_text(self._owner_ship, self._account_ownership_css, locator_type="CSS")

    def enter_maintenance_contract_contact(self):
        self.enter_data(self._maintenance_contract_contact, self._account_main_telephone_css, locator_type="CSS")
