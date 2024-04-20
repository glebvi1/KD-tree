import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point) -> float:
        """Считаем евклидово расстояние между двумя точками"""
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        return None

    def __str__(self):
        return f"({self.x}, {self.y})"

    def nearest_point(self, point1, point2):
        if point1 is None:
            return point2
        if point2 is None:
            return point1

        if self.distance(point1) < self.distance(point2):
            return point1
        return point2
