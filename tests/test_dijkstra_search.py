import pytest

from PathPlanning.VoronoiRoadMap.dijkstra_search import DijkstraSearch


def test_search_returns_empty_path_when_goal_is_unreachable():
    planner = DijkstraSearch(show_animation=False)
    node_x = [0.0, 1.0, 2.0]
    node_y = [0.0, 0.0, 0.0]
    edge_ids = [[1], [], []]

    assert planner.search(0.0, 0.0, 2.0, 0.0, node_x, node_y, edge_ids) == ([], [])
