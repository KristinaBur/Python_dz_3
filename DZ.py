# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
my_list = [random.randint(1,100) for _ in range(30)]
print (my_list)

x = int (input ('Введите число: '))
count = 0
for i in my_list:
    if i == x:
        count += 1
print(count)

