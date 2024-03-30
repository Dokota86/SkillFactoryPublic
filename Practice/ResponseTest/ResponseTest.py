from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Открываем браузер
driver = webdriver.Chrome()

# Максимальное время ожидания элементов на странице
driver.implicitly_wait(10)

# Открываем сайт
driver.get("https://shopiland.ru/")

# Находим поле ввода для поиска
search_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/div/div[1]/div/input')

# Вводим запрос "смартфон" в поле поиска
search_input.send_keys("смартфон")

# Находим кнопку поиска и выполняем поиск
search_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/div/div[1]/button')
search_button.click()

try:
    # Ждем ответ от маркетплейсов
    WebDriverWait(driver, 20).until_not(EC.presence_of_element_located((By.CLASS_NAME, "MuiBox-root.css-zmhted")))
    print("Ответ от маркетплейсов получен успешно.")
except TimeoutException:
    print("Не удалось получить ответ от маркетплейсов за 20 секунд.")

# Закрываем браузер
driver.quit()