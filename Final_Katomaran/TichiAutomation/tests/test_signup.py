from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

from testdata.credentials import (
    FIRST_NAME,
    LAST_NAME,
    PHONE_NUMBER,
    SIGNUP_PASSWORD,
)


class TestSignup:

    def test_valid_signup_page(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        # Use an email that is NOT registered
        login.enter_email("newuser123456789@gmail.com")
        login.click_continue()

        signup = SignupPage(driver)

        signup.enter_first_name(FIRST_NAME)
        signup.enter_last_name(LAST_NAME)
        signup.enter_phone(PHONE_NUMBER)
        signup.enter_password(SIGNUP_PASSWORD)
        signup.enter_confirm_password(SIGNUP_PASSWORD)

        signup.click_remember()

        assert "sign-up" in driver.current_url.lower()

    def test_empty_first_name(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        login.enter_email("newuser123456789@gmail.com")
        login.click_continue()

        signup = SignupPage(driver)

        signup.enter_last_name(LAST_NAME)
        signup.enter_phone(PHONE_NUMBER)
        signup.enter_password(SIGNUP_PASSWORD)
        signup.enter_confirm_password(SIGNUP_PASSWORD)

        assert "sign-up" in driver.current_url.lower()

    def test_empty_last_name(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        login.enter_email("newuser123456789@gmail.com")
        login.click_continue()

        signup = SignupPage(driver)

        signup.enter_first_name(FIRST_NAME)
        signup.enter_phone(PHONE_NUMBER)
        signup.enter_password(SIGNUP_PASSWORD)
        signup.enter_confirm_password(SIGNUP_PASSWORD)

        assert "sign-up" in driver.current_url.lower()

    def test_password_mismatch(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        login.enter_email("newuser123456789@gmail.com")
        login.click_continue()

        signup = SignupPage(driver)

        signup.enter_first_name(FIRST_NAME)
        signup.enter_last_name(LAST_NAME)
        signup.enter_phone(PHONE_NUMBER)
        signup.enter_password("Test@12345")
        signup.enter_confirm_password("Wrong@12345")

        assert "sign-up" in driver.current_url.lower()