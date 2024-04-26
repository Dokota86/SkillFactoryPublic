import time
from selenium import webdriver
from pages.base import MainPage
from pages.recovery_page import RecoveryPage
from utilities.locators import RecoveryPageLocators


# Тест-кейс 15: Восстановление пароля по телефону
def test_phone_recovery():
    # Открытие страницы восстановления пароля
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_recovery_link()
    time.sleep(2)
    # Переходим на страницу восстановления по телефону
    recovery_page = RecoveryPage(driver)
    recovery_page.click_phone_tab()
    # Заполняем поле Мобильный телефон верными данными
    recovery_page.enter_username("9876543210")
    # Заполняем поле Капчи неверными данными
    recovery_page.enter_captcha("123456")
    # Нажимаем кнопку Продолжить
    recovery_page.click_reset_button()
    time.sleep(2)
    # Проверка отображения сообщения об ошибке
    error_messages = main_page.get_error_messages(RecoveryPageLocators.ERROR_MESSAGE)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить авторизацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 16: Восстановление пароля по почте
def test_email_recovery():
    # Открытие страницы восстановления пароля
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_recovery_link()
    time.sleep(2)
    # Переходим на страницу восстановления по почте
    recovery_page = RecoveryPage(driver)
    recovery_page.click_email_tab()
    # Заполняем поле Электронная почта верными данными
    recovery_page.enter_username("erik.krou@example.com")
    # Заполняем поле Капчи неверными данными
    recovery_page.enter_captcha("123456")
    # Нажимаем кнопку Продолжить
    recovery_page.click_reset_button()
    time.sleep(2)
    # Проверка отображения сообщения об ошибке
    error_messages = main_page.get_error_messages(RecoveryPageLocators.ERROR_MESSAGE)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить авторизацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 17: Восстановление пароля по логину
def test_login_recovery():
    # Открытие страницы восстановления пароля
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_recovery_link()
    time.sleep(2)
    # Переходим на страницу восстановления по логину
    recovery_page = RecoveryPage(driver)
    recovery_page.click_login_tab()
    # Заполняем поле Логин верными данными
    recovery_page.enter_username("erik.krou")
    # Заполняем поле Капчи неверными данными
    recovery_page.enter_captcha("123456")
    # Нажимаем кнопку Продолжить
    recovery_page.click_reset_button()
    time.sleep(2)
    # Проверка отображения сообщения об ошибке
    error_messages = main_page.get_error_messages(RecoveryPageLocators.ERROR_MESSAGE)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить авторизацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 18: Восстановление пароля по лицевому счету
def test_ls_recovery():
    # Открытие страницы восстановления пароля
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_recovery_link()
    time.sleep(2)
    # Переходим на страницу восстановления по логину
    recovery_page = RecoveryPage(driver)
    recovery_page.click_ls_tab()
    # Заполняем поле Логин верными данными
    recovery_page.enter_username("rtkid_1111111111111")
    # Заполняем поле Капчи неверными данными
    recovery_page.enter_captcha("123456")
    # Нажимаем кнопку Продолжить
    recovery_page.click_reset_button()
    time.sleep(2)
    # Проверка отображения сообщения об ошибке
    error_messages = main_page.get_error_messages(RecoveryPageLocators.ERROR_MESSAGE)
    if error_messages:
        print("Обнаружены следующие ошибки:")
        for message in error_messages:
            print(f"- {message}")
    else:
        print("Ошибка: Не удалось завершить авторизацию")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 19: Открытие окна помощи
def test_faq():
    # Открытие страницы восстановления пароля
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_recovery_link()
    time.sleep(2)
    # Нажимаем кнопку Помощь
    recovery_page = RecoveryPage(driver)
    recovery_page.click_faq_button()
    time.sleep(2)
    # Проверка, что окно помощи открылось
    faq_window = recovery_page.find_faq_open()
    if faq_window.is_displayed():
        print("Окно помощи успешно открыто")
    else:
        print("Ошибка: Окно помощи не открылось")
    # Закрытие браузера
    driver.quit()


# Тест-кейс 20: Проверка работоспособности кнопки "Вернуться назад"
def test_back_button():
    # Открытие страницы восстановления пароля
    driver = webdriver.Chrome()
    driver.get("https://start.rt.ru/")
    main_page = MainPage(driver)
    main_page.click_recovery_link()
    time.sleep(2)
    # Запомните текущий URL
    initial_url = driver.current_url
    # Найдите кнопку возврата назад и нажмите на нее
    recovery_page = RecoveryPage(driver)
    recovery_page.click_back_button()
    time.sleep(2)
    # Запрос подтверждения, что произошло возвращение назад
    if initial_url == driver.current_url:
        print("Кнопка возврата назад не работает")
    else:
        print("Кнопка возврата назад работает")
    # Закрыть браузер
    driver.quit()
