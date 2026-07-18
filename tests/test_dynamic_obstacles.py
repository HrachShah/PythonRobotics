import numpy as np

from PathPlanning.TimeBasedPathPlanning.GridWithDynamicObstacles import Grid, Position


def test_grid_copies_obstacle_avoid_points():
    avoid_points = [Position(1, 1)]
    first_grid = Grid(np.array([3, 3]), num_obstacles=0, obstacle_avoid_points=avoid_points)
    avoid_points.append(Position(2, 2))
    second_grid = Grid(np.array([3, 3]), num_obstacles=0)

    assert first_grid.obstacle_avoid_points == [Position(1, 1)]
    assert second_grid.obstacle_avoid_points == []
