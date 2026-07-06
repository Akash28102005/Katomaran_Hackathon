from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")
    CONTINUE = (By.XPATH, "//button[@type='submit']")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.XPATH, "//button[@type='submit']")

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def click_continue(self):

        button = self.get_element(self.CONTINUE)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        self.wait.until(
            lambda d:
            "sign-up" in d.current_url.lower()
            or self.driver.find_elements(By.ID, "password")
        )

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def click_login(self):

        button = self.get_element(self.LOGIN)

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

    def login(self, email, password):

        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_login()