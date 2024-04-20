from prepare_data import parse_file, plot_of_point
from Point import Point
from KD_tree import KDTree

if __name__ == "__main__":
    P = Point(0, 0)

    coords = parse_file()
    plot_of_point(coords, P)
    kd_tree = KDTree(coords)

    print(kd_tree.search_nearest_point(P))
