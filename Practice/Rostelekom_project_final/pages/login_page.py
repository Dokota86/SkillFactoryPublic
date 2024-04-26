from selenium.webdriver.support.ui import WebDriverWait
from utilities.locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_phone_tab(self):
        phone_tab = self.driver.find_element(*LoginPageLocators.PHONE_TAB)
        phone_tab.click()

    def click_email_tab(self):
        email_tab = self.driver.find_element(*LoginPageLocators.EMAIL_TAB)
        email_tab.click()

    def click_login_tab(self):
        login_tab = self.driver.find_element(*LoginPageLocators.LOGIN_TAB)
        login_tab.click()

    def click_ls_tab(self):
        ls_tab = self.driver.find_element(*LoginPageLocators.LS_TAB)
        ls_tab.click()

    def enter_phone_number(self, phone_number):
        phone_input = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
        phone_input.send_keys(phone_number)

    def enter_password(self, password):
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def enter_username(self, username):
        username_input = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def click_login_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def click_back_get_code_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.BACK_GET_CODE_BUTTON)
        login_button.click()
    def click_get_code_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.GET_CODE_BUTTON)
        login_button.click()

    def enter_email(self, username):
        username_input = self.driver.find_element(*LoginPageLocators.CODE_INPUT)
        username_input.clear()
        username_input.send_keys(username)
