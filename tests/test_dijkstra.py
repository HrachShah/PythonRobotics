import conftest
from PathPlanning.Dijkstra import dijkstra as m


def test_1():
    m.show_animation = False
    m.main()


def test_verify_node_rejects_upper_bounds():
    planner = m.DijkstraPlanner([0, 4], [0, 4], 1.0, 0.0)
    assert not planner.verify_node(planner.Node(planner.x_width, 0, 0.0, -1))
    assert not planner.verify_node(planner.Node(0, planner.y_width, 0.0, -1))


if __name__ == '__main__':
    conftest.run_this_test(__file__)
