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


def test_planning_returns_empty_path_when_goal_is_unreachable():
    planner = m.DijkstraPlanner([0, 2], [0, 2], 1.0, 0.0)
    planner.obstacle_map[1][1] = True
    rx, ry = planner.planning(0.0, 0.0, 1.0, 1.0)
    assert rx == []
    assert ry == []
