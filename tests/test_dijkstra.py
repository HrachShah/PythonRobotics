import conftest
from PathPlanning.Dijkstra import dijkstra as m


def test_1():
    m.show_animation = False
    m.main()


if __name__ == '__main__':
    conftest.run_this_test(__file__)

def test_no_path_returns_empty_route():
    m.show_animation = False
    ox, oy = [], []
    for i in range(6):
        ox.extend((float(i), float(i)))
        oy.extend((0.0, 5.0))
    for i in range(1, 5):
        ox.extend((0.0, 5.0))
        oy.extend((float(i), float(i)))
    for i in range(6):
        ox.append(3.0)
        oy.append(float(i))

    planner = m.DijkstraPlanner(ox, oy, 1.0, 0.4)
    rx, ry = planner.planning(1.0, 1.0, 4.0, 4.0)

    assert rx == []
    assert ry == []

