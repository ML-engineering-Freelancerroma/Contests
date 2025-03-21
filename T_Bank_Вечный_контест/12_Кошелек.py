# У Артемия есть бесконечное число монет, каждая из которых одного из трех номиналов. Его интересует, какие суммы от 1 до N рублей он может набрать в свой кошелек, если там заранее лежала монета величиной в 1 рубль.

# Формат входных данных:
# Первая строка содержит число N — ограничение на сумарную стоимость монет в кошельке (1<=N<=10^18).
# Вторая строка содержит три числа A, B, C задающие достоинства типов монет (1<=A, B, C<=100000).

# Формат выходных данных:
# Выведите единственное число — количество сумм, которые можно набрать в кошельке.

# Замечание:
# В первом примере возможны следующие варианты:
# 1=1
# 1+4=5
# 1+7=8
# 1+4+4=9
# 1+9=10
# 1+4+7=12
# 1+4+4+4=13
# 1+4+9=14
# 1+7+7=15

# Пример 1:
# Ввод:
# 15
# 4 7 9
# Вывод:
# 9

# ЧАСТИЧНОЕ РЕШЕНИЕ

from collections import deque


def count_reachable_sums(N, A, B, C):
    coins = {A, B, C}
    reachable = set([1])
    queue = deque([1])

    while queue:
        current = queue.popleft()
        for coin in coins:
            new_sum = current + coin
            if new_sum <= N and new_sum not in reachable:
                reachable.add(new_sum)
                queue.append(new_sum)

    return len(reachable)


N = int(input())
A, B, C = map(int, input().split())
print(count_reachable_sums(N, A, B, C))
