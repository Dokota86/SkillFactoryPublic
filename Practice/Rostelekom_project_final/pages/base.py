from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from utilities.locators import MainPageLocators, ConfirmationCodeLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_register_link(self):
        # Переход на страницу с возможностью выбора функции - зарегистрироваться
        s_auth_button = self.wait.until(EC.visibility_of_element_located(MainPageLocators.S_AUTH_ID))
        # Нажатие на кнопку
        s_auth_button.click()
        # Переход на страницу регистрации
        register_button = self.wait.until(EC.visibility_of_element_located(MainPageLocators.GO_REGISTER_BUTTON_ID))
        register_button.click()

    def click_auth_link(self):
        # Переход на страницу авторизации
        s_auth_button = self.wait.until(EC.visibility_of_element_located(MainPageLocators.S_AUTH_ID))
        # Нажатие на кнопку
        s_auth_button.click()

    def click_recovery_link(self):
        # Переход на страницу с возможностью выбора функции - зарегистрироваться
        s_auth_button = self.wait.until(EC.visibility_of_element_located(MainPageLocators.S_AUTH_ID))
        # Нажатие на кнопку
        s_auth_button.click()
        # Переход на страницу восстановления пароля
        register_button = self.wait.until(EC.visibility_of_element_located(MainPageLocators.FORGOT_PASSWORD_LINK))
        register_button.click()

    def find_error_elements(self, error_locator):
        try:
            return self.driver.find_elements(*error_locator)
        except NoSuchElementException:
            return []

    def get_error_messages(self, error_locator):
        error_elements = self.find_error_elements(error_locator)
        error_message = [error_element.text for error_element in error_elements]
        return error_message

    def fill_confirmation_code(self, code):
        code_inputs = [
            ConfirmationCodeLocators.CODE_INPUT_1,
            ConfirmationCodeLocators.CODE_INPUT_2,
            ConfirmationCodeLocators.CODE_INPUT_3,
            ConfirmationCodeLocators.CODE_INPUT_4,
            ConfirmationCodeLocators.CODE_INPUT_5,
            ConfirmationCodeLocators.CODE_INPUT_6
        ]
        for i, locator in enumerate(code_inputs):
            code_input = self.driver.find_element(*locator)
            code_input.send_keys(code[i])

