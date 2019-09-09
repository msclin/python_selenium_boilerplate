import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tests import config


def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='https://www.google.com',
        help='base URL for the application under test'
    )

    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='browser used for testing'
    )


@pytest.fixture()
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.browser = request.config.getoption('--browser')

    _driver = None

    if config.browser == 'chrome':
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')

        _driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options,
            desired_capabilities=DesiredCapabilities.CHROME
        )
    elif config.browser == 'firefox':
        _driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
    else:
        pytest.fail(f'Do not recognize the --browser option "{config.browser}." Valid options: chrome, firefox')

    def _quit():
        _driver.quit()

    request.addfinalizer(_quit)

    return _driver
