def check_range(numbers):
    for i in range(len(numbers)):
        if numbers[i] < 1 or numbers[i] > 100:
            return False
    return True
    
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

def sort_list(lst):
    return sorted(lst)

input_sequence = input("Введите последовательность чисел через пробел: ")
try:
    numbers = [int(num) for num in input_sequence.split()]
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите последовательность чисел.")
    exit()

if not check_range(numbers):
        print("Некоторые числа не соответствуют условию")
        exit()

user_number = input("Введите любое число: ")
try:
    user_number = int(user_number)
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите число.")
    exit()

sorted_numbers = sort_list(numbers)
position = binary_search(sorted_numbers, user_number, 0, len(sorted_numbers) - 1)

print("Отсортированная последовательность:", sorted_numbers)

if position is not False:
    print(f"Номер позиции элемента, который меньше {user_number}, "
          f"а следующий за ним больше или равен этому числу: {position}")
else:
    print(f"Введенное число {user_number} не найдено в последовательности.")