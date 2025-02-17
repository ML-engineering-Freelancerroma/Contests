# Во время разработки некоторой задачи Саша решил сгенерировать несколько новых тестов. Каждый тест Саши должен представлять собой натуральное число, не меньшее l и не большее r. Кроме того, натуральное число в тесте обязательно должно состоять из одинаковых цифр.
# Например, число 999 подходит под это требование, а число 123 — нет. Какое максимальное число различных тестов сможет создать Саша?

# Формат входных данных 
# В единственной строке вводятся два натуральных числа l, r (1<=l,r<=10^18) — ограничения на тесты Саши.
# Обратите внимания, что эти числа не вместятся в 32-битный тип данных, используйте 64-битный при необходимости

# Формат выходных данных
# Выведите одно число — количество тестов, которое может сделать Саша.

# Замечание
# В первом тесте Саше подходят номера [4, 5, 6, 7].
# Во втором тесте подходят все числа, кратные 11, от 11 до 99.

# Пример 1:
# Ввод:
# 4 7
# Вывод:
# 4

# Пример 2:
# Ввод:
# 10 100
# Вывод:
# 9

def count_same_digit_numbers(x, y):
    count = 0
    for digit in range(1, 10):
        num = digit
        while num <= y:
            if num >= x:
                count += 1
            num = num * 10 + digit
    return count


l, r = map(int, input().split())

result = count_same_digit_numbers(l, r)
print(result)
