import time
from selenium import webdriver
from pages.base import MainPage
from pages.login_page import LoginPage
from utilities.locators import LoginPageLocators


# Тест-кейс 7: Авторизация по номеру телефона
def test_phone_authentication():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Переход на вход по номеру телефона
    login_page = LoginPage(driver)
    login_page.click_phone_tab()
    # Заполняем поля верными данными
    login_page.enter_phone_number("9876543210")
    login_page.enter_password("12345678Qq")
    # Нажимаем кнопку Войти
    login_page.click_login_button()
    time.sleep(2)
    # Проверка успешной аутентификации
    if "https://start.rt.ru/?tab=main" in driver.current_url:
        print("Аутентификации прошла успешно!")
    else:
        print("Аутентификации не удалась.")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 8: Авторизация по почте
def test_email_authentication():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Переход на вход по почте
    login_page = LoginPage(driver)
    login_page.click_email_tab()
    # Заполняем поля верными данными
    login_page.enter_username("erik.krou@example.com")
    login_page.enter_password("12345678Qq")
    # Нажимаем кнопку Войти
    login_page.click_login_button()
    time.sleep(2)
    # Проверка успешной аутентификации
    if "https://start.rt.ru/?tab=main" in driver.current_url:
        print("Аутентификации прошла успешно!")
    else:
        print("Аутентификации не удалась.")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 9: Авторизация по логину
def test_login_authentication():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Переход на вход по логину
    login_page = LoginPage(driver)
    login_page.click_login_tab()
    # Заполняем поля верными данными
    login_page.enter_username("erik.krou")
    login_page.enter_password("12345678Qq")
    # Нажимаем кнопку Войти
    login_page.click_login_button()
    time.sleep(2)
    # Проверка успешной аутентификации
    if "https://start.rt.ru/?tab=main" in driver.current_url:
        print("Аутентификации прошла успешно!")
    else:
        print("Аутентификации не удалась.")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 10: Авторизация по лицевому счету
def test_account_authentication():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Переход на вход по лицевому счету
    login_page = LoginPage(driver)
    login_page.click_ls_tab()
    # Заполняем поля верными данными
    login_page.enter_username("1111111111111")
    login_page.enter_password("12345678Qq")
    # Нажимаем кнопку Войти
    login_page.click_login_button()
    time.sleep(2)
    # Проверка успешной аутентификации
    if "https://start.rt.ru/?tab=main" in driver.current_url:
        print("Аутентификации прошла успешно!")
    else:
        print("Аутентификации не удалась.")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 11: Ошибка при некорректном вводе номера телефона и пароля
def test_phone_number_authentication_error():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Переход на вход по номеру телефона
    login_page = LoginPage(driver)
    login_page.click_phone_tab()
    # Ввод некорректного номера телефона и/или пароля
    login_page.enter_phone_number("9876543210")
    login_page.enter_password("12345678Qq")
    # Нажатие кнопки авторизации
    login_page.click_login_button()
    time.sleep(2)
    # Проверка отображения сообщения об ошибке
    error_messages = main_page.get_error_messages(LoginPageLocators.ERROR_MESSAGE)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить авторизацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 12: Ошибка при некорректном вводе почты и пароля
def test_email_authentication_error():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Переход на вход по почте
    login_page = LoginPage(driver)
    login_page.click_email_tab()
    # Ввод некорректного e-mail и/или пароля
    login_page.enter_username("erik.krou@example.com")
    login_page.enter_password("12345678Qq")
    # Нажатие кнопки авторизации
    login_page.click_login_button()
    time.sleep(2)
    # Проверка отображения сообщения об ошибке
    error_messages = main_page.get_error_messages(LoginPageLocators.ERROR_MESSAGE)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить авторизацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 13: Проверка работоспособности кнопки возрата на вход временному коду
def test_back_get_code_button():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Запомните текущий URL
    initial_url = driver.current_url
    # Найдите кнопку возврата назад и нажмите на нее
    login_page = LoginPage(driver)
    login_page.click_back_get_code_button()
    time.sleep(2)
    # Запрос подтверждения, что произошло возвращение на авторизацию по временному коду
    if initial_url == driver.current_url:
        print("Кнопка возврата назад не работает")
    else:
        print("Кнопка возврата назад работает")
    # Закрыть браузер
    driver.quit()


# Тест-кейс 14: Авторизация по временному коду
def test_temporary_code_authentication():
    # Открытие страницы авторизации
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    main_page.click_auth_link()
    time.sleep(2)
    # Ввод номера телефона/почты
    login_page = LoginPage(driver)
    login_page.enter_email("erik.krou@example.com")
    # Нажатие кнопки "Получить код"
    login_page.click_get_code_button()
    # Ожидание получения кода
    time.sleep(2)
    base = MainPage(driver)
    base.fill_confirmation_code(
        "123456")
    time.sleep(2)
    # Проверка успешной аутентификации
    if "https://start.rt.ru/?tab=main" in driver.current_url:
        print("Аутентификации прошла успешно!")
    else:
        print("Аутентификации не удалась.")
    # Закрытие браузера
    driver.quit()
