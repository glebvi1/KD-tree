from Point import Point
from KD_tree import KDTree

import matplotlib.pyplot as plt

import time
import random

N = [100, 500, 1000, 2000, 4000, 6000, 8000, 10000, 100000]
K = 100
building_time = []
search_time = []

for n in N:
    coords = [Point(random.uniform(-10**6, 10**6), random.uniform(-10**6, 10**6)) for _ in range(n)]

    start = time.time()
    kd_tree = KDTree(coords)
    building_time.append(time.time() - start)

    start = time.time()
    times = 0
    for _ in range(K):
        kd_tree.search_nearest_point(Point(random.uniform(-10**6, 10**6), random.uniform(-10**6, 10**6)))
        times += time.time() - start
    search_time.append(times / K)

print(building_time)
print(search_time)

plt.title("Время работы")

plt.plot(N, building_time, label="Время постройки дерева")
plt.plot(N, search_time, label=f"Среднее арифметическое время поиска {K} точек")

plt.legend()
plt.xlabel("Количество точек на плоскости")
plt.ylabel("Время (секунды)")

plt.savefig("Время работы.jpg")
plt.show()


