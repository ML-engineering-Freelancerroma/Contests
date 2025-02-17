# В школе перед Новым Годом устраивают игру в Тайного Санту. Каждому ученику i выдается ученик ai, которому он должен подарить подарок.
# Костя, как администратор игры, определил каждому школьнику свое число ai. Но потом его коллега Маша спросила: А правда ли, что если начать цепочку подарков от школьника 1 к школьнику a1, потом aa1 и так далее, то цепочка замкнется на школьнике 1, после того, как задействует всех остальных учеников ровно по одному разу?
# Костя не знает, правда это или нет, но он собирается изменить ровно одно число ai, чтобы получить конфигурацию, которая устроит Машу. Помогите ему с этим.

# Формат входных данных
# В первой строке находится натуральное число n — количество школьников (2<=n<=10^5). В следующей строке находится n натуральных чисел ai — ученик, который достался Тайному Санте с номером i(1<=ai<=n).

# Формат выходных данных
# В первой строке выведите два числа (1<=x,y<=n, x!=y) — номер ученика x, которому нужно изменить число ax, и новое значение ax.
# Должно выполняться условие ax!=y. Если ответов несколько — выведите любой.
# Если сделать это невозможно — выведите << -1 -1 >>

# Замечание
# В первом примере хотя бы один школьник будет дарить подарок сам себе.
# Во втором примере после изменения происходят передачи подарков 1->2->3->1.

# Пример1:
# Ввод:
# 3
# 1 2 3
# Вывод:
# -1 -1

# Пример2:
# Ввод:
# 3
# 1 3 1
# Вывод:
# 1 2


def can_make_valid_graph(nums):
    graph = {}
    pair_val = 0
    vals = set()

    for idx, val in enumerate(nums, start=1):
        graph[idx] = val
        if val in vals:
            if pair_val == 0:
                pair_val = val
            else:
                return -1, -1
        else:
            vals.add(val)
    if len(vals) + 1 != len(nums):
        return -1, -1
    if pair_val == 0:
        return -1, -1

    excepted_val = 0
    for i in range(len(nums)):
        if (i+1) not in vals:
            excepted_val = i + 1
            break

    idxs_of_pair_vals = []
    for idx, val in enumerate(nums):
        if val == pair_val:
            idxs_of_pair_vals.append(idx+1)

    done_cells = set()
    next_val = graph[excepted_val]
    while next_val not in done_cells:
        done_cells.add(next_val)
        prev_val = next_val
        next_val = graph[next_val]
    if len(done_cells) == len(nums) - 1:
        return prev_val, excepted_val
    return -1, -1


input()
nums = list(map(int, input().split()))
print(*can_make_valid_graph(nums))
