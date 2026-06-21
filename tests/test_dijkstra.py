import conftest
from PathPlanning.Dijkstra import dijkstra as m


def test_1():
    m.show_animation = False
    m.main()


def test_unreachable_goal_does_not_crash():
    # When the goal is fully enclosed by obstacles, the open set drains
    # before the goal is reached. planning() must return gracefully
    # (one final-path point at the goal) rather than raising
    # `ValueError: min() iterable argument is empty` from the inner
    # `min(open_set, ...)` call inside the search loop.
    m.show_animation = False
    ox, oy = [], []
    # Outer wall
    for i in range(-10, 60):
        ox.append(float(i))
        oy.append(-10.0)
    for i in range(-10, 60):
        ox.append(60.0)
        oy.append(float(i))
    for i in range(-10, 61):
        ox.append(float(i))
        oy.append(60.0)
    for i in range(-10, 61):
        ox.append(-10.0)
        oy.append(float(i))
    # Box around the goal (50, 50) so it is unreachable
    for i in range(45, 56):
        ox.append(float(i))
        oy.append(45.0)
    for i in range(45, 56):
        ox.append(float(i))
        oy.append(55.0)
    for i in range(45, 56):
        ox.append(45.0)
        oy.append(float(i))
    for i in range(45, 56):
        ox.append(55.0)
        oy.append(float(i))

    planner = m.DijkstraPlanner(ox, oy, 2.0, 1.0)
    rx, ry = planner.planning(-5.0, -5.0, 50.0, 50.0)
    # The fix makes this return gracefully; the path collapses to the
    # goal's grid position because no node in the open set matched.
    assert isinstance(rx, list) and isinstance(ry, list)
    assert len(rx) == len(ry)
    assert len(rx) >= 1


if __name__ == '__main__':
    conftest.run_this_test(__file__)
