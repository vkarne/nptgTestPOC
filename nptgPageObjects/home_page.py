from nptgBase.base_page import BasePage
import nptgUtilities.custom_logger as cl
import logging


class OpenAccountPage(BasePage):
    log = cl.customer_logging(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #  Locators
    _menu_icon_css = 'span.symbolFont.SiteMap-symbol'
    _home_link_css = '[data-text="Home"]'
    _dashboard_link_id = 'sitemap-entity-nav_dashboards'
    _dashboards_selector_id = 'Dashboard_Selector'
    _account_link_id = 'sitemap-entity-nav_accts'
    _show_chart_btn_id = 'ShowChartPane-button'
    _my_active_accounts_xpath = '//span[text()="My Active Accounts"]'
    _active_accounts_xpath = '//span[text()="Active Accounts"]'
    _property = '"aria-selected"'

    def click_on_menu_icon(self):
        self.element_click(self._menu_icon_css, locator_type="CSS")

    def click_on_account_link(self):
        self.element_click(self._account_link_id, locator_type="ID")

    def verify_show_chart_button(self):
        show_chart_btn_element = self.wait_for_element_visible(self._show_chart_btn_id, locator_type="ID")
        is_shows = self.is_element_displayed(element=show_chart_btn_element)
        if is_shows:
            self.log.info('SHow Chart Button is Displayed as expected - TEST PASSED')
        else:
            self.log.error('SHow Chart Button is NOT Displayed - TEST FAILED')

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











