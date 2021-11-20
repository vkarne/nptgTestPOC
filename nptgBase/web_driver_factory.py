"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class WebDriverFactory:

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def get_driver_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        base_url = "https://smsqa-ntgcrm.crm3.dynamics.com//"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            opt = Options()
            ser = Service("D:/Projects/drivers/chromedriver.exe")
            opt.add_argument("disable-extensions")
            # opt.add_experimental_option("debuggerAddress", "localhost:8989")
            opt.add_experimental_option("excludeSwitches", ["enable-automation", "load-extension"])
            opt.add_argument("user-data-dir=D:/Venkanna/chromeProfile")
            driver = webdriver.Chrome(service=ser, options=opt)
            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(3)
            driver.maximize_window()
            driver.get(base_url)
        else:
            # Set chrome driver
            opt = Options()
            ser = Service("D:/Projects/drivers/chromedriver.exe")
            opt.add_experimental_option("debuggerAddress", "localhost:8989")
            driver = webdriver.Chrome(service=ser, options=opt)
            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(3)
            driver.maximize_window()
            driver.get(base_url)

        return driver
