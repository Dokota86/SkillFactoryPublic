from selenium.webdriver.common.by import By


class MainPageLocators:
    S_AUTH_ID = (By.ID, "standard_auth_btn")
    GO_REGISTER_BUTTON_ID = (By.ID, "kc-register")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot_password")


class RegistrationPageLocators:
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    CITY_DROPDOWN_BUTTON = (By.CSS_SELECTOR, ".rt-select.rt-select--search.register-form__dropdown .rt-input.rt-input--actions .rt-input__action")
    CITY_OPTION = (lambda city_name: (By.XPATH, f"//div[@class='rt-select__list-item' and text()='{city_name}']"))
    EMAIL_INPUT = (By.ID, "address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "password-confirm")
    REGISTER_BUTTON_ID = (By.NAME, "register")
    ERROR_MESSAGES = (By.CSS_SELECTOR, "span.rt-input-container__meta.rt-input-container__meta--error")
    ALREADY_REGISTERED_EMAIL_MESSAGE = (By.CLASS_NAME, "card-modal__title")


class ConfirmationCodeLocators:
    CODE_INPUT_1 = (By.ID, "rt-code-0")
    CODE_INPUT_2 = (By.ID, "rt-code-1")
    CODE_INPUT_3 = (By.ID, "rt-code-2")
    CODE_INPUT_4 = (By.ID, "rt-code-3")
    CODE_INPUT_5 = (By.ID, "rt-code-4")
    CODE_INPUT_6 = (By.ID, "rt-code-5")


class LoginPageLocators:
    PHONE_TAB = (By.ID, "t-btn-tab-phone")
    EMAIL_TAB = (By.ID, "t-btn-tab-mail")
    LOGIN_TAB = (By.ID, "t-btn-tab-login")
    LS_TAB = (By.ID, "t-btn-tab-ls")
    CODE_INPUT = (By.ID, "address")
    PASSWORD_INPUT = (By.ID, "password")
    USERNAME_INPUT = (By.ID, "username")
    LOGIN_BUTTON = (By.ID, "kc-login")
    ERROR_MESSAGE = (By.ID, "form-error-message")
    BACK_GET_CODE_BUTTON = (By.ID, "back_to_otp_btn")
    GET_CODE_BUTTON = (By.ID, "otp_get_code")


class RecoveryPageLocators:
    CAPTCHA_INPUT = (By.ID, "captcha")
    PHONE_TAB = (By.ID, "t-btn-tab-phone")
    EMAIL_TAB = (By.ID, "t-btn-tab-mail")
    LOGIN_TAB = (By.ID, "t-btn-tab-login")
    LS_TAB = (By.ID, "t-btn-tab-ls")
    USERNAME_INPUT = (By.ID, "username")
    RESET_BUTTON = (By.ID, "reset")
    ERROR_MESSAGE = (By.ID, "form-error-message")
    FAQ_BUTTON = (By.ID, "faq-open")
    FAQ_OPEN = (By.CLASS_NAME, "faq-modal")
    BACK_BUTTON = (By.ID, "reset-back")
