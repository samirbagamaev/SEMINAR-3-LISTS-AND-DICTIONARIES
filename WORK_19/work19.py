# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_1 = [1, 2, 3, 4, 5, 6, 7]
K = int(input('Введите на какое количество чисел  сдвинуть последовательность '))

list_1 = list_1[-K:] + list_1[:-K]
print(list_1)
