from nptgBase.base_page import BasePage
import nptgUtilities.custom_logger as cl
import logging
import time


class SMS888PO(BasePage):
    log = cl.customer_logging(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    # ----------

    # Account information web elements
    _home_link_css = '[data-text="Home"]'
    _dashboard_link_id = 'sitemap-entity-nav_dashboards'
    _dashboards_selector_id = 'Dashboard_Selector'
    _account_link_id = 'sitemap-entity-nav_accts'
    _show_chart_btn_id = 'ShowChartPane-button'
    _my_active_accounts_xpath = '//span[text()="My Active Accounts"]'
    _active_accounts_xpath = '//span[normalize-space()="Active Accounts"]'
    _all_accounts_xpath = '//span[normalize-space()="All Accounts"]'
    _first_account_rec_xpath = '//span[normalize-space()="1026560 ALBERTA LTD (CEDARS PARK)"]'
    _summary_section_css = '[data-id="tabpanel-tab_9"]'
    _account_name_css = 'input[data-id="name.fieldControl-text-box-text"]'
    _account_type_css = 'select[data-id="customertypecode.fieldControl-option-set-select"]'
    _parent_account_css = 'input[aria-label="Parent Account, Lookup"]'
    _managing_distributor_css = 'input[aria-label="Managing Distributor, Lookup"]'
    _international_customer_css = 'input[data-id="ntg_internationalcustomer.fieldControl-checkbox-empty"]'
    _ownership_css = 'select[data-id="ntg_ownership.fieldControl-option-set-select"]'
    _site_id_css = '[data-id="ntg_siteidnumber.fieldControl-text-box-text"]'
    _pin_css = '[data-id="ntg_pinnumber.fieldControl-text-box-text"]'
    _priority_css = 'select[data-id="ntg_prioritycode.fieldControl-option-set-select"]'
    _price_list_css = 'div[data-id="defaultpricelevelid' \
                      '.fieldControl-LookupResultsDropdown_defaultpricelevelid_selected_tag_text"]'
    _comments_css = 'textarea[data-id="description.fieldControl-text-box-text"]'
    _automation_source_css = '[data-id="ntg_automationsource.fieldControl-option-set-select"]'
    _website_css = '[data-id="websiteurl.fieldControl-url-text-input"]'
    _email_css = '[data-id="emailaddress1.fieldControl-mail-text-input"]'
    _main_telephone_css = '[data-id="telephone1.fieldControl-phone-text-input"]'
    _fax_css = '[data-id="fax.fieldControl-text-box-text"]'

    # address information web elements
    _address_street1_css = '[data-id="address1_line1.fieldControl-text-box-text"]'
    _address_street2_css = '[data-id="address1_line2.fieldControl-text-box-text"]'
    _address_city_css = '[data-id="address1_city.fieldControl-text-box-text"]'
    _address_state_province_css = '[data-id="address1_stateorprovince.fieldControl-text-box-text"]'
    _address_zip_code_css = '[data-id="address1_postalcode.fieldControl-text-box-text"]'
    _address_country_css = '[data-id="address1_country.fieldControl-text-box-text"]'
    _address_county_css = '[data-id="address1_county.fieldControl-text-box-text"]'

    # Billing Information web elements
    _bill_to_account_css = 'select[data-id="ntg_isbilltoaccountdifferentthanthisaccount' \
                           '.fieldControl-option-set-select"]'
    _bill_to_erp_css = 'input[data-id="ntg_erpid.fieldControl-text-box-text"]'

    # Contact information web elements
    _primary_contact_css = '[data-id="primarycontactid' \
                           '.fieldControl-LookupResultsDropdown_primarycontactid_selected_tag_text"]'
    _maintenance_contract_contact_css = '[data-id="ntg_maintenancecontractcontact.fieldControl-' \
                                        'LookupResultsDropdown_ntg_maintenancecontractcontact_selected_tag_text"]'
    _rma_po_contact_css = '[data-id="ntg_rmapocontact.fieldControl' \
                          '-LookupResultsDropdown_ntg_rmapocontact_selected_tag_text"]'
    _ami_service_contact_css = 'input[data-id="ntg_amiservicecontact.fieldControl' \
                               '-LookupResultsDropdown_ntg_amiservicecontact_textInputBox_with_filter_new"]'

    # Territory information web elements
    _owner_css = '[data-id="ownerid.fieldControl-LookupResultsDropdown_ownerid_SelectedRecordList"]'
    _region_css = '[data-id="ntg_regionid.fieldControl-LookupResultsDropdown_ntg_regionid_SelectedRecordList"]'
    _district_css = 'input[data-id="ntg_districtid.fieldControl' \
                    '-LookupResultsDropdown_ntg_districtid_textInputBox_with_filter_new"]'
    _territory_css = '[data-id="ntg_territoryid.fieldControl-LookupResultsDropdown_ntg_territoryid_SelectedRecordList"]'
    _customer_success_specialist_css = '[data-id="Customer_Support_Specialist"]'

    # Action method of sms-888

    def click_on_account_link(self):
        self.element_click(self._account_link_id, locator_type="ID")

    def verify_show_chart_button(self):
        show_chart_btn_element = self.wait_for_element_visible(self._show_chart_btn_id, locator_type="ID")
        is_shows = self.is_element_displayed(element=show_chart_btn_element)
        if is_shows:
            self.log.info('SHow Chart Button is Displayed as expected - TEST PASSED')
        else:
            self.log.error('SHow Chart Button is NOT Displayed - TEST FAILED')

    def select_active_account(self):
        self.element_click(self._my_active_accounts_xpath, locator_type="XPATH")
        time.sleep(2)
        self.element_click(self._active_accounts_xpath, locator_type="XPATH")

    def verify_active_accounts_listed(self):
        is_record_visible = self.wait_for_element_visible(self._first_account_rec_xpath, locator_type="XPATH")
        if is_record_visible:
            self.log.info("All the active records are displayed ase expected TEST PASSED")
            return True
        else:
            self.log.error("There is an error opening the active accounts TEST FAILED")
            return False

    def open_active_account_details(self):
        self.element_click(self._first_account_rec_xpath, locator_type="XPATH")

    def verify_account_details_opened(self):
        is_account_name_visible = self.wait_for_element_visible(self._account_name_css, locator_type="CSS")
        if is_account_name_visible:
            self.log.info("selected active account details opened as expected - TEST PASSED")
            return True
        else:
            self.log.error("There is an error opening account details  TEST FAILED")

    def verify_account_info_fields(self):
        account_name_field = self.is_element_present(locator=self._account_name_css, locator_type="CSS")
        account_type_field = self.is_element_present(locator=self._account_type_css, locator_type="CSS")
        parent_account_field = self.is_element_present(locator=self._parent_account_css, locator_type="CSS")
        managing_distributor_field = self.is_element_present(locator=self._managing_distributor_css, locator_type="CSS")
        international_customer_field = self.is_element_present(locator=self._international_customer_css,
                                                               locator_type="CSS")
        ownership_field = self.is_element_present(locator=self._ownership_css, locator_type="CSS")
        self.web_page_down(self._summary_section_css, locator_type="CSS")
        site_id_field = self.is_element_present(locator=self._site_id_css, locator_type="CSS")
        pin_filed = self.is_element_present(locator=self._pin_css, locator_type="CSS")
        priority_filed = self.is_element_present(locator=self._priority_css, locator_type="CSS")
        price_list_field = self.is_element_present(locator=self._price_list_css, locator_type="CSS")
        comments_field = self.is_element_present(locator=self._comments_css, locator_type="CSS")
        self.web_page_down(self._summary_section_css, locator_type="CSS")
        automation_source_field = self.is_element_present(locator=self._automation_source_css, locator_type="CSS")
        web_site_field = self.is_element_present(locator=self._website_css, locator_type="CSS")
        email_field = self.is_element_present(locator=self._email_css, locator_type="CSS")
        main_telephone_field = self.is_element_present(locator=self._main_telephone_css, locator_type="CSS")
        fax_field = self.is_element_present(locator=self._fax_css, locator_type="CSS")
        if (account_name_field and account_type_field and parent_account_field and managing_distributor_field and
                international_customer_field and ownership_field and site_id_field and pin_filed and
                priority_filed and price_list_field and comments_field and automation_source_field and
                web_site_field and email_field and main_telephone_field and fax_field):
            self.log.info("Account information fields are displayed as expected TEST PASSED")
            return True
        else:
            self.log.error("Either any of account information field NOT displayed or something went wrong TEST FAILED")
            return False

    def verify_address_info_fields(self):
        self.web_page_down(self._summary_section_css, locator_type="CSS")
        address_street1 = self.is_element_present(self._address_street1_css, locator_type="CSS")
        address_street2 = self.is_element_present(locator=self._address_street2_css, locator_type="CSS")
        address_city = self.is_element_present(locator=self._address_city_css, locator_type="CSS")
        address_state_province = self.is_element_present(locator=self._address_state_province_css, locator_type="CSS")
        address_zip_code = self.is_element_present(locator=self._address_zip_code_css, locator_type="CSS")
        address_country = self.is_element_present(locator=self._address_country_css, locator_type="CSS")
        address_county = self.is_element_present(locator=self._address_county_css, locator_type="CSS")
        if (address_street1 and address_street2 and address_city and address_state_province and
                address_zip_code and address_country and address_county):
            self.log.info("Physical address information fields are displayed as expected TEST PASSED")
            return True
        else:
            self.log.error("Either any of address information field NOT displayed or something went wrong TEST FAILED")
            return False

    def verify_billing_info_fields(self):
        bill_to_account = self.is_element_present(locator=self._bill_to_account_css, locator_type="CSS")
        bill_to_erp = self.is_element_present(locator=self._bill_to_erp_css, locator_type="CSS")
        if bill_to_account and bill_to_erp:
            self.log.info("Billing information fields are displayed as expected TEST PASSED")
            return True
        else:
            self.log.error("Either any of billing info field NOT displayed or something went wrong TEST FAILED")
            return False

    def verify_contact_info_fields(self):
        primary_contact = self.is_element_present(locator=self._primary_contact_css, locator_type="CSS")
        maintenance_contract_contact = self.is_element_present(locator=self._maintenance_contract_contact_css,
                                                               locator_type="CSS")
        rma_po_contact = self.is_element_present(locator=self._rma_po_contact_css, locator_type="CSS")
        ami_service_contact = self.is_element_present(locator=self._ami_service_contact_css, locator_type="CSS")
        if primary_contact and maintenance_contract_contact and rma_po_contact and ami_service_contact:
            self.log.info("Contract information fields are displayed as expected TEST PASSED")
            return True
        else:
            self.log.error("Either  any of contract info field NOT displayed or something went wrong TEST FAILED")
            return False

    def verify_territory_info_fields(self):
        owner_field = self.is_element_present(locator=self._owner_css, locator_type="CSS")
        region_field = self.is_element_present(locator=self._region_css, locator_type="CSS")
        district_field = self.is_element_present(locator=self._district_css, locator_type="CSS")
        territory_field = self.is_element_present(locator=self._territory_css, locator_type="CSS")
        customer_success_specialist = self.is_element_present(locator=self._customer_success_specialist_css,
                                                              locator_type="CSS")
        if owner_field and region_field and district_field and territory_field and customer_success_specialist:
            self.log.info("Territory information fields are displayed as expected TEST PASSED")
            return True
        else:
            self.log.error("Either any of territory info field NOT displayed oe something went wrong TEST FAILED")
            return False

    def click_on_home_link(self):
        self.element_click(self._home_link_css, locator_type="CSS")

    def verify_default_page(self):
        visible_flag = self.is_element_displayed(self._dashboards_selector_id, locator_type="ID")
        if visible_flag:
            self.log.info("DashBoard link is default page when SMS application launched - TEST PASSED")
            return True
        else:
            self.log.error('There is an error to have DashBoard link as default page - TEST FAILED')
            return False

