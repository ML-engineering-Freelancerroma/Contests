# Соня с Сашей купили торт в форме выпуклого многоугольника на n вершинах. Они хотят разделить этот торт на две равные части одним строго вертикальным разрезом. А, именно, линия разреза на торте должна быть параллельна координатной оси Oy.
# Найдите x-координату, вдоль которой надо сделать искомый разрез.

# Формат входных данных:
# В первой строке вводится число n(1<=n<=1000) — количество вершин многоугольника
# В следующих n строках записаны записаны координаты вершин торта-многоугольника в порядке обхода. Гарантируется, что координаты — целые числа, не превосходящие по модулю 10^3.

# Формат выходных данных:
# Выведите одно число — искомую x-координату. Ответ надо выводить с точностью не меньше 10^(-6).

# Замечание:
# Первый тест — это квадрат, разделенный на две равные части.

# Пример 1:
# Ввод:
# 4
# 0 0
# 0 2
# 2 2
# 2 0
# Вывод:
# 1.000000000


def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2


def area_left_of_x(vertices, x_mid):
    n = len(vertices)
    left_polygon = []
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        if x1 <= x_mid:
            left_polygon.append((x1, y1))
        if (x1 < x_mid < x2) or (x2 < x_mid < x1):
            t = (x_mid - x1) / (x2 - x1)
            y_cross = y1 + t * (y2 - y1)
            left_polygon.append((x_mid, y_cross))
    return polygon_area(left_polygon)


def find_cut_line(vertices, total_area):

    left = min(x for x, y in vertices)
    right = max(x for x, y in vertices)
    while right - left > 1e-7:
        mid = (left + right) / 2
        left_area = area_left_of_x(vertices, mid)
        if left_area < total_area / 2:
            left = mid
        else:
            right = mid
    return left


n = int(input())
vertices = [tuple(map(int, input().split())) for _ in range(n)]

total_area = polygon_area(vertices)

x_cut = find_cut_line(vertices, total_area)

print(f"{x_cut:.6f}")
