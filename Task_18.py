# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import math

n = int(input("Введите N: "))

list = list()

for i in range(n):
    if (i == n - 1):
        list.append(int(input("Введите X: ")))
    else:
        list.append(int(input()))
print(list)

min = math.fabs(list[0] - list[-1])
min_index = 0
listn = []

for j in range(1, n-1):
    if (math.fabs(list[j] - list[-1]) == min):
        listn.append(list[j])
    elif (math.fabs(list[j] - list[-1]) < min):
        min = math.fabs(list[j] - list[-1])
        min_index = j

listn.append(list[min_index])

print(f"Близкий(-ие) по величине элемент(ы): {listn}")