from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.config import Config


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def is_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url