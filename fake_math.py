def divide(first, second):
    if second == 0:
        return 'Ошибка'  # Возвращаем строку 'Ошибка', если второй параметр равен 0
    else:
        return first / second  # Возвращаем результат деления


result_1 = divide(10, 2)
print(result_1)

result_2 = divide(10, 0)
print(result_2)