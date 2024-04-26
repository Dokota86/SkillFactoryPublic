from utilities.locators import RecoveryPageLocators


class RecoveryPage:
    def __init__(self, driver):
        self.driver = driver

    def click_phone_tab(self):
        phone_tab = self.driver.find_element(*RecoveryPageLocators.PHONE_TAB)
        phone_tab.click()

    def click_email_tab(self):
        email_tab = self.driver.find_element(*RecoveryPageLocators.EMAIL_TAB)
        email_tab.click()

    def click_login_tab(self):
        login_tab = self.driver.find_element(*RecoveryPageLocators.LOGIN_TAB)
        login_tab.click()

    def click_ls_tab(self):
        ls_tab = self.driver.find_element(*RecoveryPageLocators.LS_TAB)
        ls_tab.click()

    def enter_captcha(self, captcha):
        phone_input = self.driver.find_element(*RecoveryPageLocators.CAPTCHA_INPUT)
        phone_input.send_keys(captcha)

    def enter_username(self, username):
        username_input = self.driver.find_element(*RecoveryPageLocators.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def click_reset_button(self):
        reset_button = self.driver.find_element(*RecoveryPageLocators.RESET_BUTTON)
        reset_button.click()

    def click_faq_button(self):
        aq_button = self.driver.find_element(*RecoveryPageLocators.FAQ_BUTTON)
        aq_button.click()

    def find_faq_open(self):
        return self.driver.find_element(*RecoveryPageLocators.FAQ_OPEN)

    def click_back_button(self):
        back_button = self.driver.find_element(*RecoveryPageLocators.BACK_BUTTON)
        back_button.click()
