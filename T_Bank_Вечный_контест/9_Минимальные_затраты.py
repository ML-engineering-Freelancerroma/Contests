# Даня в обеденный перерыв ходит в одно и то же кафе. Ему, как сотруднику банка, положено специальное предложение: при каждой покупке больше, чем на 100 рублей, Даня получает купон на бесплатный обед.
# Даня узнал стоимость своих обедов на ближайшие n дней. Ему хочется минимизировать свои затраты, грамотно используя талоны. Требуется найти минимальные суммарные затраты Дани на обеды.

# Формат входных данных:
# В первой строке дается натуральное число n(0<=n<=100). В каждой из n строк записана стоимость обеда в каждой из дней (неотрицательное целое число, не больше, чем 300).

# Формат выходных данных:
# В первой строке выдайте минимально возможную суммарную стоимость обедов.

# Замечание:
# В первом примере Дане придется купить первые 3 обеда, после чего у него появится талон. Этот талон будет выгоднее всего потратить на последний обед. Таким образом, он купит первые 4 обеда и получит пятый бесплатный.

# Пример 1:
# Ввод:
# 5
# 35
# 40
# 101
# 59
# 63
# Вывод:
# 235


def min_lunch_cost(dinner_costs):
    n = len(dinner_costs)
    dp = [[float('inf')] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + dinner_costs[i - 1])

            if dinner_costs[i - 1] > 100:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + dinner_costs[i - 1])

            if j >= 1:
                dp[i][j - 1] = min(dp[i][j - 1], dp[i - 1][j])

    return min(dp[n])


n = int(input())
dinner_costs = [int(input()) for _ in range(n)]
print(min_lunch_cost(dinner_costs))
