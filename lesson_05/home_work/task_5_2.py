# Дано число. Найти сумму и произведение его цифр.


try:
    num = int(input(
        'Enter nunber, please:'
    ))
except:
    print('Error input data')

str_num = str(num)

# sum
if str_num[0] == '-':
    str_num = str_num[1:]

size = len(str_num)

i = 0
sum = 0
while i < size:
    sum += int(str_num[i])
    i += 1

print(f'sum = {sum}')

# mult
if str_num[0] == '-':
    str_num = str_num[1:]

size = len(str_num)

i = 0
mult = 1
while i < size:
    mult *= int(str_num[i])
    i += 1

print(f'mult = {mult}')

