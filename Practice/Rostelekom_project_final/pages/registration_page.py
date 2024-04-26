from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.locators import RegistrationPageLocators


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_registration_form(self, first_name, last_name, email, password, confirm_password):
        first_name_input = self.driver.find_element(*RegistrationPageLocators.FIRST_NAME_INPUT)
        first_name_input.send_keys(first_name)
        last_name_input = self.driver.find_element(*RegistrationPageLocators.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)
        email_input = self.driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        confirm_password_input = self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(confirm_password)

    def click_city_dropdown_button(self):
        dropdown_button = self.wait.until(EC.visibility_of_element_located
                                          (RegistrationPageLocators.CITY_DROPDOWN_BUTTON))
        dropdown_button.click()

    def scroll_to_city(self, city_name):
        city_locator = RegistrationPageLocators.CITY_OPTION(city_name)
        city_element = self.driver.find_element(*city_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(city_element).perform()

    def select_city(self, city_name):
        city_locator = RegistrationPageLocators.CITY_OPTION(city_name)
        city_element = self.driver.find_element(*city_locator)
        city_element.click()

    def click_register_button(self):
        register_button = self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON_ID)
        register_button.click()

