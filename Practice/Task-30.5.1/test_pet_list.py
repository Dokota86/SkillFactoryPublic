import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver):
    # Вводим email
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    email_input.send_keys('VadimTest@mail.ru')
    # Вводим пароль
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    password_input.send_keys('VadimTest')
    # Нажимаем на кнопку входа в аккаунт
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    login_button.click()
    # Проверяем, что мы оказались на главной странице пользователя
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "PetFriends"))

@pytest.fixture(scope="module")
def pet_list(driver, login):
    # Переходим на страницу со списком питомцев пользователя
    driver.get('https://petfriends.skillfactory.ru/my_pets')

def test_pet_count(driver, login, pet_list):
    # Находим элемент с информацией о количестве питомцев
    pets_info_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]')))
    # Получаем текст из элемента
    pets_info_text = pets_info_element.text

    # Извлекаем число питомцев из текста с помощью регулярного выражения
    pets_count_match = re.search(r'Питомцев:\s*(\d+)', pets_info_text)
    pets_count = int(pets_count_match.group(1)) if pets_count_match else 0

    # Теперь pets_count содержит число питомцев, которое можно использовать в проверке.
    print("Количество питомцев:", pets_count)

def test_half_pets_with_images(driver, login, pet_list):
    # Получаем таблицу со списком питомцев
    pet_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table')))

    # Создаем список для информации о питомцах с фотографиями
    pets_with_images = []

    # Собираем информацию о каждом питомце с фотографиями
    for row in pet_table.find_elements(By.TAG_NAME, 'tr')[1:]:
        pet_image_src = row.find_element(By.XPATH, './th/img').get_attribute('src')

        # Проверяем, что атрибут src не пустой и не равен None
        if pet_image_src and pet_image_src != 'None':
            pets_with_images.append(True)

    # Вычисляем количество питомцев с фотографиями
    num_pets_with_images = len(pets_with_images)

    # Выводим информацию о количестве питомцев с фотографиями
    print(f"Питомцев с фотографией: {num_pets_with_images}")

    # Проверяем, что хотя бы у половины питомцев есть фотографии
    assert num_pets_with_images >= len(pet_table.find_elements(By.TAG_NAME, 'tr')[1:]) / 2

def test_pet_info(driver, login, pet_list):
    # Получаем таблицу со списком питомцев
    pet_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table')))
    # Создаем список для информации о питомцах
    pet_info_list = []
    # Собираем информацию о каждом питомце
    for row in pet_table.find_elements(By.TAG_NAME, 'tr')[1:]:
        pet_name = row.find_element(By.XPATH, './td[1]').text
        pet_breed = row.find_element(By.XPATH, './td[2]').text
        pet_age = row.find_element(By.XPATH, './td[3]').text
        pet_info = (pet_name, pet_breed, pet_age)
        pet_info_list.append(pet_info)
    # Проверяем, что у всех питомцев есть имя, порода и возраст
    for pet_info in pet_info_list:
        assert all(pet_info)

def test_pet_names_unique(driver, login, pet_list):
    # Получаем таблицу со списком питомцев
    pet_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table')))
    # Создаем список для имен питомцев
    pet_names = []
    # Собираем информацию о каждом питомце
    for row in pet_table.find_elements(By.TAG_NAME, 'tr')[1:]:
        pet_name = row.find_element(By.XPATH, './td[1]').text
        pet_names.append(pet_name)
    # Проверяем, что у всех питомцев разные имена
    assert len(pet_names) == len(set(pet_names))

def test_no_duplicate_pets(driver, login, pet_list):
    # Получаем таблицу со списком питомцев
    pet_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table')))
    # Создаем множество для уникальных питомцев и множество для дубликатов
    unique_pets = set()
    duplicate_pets = set()
    # Собираем информацию о каждом питомце
    for row in pet_table.find_elements(By.TAG_NAME, 'tr')[1:]:
        pet_name = row.find_element(By.XPATH, './td[1]').text
        pet_breed = row.find_element(By.XPATH, './td[2]').text
        pet_age = row.find_element(By.XPATH, './td[3]').text
        pet_info = (pet_name, pet_breed, pet_age)
        if pet_info in unique_pets:
            duplicate_pets.add(pet_info)
        else:
            unique_pets.add(pet_info)
    # Проверяем, что в списке нет повторяющихся питомцев
    assert len(duplicate_pets) == 0