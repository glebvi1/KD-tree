from Point import Point
from KD_tree import KDTree

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import math
import time
import random

N = [i for i in range(10000, 500000, 10000)]
K = 100
building_time = []
search_time = []
error_time = []

for n in N:
    coords = [Point(random.uniform(-n**3, n**3), random.uniform(-n**3, n**3)) for _ in range(n)]

    start = time.time()
    kd_tree = KDTree(coords)
    building_time.append(time.time() - start)

    error = []

    for i in range(K):
        start = time.time()
        kd_tree.search_nearest_point(Point(random.uniform(-n**3, n**3), random.uniform(-n**3, n**3)))
        finish = time.time()

        error.append(finish - start)

    mean = sum(error) / K
    search_time.append(mean)

    summ = 0
    for i in range(K):
        summ += (error[i] - mean)**2

    error_time.append(math.sqrt(summ / n))


N = np.array(N)
building_time = np.array(building_time)
search_time = np.array(search_time)

"""График для построения дерева"""
def func1(x, a, b, c):
    return a*x*np.log(x*b) + c


popt, pcov = curve_fit(func1, N, building_time)

plt.title("Время построения")
plt.scatter(N, building_time, c="green", marker="x", label="Время построения дерева")
a, b, c = round(popt[0], 6), round(popt[1], 4), round(popt[2], 4)
plt.plot(N, func1(N, *popt), c="blue", label=f"Аппроксимация функцией: {a}*x*ln({b}*x) + {c}")

plt.legend()
plt.xlabel("Количество точек на плоскости")
plt.ylabel("Время (секунды)")

plt.savefig("Время построения.jpg")
plt.show()

"""График для поиска по дереву"""
def func2(x, a, b, c):
    return a*np.log(x*b) + c


popt, pcov = curve_fit(func2, N, search_time)
print(popt)
a, b, c = round(popt[0], 6), round(popt[1], 4), round(popt[2], 6)

plt.title("Время поиска")

plt.errorbar(N, search_time, yerr=error_time, c="green", label=f"Среднее арифметическое время поиска {K} точек")
plt.plot(N, func2(N, *popt), c="blue", label=f"Аппроксимация функцией: {a}*ln({b}*x) + {c}")

plt.legend()
plt.xlabel("Количество точек на плоскости")
plt.ylabel("Время (секунды)")

plt.savefig("Время поиска.jpg")
plt.show()
