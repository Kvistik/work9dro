import matplotlib.pyplot as plt
import numpy as np

A = 1
w = np.pi * 2
f = 10/1000

# создание массива
t = np.arange(0, 1000, 1)
# синосуидальный закон
y_sin = A * np.sin(w*f*t)
y_cos = A * np.cos(w*f*t)

# вывод значений
plt.plot(t, y_cos, 'r')
plt.plot(t, y_sin, 'y')
plt.title('A * sin(w*f*t) yellow \n A * cos(w*f*t) red')
plt.xlabel('Время (t)')
plt.ylabel('Амплитуда (A)')
plt.show()