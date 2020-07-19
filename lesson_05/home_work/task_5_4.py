# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.


def sum_garmonic(n: int) -> float:
    s = 0
    for i in range(1, n + 1):
        s += 1 / i
    return s


print(sum_garmonic(3))
