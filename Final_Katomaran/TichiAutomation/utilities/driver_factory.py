from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.config import Config


class DriverFactory:

    @staticmethod
    def get_driver():

        options = webdriver.ChromeOptions()

        # Keeps browser open after execution (optional)
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

        if Config.MAXIMIZE_WINDOW:
            driver.maximize_window()

        driver.implicitly_wait(5)

        return driver

    @staticmethod
    def quit_driver(driver):

        if driver:
            driver.quit()