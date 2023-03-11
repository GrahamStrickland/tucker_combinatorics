# Tests for find_euler_cycle.py
from nose.tools import assert_equal
from typing import List
from ..find_euler_cycle import find_euler_cycle

def test_find_euler_cycle0():
    V = [1,2]
    E = [(1,2), (2,1)]
    obs = find_euler_cycle(V, E)
    assert_equal(is_euler_cycle(obs, V, E), True)

def test_find_euler_cycle1():
    V = [1,2,3]
    E = [(1,2), (2,3)]
    obs = find_euler_cycle(V, E)
    assert_equal(is_euler_cycle(obs, V, E), False)

def test_find_euler_cycle2():
    V = ['A','B','C','D']
    E = [('A','B'),('B','A'),('A','C'),('B','C'),
            ('B','D'),('D','B'),('C','D')]
    obs = find_euler_cycle(V, E)
    assert_equal(is_euler_cycle(obs, V, E), False)

def test_find_euler_cycle3():
    V = ['A','B','C','D']
    E = [('A','B'),('A','C'),('B','D'),('C','D')]
    obs = find_euler_cycle(V, E)
    assert_equal(is_euler_cycle(obs, V, E), True)

def is_euler_cycle(path: List[int], V: List[int], E: List[tuple[int]]) -> bool:
    # Test for missing vertex in path
    for vert in V:
        if vert not in path:
            return False

    # Test for correctness of cycle
    for i in range(len(path)-1):
        edge = (path[i], path[i+1])

        if edge in E:
            E.remove(edge)
        elif edge[::-1] in E:
            E.remove(edge[::-1])

    return not E
