from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from traceback import print_stack
import nptgUtilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:
    log = cl.customer_logging(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../nptgScreens/"
        relative_filename = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_filename)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except FileNotFoundError as err:
            self.log.error(str(err) + "### Exception Occurred when taking screenshot")
            print_stack()

    def get_page_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()

        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "classname":
            return By.CLASS_NAME
        elif locator_type == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info('locator type ' + locator_type + 'not correct or supported, please check...!')

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locator_type)
        except Exception as err:
            self.log.error("Element not found with locator: " + locator + " and  locatorType: "
                           + locator_type + "Error is: " + str(err))
        return element

    def get_element_list(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except Exception as err:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type + "error Msg is: " + str(err) )
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot click on the element with locator: " + locator + " locatorType: "
                           + locator_type)
            print_stack()

    def enter_data(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def select_dropdown_item_text(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            select_item = Select(element)
            select_item.select_by_visible_text(data)

            self.log.info("Selected item from dropdown by text "
                          "with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot select item from dropdown list with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def select_dropdown_item_value(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            select_item = Select(element)
            select_item.select_by_value(data)

            self.log.info("Selected item from dropdown by value "
                          "with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot select item from dropdown list with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def select_dropdown_item_index(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            select_item = Select(element)
            select_item.select_by_index(data)

            self.log.info("Selected item from dropdown by value "
                          "with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot select item from dropdown list with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)

            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))

            if len(text) == 0:
                text = element.get_attribute("innerHTML")

            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()

        except Exception as err:
            self.log.error(str(err) + "Failed to get text on element" + info)
            print_stack()
            text = None
        return text

    def get_element_attribute(self, data, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)

            attribute_value = element.get_attribute(data)

            if len(attribute_value) != 0:
                self.log.info("Getting attribute on element :: " + info)
                self.log.info("The attribute value is :: " + str(attribute_value))
                attribute_value = attribute_value.strip()

        except Exception as err:
            self.log.error(str(err) + "Failed to get text on element" + info)
            print_stack()
            attribute_value = None
        return attribute_value

    def is_element_present(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)

            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.error("Element not present with locator: " + locator + " locatorType: " + locator_type)
                return False

        except Exception as err:
            self.log.error(str(err) + "Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        displayed_flag = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)

            if element is not None:
                displayed_flag = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.error("Element not displayed with locator: " + locator + " locatorType: " + locator_type)
            return displayed_flag

        except Exception as err:
            print(str(err) + "Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except Exception as err:
            self.log.error(str(err) + "Element not found")
            return False

    def wait_for_element_click(self, locator, locator_type="id", time_out=15, time_frequency=1):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(time_out) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=time_out, poll_frequency=time_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     TimeoutException,
                                                     ElementNotVisibleException,
                                                     ElementNotInteractableException,
                                                     ElementClickInterceptedException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")

        except Exception as err:
            self.log.error("Element is not visible error:: " + str(err) + "please check...!")
            print_stack()
        return element

    def wait_for_element_visible(self, locator, locator_type="id", time_out=20, time_frequency=1):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(time_out) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=time_out, poll_frequency=time_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     TimeoutException,
                                                     ElementNotVisibleException])
            element = wait.until(ec.visibility_of_element_located((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except Exception as err:
            self.log.error("Element is not visible error:: " + str(err) + "please check...!")
            print_stack()
            return element

        return element

    def web_scroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def scroll_to_element(self, locator, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)

            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Scrolled to the element with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot select item from dropdown list with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def web_page_up(self, locator, locator_type="id"):
        element = None
        try:
            if locator:
                locator_type = locator_type.lower()
                by_type = self.get_by_type(locator_type)
                element = self.driver.find_element(by_type, locator)

            element.send_keys(Keys.PAGE_UP)
            self.log.info("Scrolled to Page Up with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot select item from dropdown list with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def web_page_down(self, locator, locator_type="id"):
        element = None
        try:
            if locator:
                locator_type = locator_type.lower()
                by_type = self.get_by_type(locator_type)
                element = self.driver.find_element(by_type, locator)

            element.send_keys(Keys.PAGE_DOWN)
            self.log.info("Scrolled to Page Up with locator: " + locator + " locatorType: " + locator_type)

        except Exception as err:
            self.log.error(str(err) + "Cannot select item from dropdown list with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def press_up_arrow(self):
        try:
            actions = ActionChains(self.driver)
            actions.key_up(Keys.ARROW_UP).perform()
        except Exception as err:
            self.log.error(str(err) + "Key press not happened")
            print_stack()

    def press_down_arrow(self):
        try:
            actions = ActionChains(self.driver)
            actions.key_up(Keys.ARROW_DOWN).perform()
        except Exception as err:
            self.log.error(str(err) + "Key press not happened")
            print_stack()

    def press_enter_key(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)

        except Exception as err:
            self.log.error(str(err) + "Key press not happened")
            print_stack()

    def press_tab_key(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.TAB)

        except Exception as err:
            self.log.error(str(err) + "Key press not happened")
            print_stack()




