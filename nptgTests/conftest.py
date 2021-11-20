from nptgBase.web_driver_factory import WebDriverFactory
import pytest


@pytest.fixture()
def setup():
    print(" - Running method level setUp ")
    yield
    print(" - Running method level tearDown ")


@pytest.fixture(scope="class")
def one_time_setup(request, browser):
    print(" - Running one time setUp ")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.close()
    print(" - Running one time tearDown ")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os_type", help=" Type of operating system ")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--os_type")


# ------------------- PyTest HTML Report Generation --------------#

# ----------------- It is the hook for adding Environment information to HTML Report --------------- #
def pytest_configure(config):
    config._metadata['Project Name'] = 'Neptune SMS application'
    config._metadata['Module Name'] = 'Test Accounts Page Open'
    config._metadata['Tester'] = 'Venkanna Karne'


# ----------------- It is the hook for delete/modify Environment information to HTML Report --------------- #
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

