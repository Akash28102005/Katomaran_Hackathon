from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utilities.config import Config


class HomePage(BasePage):

    SIGN_IN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Sign In')]"
    )

    def open(self):
        self.driver.get(Config.BASE_URL)

    def click_sign_in(self):

        button = self.get_element(self.SIGN_IN_BUTTON)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            EC.url_contains("/login")
        )