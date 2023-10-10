import random
import numpy as np

#Сгенерировать массив случайных чисел размером 1024 в пределах [-1000:1000]
array = []
for i in range(1024):
    array.append(random.randrange(-1000, 1000))

#Сортировка массива
array.sort()

print("Массив случайных чисел", array)
print('Число значений в массиве:', len(array))

#Удаление отрицательных чисел из массива
for y in range(i):
    if min(array) < 0:
        array.pop(0)
print("Массив без отрицательных чисел", array)
print('Число значений в массиве:', len(array))
