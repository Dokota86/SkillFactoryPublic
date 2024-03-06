from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Жужа', animal_type='Бигль',
                                     age='1', pet_photo='images/dog.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Белла", "кошка", "3", "images/cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Лора', animal_type='Кот', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список своих питомцев не пустой, пробуем обновить информацию
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем, что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # Если список питомцев пуст, выводим сообщение об этом
        print("There are no pets to update")

def test_empty_email_password_get_api_key():
    """Тест на передачу пустого email и пароля при получении ключа API"""
    status, result = pf.get_api_key('', '')
    assert status == 403


def test_empty_filter_get_list_of_pets():
    """Тест на передачу пустого значения параметра при запросе списка питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter='')
    assert status == 200


def test_too_large_animal_type_add_new_pet():
    """Тест на передачу слишком большого значения в параметре "animal_type" при добавлении питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, 'Fluffy', 'VeryVeryVeryVeryVeryVeryLongAnimalType',
                                    '3', 'images/cat1.jpg')
    assert status == 400

def test_missing_required_fields_add_new_pet():
    """Тест на передачу недостающих обязательных полей при добавлении питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, '', '', '', 'images/cat1.jpg')
    assert status == 400


def test_invalid_photo_format_add_new_pet():
    """Тест на передачу неверного формата фотографии при добавлении питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, 'Fluffy', 'Cat', '3', 'images/cat2.pdf')
    assert status == 400


def test_invalid_auth_key_get_list_of_pets():
    """Тест на передачу неверного ключа авторизации при запросе списка питомцев"""
    invalid_auth_key = {'key': 'invalid_key'}
    status, result = pf.get_list_of_pets(invalid_auth_key, filter='')
    assert status == 403

def test_delete_nonexistent_pet():
    """Тест на удаление питомца с несуществующим ID"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.delete_pet(auth_key, 'nonexistent_id')
    assert status != 200

def test_update_nonexistent_pet_info():
    """Тест на обновление информации о питомце с несуществующим ID"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_pet_info(auth_key, 'nonexistent_id', 'Fluffy', 'Cat', 5)
    assert status == 400


def test_invalid_age_add_new_pet():
    """Тест на передачу неверного типа данных в параметре "age" при добавлении питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, 'Fluffy', 'Cat', 'not_a_number', 'images/cat.jpg')
    assert status == 400


def test_invalid_photo_format_set_pet_photo():
    """Тест на передачу некорректного формата фотографии при установке фотографии питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.set_pet_photo(auth_key, 'pet_id', 'images/cat2.pdf')
    assert status != 200
