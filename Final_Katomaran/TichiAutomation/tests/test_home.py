from pages.home_page import HomePage


class TestHome:

    def test_home_page_title(self, driver):

        home = HomePage(driver)

        assert "tichi" in home.get_title().lower()

    def test_signin_navigation(self, driver):

        home = HomePage(driver)

        home.click_sign_in()

        assert "/login" in driver.current_url.lower()