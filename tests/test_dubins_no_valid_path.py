"""Tests for PathPlanning/DubinsPath/dubins_path_planner behaviour when no
path type produces a feasible configuration.

Before the fix, ``_dubins_path_planning_from_origin`` would silently leave
``b_mode = None`` and pass that (plus ``[None, None, None]`` as ``lengths``)
into ``_generate_local_course``, which then crashed with::

    TypeError: 'NoneType' object is not iterable

inside ``zip(modes, lengths)``. The new code raises a clear ``ValueError``
before that happens, with a message that distinguishes between "you asked
for no path types at all" and "the path types you asked for all failed".
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest


_HERE = pathlib.Path(__file__).resolve().parent
_PLANNER_PATH = (
    _HERE.parent / "PathPlanning" / "DubinsPath" / "dubins_path_planner.py"
)


def _load_planner():
    spec = importlib.util.spec_from_file_location(
        "dubins_path_planner_under_test", _PLANNER_PATH
    )
    mod = importlib.util.module_from_spec(spec)
    # The planner file does ``from utils.angle import ...`` so make sure the
    # repo root is on sys.path before executing it.
    repo_root = str(_HERE.parent)
    added = repo_root not in sys.path
    if added:
        sys.path.insert(0, repo_root)
    try:
        spec.loader.exec_module(mod)
    finally:
        if added:
            sys.path.remove(repo_root)
    return mod


@pytest.fixture
def planner():
    return _load_planner()


def test_empty_selected_types_raises_clear_value_error(planner):
    """Passing an empty selected_types list means no planner ran, so the
    error message should explain that explicitly rather than claim all six
    path types failed.
    """
    with pytest.raises(ValueError) as excinfo:
        planner.plan_dubins_path(
            0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, selected_types=[]
        )
    msg = str(excinfo.value)
    assert "No valid Dubins path found" in msg
    assert "empty" in msg or "no path planners" in msg


def test_selected_types_all_feasible_returns_path(planner):
    """Sanity check: when the selected types actually have a feasible
    configuration, the planner should return a path instead of raising.
    """
    px, py, pyaw, modes, lengths = planner.plan_dubins_path(
        0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, selected_types=["LSL"]
    )
    assert len(px) > 0
    assert len(px) == len(py) == len(pyaw)
    assert modes == ["L", "S", "L"]
    assert all(l is not None for l in lengths)