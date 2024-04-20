from typing import List, Optional
from Point import Point


class KDTree:
    def __init__(self, coords: List[Point]):
        self.coords = coords
        self.k = 2
        self.tree = self.build_tree()

    def build_tree(self):
        """Строим дерево"""
        return self.__build(coords=self.coords, disc=0)

    def search_nearest_point(self, point: Point):
        """Ищем ближайшую точку к точке point"""
        return self.__search(root=self.tree, point=point, disc=0)

    def __search(self, root, point, disc) -> Optional[Point]:
        """Рекурсивная функция для поиска ближайшей точки
        :param root: текущее поддерево, в котором ищем ближайшую точку. В первом запуске - корень дерева
        :param point: Искомая точка
        :param disc: Значение дискриминатора на данном шаге рекурсии
        """

        if root is None:
            return None

        if point[disc] < root["point"][disc]:
            branch1 = root["left"]
            branch2 = root["right"]
        else:
            branch1 = root["right"]
            branch2 = root["left"]

        # Продолжаем поиск в следующей ветки
        # Ищем ближайшую между текущем узлом (root["point"]) и следующими точками
        # Когда дойдем до конца дерева, то point2=None и nearest = root["point"]
        nearest = point.nearest_point(
            root["point"],
            self.__search(branch1, point, self.__next_disc(disc))
        )

        # Рассматриваем ситуацию, где ближайшая точка может лежать в другом поддереве
        # Считаем расстояние между искомой точкой и ближайшей на данный момент
        r = point.distance(nearest)
        # Если окружность с центром в исходной точки point и радиусом r пересекает соседнюю ветку
        # То ищем ближайшую точку в соседней ветки и сравниваем с текущей ближайшей точкой
        if r > abs(point[disc] - root["point"][disc]):
            nearest = point.nearest_point(
                nearest,
                self.__search(branch2, point, self.__next_disc(disc))
            )

        return nearest

    def __build(self, coords, disc):
        """Рекурсивная функция для постройки дерева
        :param coords: Список точек
        :param disc: Значение дискриминатора на данном шаге рекурсии
        """

        n = len(coords)
        if n <= 0:
            return None

        sorted_points = sorted(coords, key=lambda coord: coord[disc])

        return {
            "left": self.__build(sorted_points[:n//2], self.__next_disc(disc)),
            "point": sorted_points[n // 2],
            "right": self.__build(sorted_points[(n//2 + 1):], self.__next_disc(disc))
        }

    def __next_disc(self, disc):
        """Функция вычисляет следующее значение дискриминатора"""
        return (disc + 1) % self.k
