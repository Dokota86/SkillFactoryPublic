import time
from selenium import webdriver
from pages.base import MainPage
from pages.registration_page import RegistrationPage
from utilities.locators import RegistrationPageLocators


# Тест-кейс 1: Успешная регистрация
def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_register_link()
    time.sleep(2)
    # Заполняем поля верными данными
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("Эрик", "Кроу", "erik.krou@example.com", "12345678Qq", "12345678Qq")
    # Нажимаем на кнопку для открытия списка городов
    registration_page.click_city_dropdown_button()
    # Добавляем задержку для открытия списка
    time.sleep(1)
    # Прокручиваем список до города Саратовская обл
    registration_page.scroll_to_city("Саратовская обл")
    # Выбираем город из списка
    registration_page.select_city("Саратовская обл")
    # Нажимаем кнопку Зарегистрироваться
    registration_page.click_register_button()
    time.sleep(2)
    # Вводим заведомо верный код
    base = MainPage(driver)
    base.fill_confirmation_code(
        "123456")
    # Проверка успешной регистрации
    time.sleep(2)
    if "https://start.rt.ru/?tab=main" in driver.current_url:
        print("Регистрация прошла успешно!")
    else:
        print("Регистрация не удалась.")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 2: Регистрация с неполными данными
def test_registration_with_incomplete_data():
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_register_link()
    time.sleep(2)
    # Оставляем поле фамилия и e-mail пустыми
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("Эрик", "", "", "12345678Qq", "12345678Qq")
    # Нажимаем кнопку Зарегистрироваться
    registration_page.click_register_button()
    # Добавим задержку для ожидания ошибки
    time.sleep(2)
    # Проверка наличия сообщения об ошибке
    error_messages = main_page.get_error_messages(RegistrationPageLocators.ERROR_MESSAGES)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить регистрацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 3: Неверный формат ввода имени
def test_incorrect_name_input():
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_register_link()
    time.sleep(2)
    # Оставляем поле фамилия и e-mail пустыми
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("Erik", "Кроу", "erik.krou@example.com", "12345678Qq", "12345678Qq")
    # Нажимаем кнопку Зарегистрироваться
    registration_page.click_register_button()
    # Добавим задержку для ожидания ошибки
    time.sleep(2)
    # Проверка наличия сообщения об ошибке
    error_messages = main_page.get_error_messages(RegistrationPageLocators.ERROR_MESSAGES)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить регистрацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 4: Неверный формат ввода email
def test_incorrect_email_input():
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_register_link()
    time.sleep(2)
    # Заполняем поле email неверным форматом
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("Эрик", "Кроу", "эрик.кроу@example.com", "12345678Qq", "12345678Qq")
    # Нажимаем кнопку Зарегистрироваться
    registration_page.click_register_button()
    # Добавим задержку для ожидания ошибки
    time.sleep(2)
    # Проверка наличия сообщения об ошибке
    error_messages = main_page.get_error_messages(RegistrationPageLocators.ERROR_MESSAGES)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить регистрацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 5: Неверное значения подтверждения пароля
def test_incorrect_confirm_password_input():
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_register_link()
    time.sleep(2)
    # Заполняем поля с неверным подтверждением пароля
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("Эрик", "Кроу", "erik.krou@example.com", "12345678Qq", "22345678Qq")
    # Нажимаем на кнопку для открытия списка городов
    registration_page.click_city_dropdown_button()
    # Добавляем задержку для открытия списка
    time.sleep(1)
    # Прокручиваем список до города Саратовская обл
    registration_page.scroll_to_city("Саратовская обл")
    # Выбираем город из списка
    registration_page.select_city("Саратовская обл")
    # Нажимаем кнопку Зарегистрироваться
    registration_page.click_register_button()
    time.sleep(2)
    # Проверка наличия сообщения об ошибке
    error_messages = main_page.get_error_messages(RegistrationPageLocators.ERROR_MESSAGES)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить регистрацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 6: Проверка уникальности email
def test_check_email_uniqueness():
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_register_link()
    time.sleep(2)
    # Заполняем поля верными данными с уже зарегистрированным e-mail
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("Эрик", "Кроу", "erik.krou@example.com", "12345678Qq", "12345678Qq")
    # Нажимаем на кнопку для открытия списка городов
    registration_page.click_city_dropdown_button()
    # Добавляем задержку для открытия списка
    time.sleep(1)
    # Прокручиваем список до города Саратовская обл
    registration_page.scroll_to_city("Саратовская обл")
    # Выбираем город из списка
    registration_page.select_city("Саратовская обл")
    # Нажимаем кнопку Зарегистрироваться
    registration_page.click_register_button()
    time.sleep(2)
    # Проверка наличия сообщения об ошибке
    error_messages = main_page.get_error_messages(RegistrationPageLocators.ALREADY_REGISTERED_EMAIL_MESSAGE)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить регистрацию")
    # Закрытие браузера
    driver.quit()
