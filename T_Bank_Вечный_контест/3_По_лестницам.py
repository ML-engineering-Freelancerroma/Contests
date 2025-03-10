# У Кати насыщенный день на работе. Ей надо передать n разных договоров коллегам. Все встречи происходят на разных этажах, а между этажами можно перемещаться только по лестничным пролетам — считается, что это улучшает физическую форму сотрудников. Прохождение каждого пролета занимает ровно 1 минуту.
# Сейчас Катя на парковочном этаже, планирует свой маршрут. Коллег можно посетить в любом порядке, но один из них покинет офис через t минут. С парковочного этажа лестницы нет — только лифт, на котором можно подняться на любой этаж.
# В итоге план Кати следующий:

# Подняться на лифте на произвольный этаж. Считается, что лифт поднимается на любой этаж за 0 минут.
# Передать всем коллегам договоры, перемещаясь между этажами по лестнице. Считается, что договоры на этаже передаются мгновенно.
# В первые t минут передать договор тому коллеге, который планирует уйти.
# Пройти минимальное количество лестничных пролетов.
# Помогите Кате выполнить все пункты ее плана.

# Формат входных данных:
# В первой строке вводятся целые положительные числа n и t (2<=n, t<=100) — количество сотрудников и время, когда один из сотрудников покинет офис (в минутах). В следующей строке n чисел — номера этажей, на которых находятся сотрудники. Все числа различны и по абсолютной величине не превосходят 100. Номера этажей даны в порядке возрастания. В следующей строке записан номер сотрудника, который уйдет через t минут.

# Формат выходных данных:
# Выведите одно число — минимально возможное число лестничных пролетов, которое понадобится пройти Кате.

# Замечание:
# В первом примере времени достаточно, чтобы Катя поднялась по этажам по порядку.
# Во втором примере Кате понадобится подняться к уходящему сотруднику, а потом пройти всех остальных — например, в порядке {1, 2, 3, 4, 6}

# Пример 1
# Ввод:
# 5 5
# 1 4 9 16 25
# 2
# Вывод:
# 24

# Пример 2
# Ввод:
# 6 4
# 1 2 3 6 8 25
# 5
# Вывод:
# 31


n, t = map(int, input().split())
floors = list(map(int, input().split()))
leave_index = int(input()) - 1

final_floor = floors[leave_index]
min_floor = floors[0]
max_floor = floors[-1]

if final_floor - min_floor <= t or max_floor - final_floor <= t:
    print(max_floor - min_floor)
else:
    path1 = (final_floor - min_floor) + (max_floor - min_floor)
    path2 = (max_floor - final_floor) + (max_floor - min_floor)
    print(min(path1, path2))
