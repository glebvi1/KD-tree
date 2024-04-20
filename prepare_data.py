from typing import List
from Point import Point

import matplotlib.pyplot as plt


def parse_file(filename="data.txt") -> List[Point]:
    """Парсим filename и возвращаем список координат"""
    coords = []

    with open(filename) as f:
        for line in f.readlines():
            coords.append(Point(*map(float, line.rstrip().split())))

    return coords


def plot_of_point(coords: List[Point], point) -> None:
    """Визуализируем данные точки и искомую точку"""
    plt.title("Точки")

    plt.scatter([p.x for p in coords], [p.y for p in coords], label="Данные точки")
    plt.scatter(point.x, point.y, label="Искомая точка")

    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
