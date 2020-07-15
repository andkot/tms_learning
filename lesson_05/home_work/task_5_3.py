# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.

def is_prime(x: int) -> bool:
    """
    :param x: integer unsigned value
    :return: True if x is prime and false when x isn't prime and < 2.
    """
    if x < 2:
        return False

    right = int(x ** 0.5)
    print(right)
    i = 2

    while i <= right:
        if x % i == 0:
            return False
        i += 1

    return True


def factorize(x: int) -> list:
    """

    :param x: integer unsigned value
    :return: list of primes which x is factorized or None when x isn't unsigned integer value
    """

    if x < 2:
        return [x]

    result = []

    right = int(x ** 0.5)
    i = 2

    while i <= int(x ** 0.5):
        while x % i == 0:
            result.append(i)
            x /= i
        i += 1

    if x != 1:
        result.append(int(x))

    return result


def sum_dividers(x: int) -> int:
    factorize_list = factorize(x)

    matrix = []

    mat_length = len(factorize_list)
    mat_height = int(2 ** len(factorize_list))

    for i in range(mat_length):
        tmp = []
        h = 0
        p = 0
        x = int(mat_height / (2 ** (1 + i)))

        for j in range(mat_height):
            if x > h:
                tmp.append(p)
            else:
                h = 0
                if p == 0:
                    p = 1
                else:
                    p = 0
                tmp.append(p)
            h += 1

        matrix.append(tmp)

    check_list = []
    for i in range(len(matrix[0]) - 1):
        x = 1
        for j in range(len(matrix)):
            if matrix[j][i] != 0:
                x *= matrix[j][i] * factorize_list[j]
            if x not in check_list:
                check_list.append(x)
    return sum(check_list)


def find_couple(left: int, right: int) -> list:
    """
    :param left:
    :param right:
    :return:
    """
    factorize_sum = {}
    for i in range(left, right + 1):
        factorize_sum[i] = sum_dividers(i)

    couple = []

    for i in range(left, right + 1):
        for key, value in factorize_sum.items():
            if i != key and i == value and factorize_sum[i] == key:
                couple.append(str(i) + ' - ' + str(key))

    return couple


a = find_couple(200, 1210)
print(a)
