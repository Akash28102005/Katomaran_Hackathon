from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestLoginPage:

    def test_continue_button(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        # Use a new email every time
        login.enter_email("testing123456789@gmail.com")

        login.click_continue()

        WebDriverWait(driver, 10).until(
            lambda d:
                "sign-up" in d.current_url.lower()
                or EC.presence_of_element_located((By.ID, "password"))(d)
        )

        assert (
            "sign-up" in driver.current_url.lower()
            or driver.find_elements(By.ID, "password")
        )