from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    PHONE = (By.ID, "phoneNumber")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirmPassword")
    REMEMBER = (By.ID, "remember")
    SIGNUP = (By.XPATH, "//button[@type='submit']")

    def enter_first_name(self, firstname):
        self.type(self.FIRST_NAME, firstname)

    def enter_last_name(self, lastname):
        self.type(self.LAST_NAME, lastname)

    def enter_phone(self, phone):
        self.type(self.PHONE, phone)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def enter_confirm_password(self, password):
        self.type(self.CONFIRM_PASSWORD, password)

    def click_remember(self):
        self.click(self.REMEMBER)

    def click_signup(self):
        self.click(self.SIGNUP)

    def signup(self, firstname, lastname, phone, password):

        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_phone(phone)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_remember()
        self.click_signup()