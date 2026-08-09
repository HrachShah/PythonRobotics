import conftest
from PathPlanning.AStar import a_star as m


def test_1():
    m.show_animation = False
    m.main()


if __name__ == '__main__':
    conftest.run_this_test(__file__)


def test_planning_returns_empty_path_for_occupied_endpoints():
    m.show_animation = False
    planner = m.AStarPlanner([0, 2, 0, 2], [0, 0, 2, 2], 1.0, 0.0)

    rx, ry = planner.planning(0.0, 0.0, 1.0, 1.0)

    assert rx == []
    assert ry == []


def test_planning_returns_empty_path_when_goal_is_unreachable():
    m.show_animation = False
    planner = m.AStarPlanner([1, 1, 1, 3, 3, 3], [1, 2, 3, 1, 2, 3], 1.0, 0.0)

    rx, ry = planner.planning(2.0, 2.0, 0.0, 0.0)

    assert rx == []
    assert ry == []
