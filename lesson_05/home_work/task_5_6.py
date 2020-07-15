# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают (каждое следующее число
# больше предыдущего).

def counter(input_list):
    tmp = input_list[0]

    for i in range(len(input_list)):
        tmp = input_list[i]
        j = i + 1

        if i < len(input_list) - 1:
            while j < len(input_list):
                if tmp < input_list[j]:
                    pass
