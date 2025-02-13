# Герман немного устал. Вот бы кто-нибудь сделал за него домашнее задание...
# Задача, которую необходимо решить Герману, звучит следующим образом. Дана последовательность a1, a2, ... , an и числа x, y, z.
# Разрешается произвольное количество (в том числе ноль) раз выполнить следующую операцию: выбрать произвольное i (1<=i<=n) и увеличить ai на единицу.
# Необходимо, чтобы хотя бы один элемент из последовательности делился на x, хотя бы один элемент делился на y и хотя бы один элемент делился на z. Разрешается, чтобы для разных значений из набора (x, y, z) подходил один и тот же элемент из последовательности.
# Помогите Герману отдохнуть перед сессией и найдите минимальное количество операций, которое необходимо выполнить, чтобы условие стало выполнено.
# Формат входных данных
# Первая строка содержит числа n (1<=n<=2*10^5), x, y и z (1<=x,y,z<=10^6).
# Вторая строка содержит числа a1, a2, ... , an (1<=ai<=10^18).
# Формат выходных данных
# Выведите одно число — минимальное количество операций, которое надо выполнить, чтобы для каждого из чисел x, y, z был хотя бы один элемент в последовательности, кратный данному числу.
# Комментарий к примеру
# В примере можно дважды увеличить a4 и один раз увеличить a5. Тогда на 10 будет делиться a4, на 20 будет делиться a5, на 30 будет делиться a4.
# Примеры данных
# ввод:
# 6 10 20 30
# 8 17 5 28 39 13
# вывод:
# 3

import math


def solve():
    n, x, y, z = map(int, input().strip().split())

    a = list(map(int, input().strip().split()))

    def cost(a_i, m):
        r = a_i % m
        return 0 if r == 0 else m - r

    def lcm(a, b):
        return a // math.gcd(a, b) * b

    lcm_xy = lcm(x, y)
    lcm_xz = lcm(x, z)
    lcm_yz = lcm(y, z)
    lcm_xyz = lcm(lcm_xy, z)

    INF = 10**20
    mX = mY = mZ = INF
    mXY = mXZ = mYZ = INF
    mXYZ = INF

    for val in a:
        cX = cost(val, x)
        cY = cost(val, y)
        cZ = cost(val, z)
        cXY = cost(val, lcm_xy)
        cXZ = cost(val, lcm_xz)
        cYZ = cost(val, lcm_yz)
        cXYZ = cost(val, lcm_xyz)

        if cX < mX:
            mX = cX
        if cY < mY:
            mY = cY
        if cZ < mZ:
            mZ = cZ
        if cXY < mXY:
            mXY = cXY
        if cXZ < mXZ:
            mXZ = cXZ
        if cYZ < mYZ:
            mYZ = cYZ
        if cXYZ < mXYZ:
            mXYZ = cXYZ

    S1 = mXYZ
    S2 = min(mXY + mZ, mXYZ)
    S3 = min(mXZ + mY, mXYZ)
    S4 = min(mYZ + mX, mXYZ)
    S5 = mX + mY + mZ
    answer = min(S1, S2, S3, S4, S5)
    print(answer)


if __name__ == "__main__":
    solve()
