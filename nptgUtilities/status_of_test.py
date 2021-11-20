"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from traceback import print_stack
import nptgUtilities.custom_logger as cl
from nptgBase.selenium_driver import SeleniumDriver
import logging


class StatusOfTest(SeleniumDriver):
    log = cl.customer_logging(logging.DEBUG)

    def __init__(self, driver):
        super(StatusOfTest, self).__init__(driver)
        self.resultList = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: -- " + result_message)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: -- " + result_message)
                    self.screen_shot(result_message)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: -- " + result_message)
                self.screen_shot(result_message)
        except FileNotFoundError as err:
            self.resultList.append("FAIL")
            self.log.error(str(err) + "### Exception Occurred !!!")
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)

        if "FAIL" in self.resultList:
            self.log.error(test_name + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
