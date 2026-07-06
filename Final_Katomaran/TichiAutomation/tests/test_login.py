from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage

from testdata.credentials import (
    VALID_EMAIL,
    VALID_PASSWORD,
    INVALID_PASSWORD,
)


class TestLogin:

    def test_valid_login(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        login.login(
            VALID_EMAIL,
            VALID_PASSWORD
        )

        import time
        time.sleep(5)

        print("\nCurrent URL:", driver.current_url)
        print("\nPage Title:", driver.title)

    def test_invalid_password(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        login.login(
            VALID_EMAIL,
            INVALID_PASSWORD
        )

        WebDriverWait(driver, 10).until(
            lambda d:
            "login" in d.current_url.lower()
            or "password" in d.page_source.lower()
        )

        assert (
            "login" in driver.current_url.lower()
            or "password" in driver.page_source.lower()
        )

    def test_password_field_visible(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        login.enter_email(VALID_EMAIL)
        login.click_continue()

        password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        )

        assert password.is_displayed()