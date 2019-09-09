from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from tests import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _click(self, locator):
        self._find(locator).click()

    def _find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _is_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(visibility_of_element_located((locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _type(self, locator, input_text, clear_input=False, terminate_with_return_key=False):
        input_element = self._find(locator)

        if clear_input:
            input_element.clear()

        input_element.send_keys(input_text)

        if terminate_with_return_key:
            input_element.send_keys(Keys.RETURN)

    def _visit(self, url):
        if url.startswith('http'):
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)
