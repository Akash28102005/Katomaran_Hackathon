from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


class TestSignupPage:

    def test_signup_page_loads(self, driver):

        home = HomePage(driver)
        home.click_sign_in()

        login = LoginPage(driver)

        login.enter_email("newuser123456@gmail.com")
        login.click_continue()

        signup = SignupPage(driver)

        assert signup.wait.until(
            lambda d: "sign-up" in d.current_url.lower()
        )