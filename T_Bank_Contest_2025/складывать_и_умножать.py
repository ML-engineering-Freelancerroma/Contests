# Согласно законам неизвестного государства Т каждый совершеннолетний гражданин должен уметь складывать и умножать числа.
# Дан массив a1, a2, ..., an. Для каждого р от 1 до к рассмотрим следующий процесс:
# 1) для всех і, j таких, что 1 <= i < j <= n выпишем пары (аi, аj);
# 2) в полученной последовательности каждую пару заменим на сумму ее элементов;
# 3) в очередной последовательности каждый элемент возведем в р-ю степень;
# 4) сложим все числа итоговой последовательности;
# 5) заменим значение на его остаток при делении на 998244353
# Обозначим результат за f(p). Найдите значения f(1), f(2)..... f(k).

# Формат входных данных
# Первая строка содержит числа n (2 <= n <= 2 * 10^5) и k (1<=300).
# Вторая строка содержит числа a1, a2,...an, (1 <= ai <= 10^8).

# Формат выходных данных
# Выведите f(1), f(2),..., f(k), каждое в новой строке.


MOD = 998244353


def add(a, b):
    """Сложение по модулю"""
    a += b
    if a >= MOD:
        a -= MOD
    return a


def sub(a, b):
    """Вычитание по модулю"""
    a -= b
    if a < 0:
        a += MOD
    return a


def mod(a, b):
    """Умножение по модулю"""
    return (a * b) % MOD


def bin_coeff(max_k):
    """Вычисление биномиальных коэффициентов до max_k"""
    binom = [[0] * (i + 1) for i in range(max_k + 1)]
    for i in range(max_k + 1):
        binom[i][0] = binom[i][i] = 1
        for j in range(1, i):
            binom[i][j] = add(binom[i-1][j-1], binom[i-1][j])
    return binom


def result():
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().strip().split())

    a = list(map(int, input().strip().split()))

    S = [0] * (k + 1)
    S[0] = n % MOD
    for x in a:
        current_power = 1
        for t in range(1, k + 1):
            current_power = mod(current_power, x)
            S[t] = add(S[t], current_power)

    binom = bin_coeff(k)

    two = [1] * (k + 1)
    for p in range(1, k + 1):
        two[p] = mod(two[p-1], 2)
    inv2 = 499122177

    results = []
    for p in range(1, k + 1):
        firstPart = 0
        for r in range(p + 1):
            term = mod(binom[p][r], S[r])
            term = mod(term, S[p-r])
            firstPart = add(firstPart, term)
        firstPart = mod(firstPart, inv2)
        secondPart = mod(two[p-1], S[p])
        res = sub(firstPart, secondPart)
        results.append(res)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')


if __name__ == "__main__":
    result()
