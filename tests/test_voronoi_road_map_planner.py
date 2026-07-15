import conftest  # Add root path to sys.path
from PathPlanning.VisibilityRoadMap import visibility_road_map as m
from PathPlanning.VoronoiRoadMap.dijkstra_search import DijkstraSearch


def test1():
    m.show_animation = False
    m.main()


if __name__ == '__main__':
    conftest.run_this_test(__file__)


def test_dijkstra_returns_empty_route_when_goal_is_unreachable():
    planner = DijkstraSearch(show_animation=False)
    rx, ry = planner.search(0, 0, 2, 0, [0, 2], [0, 0], [[], []])

    assert rx == []
    assert ry == []
