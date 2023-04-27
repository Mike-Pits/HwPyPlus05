objects = [1, 3, None, "", 0, -2, 5, []]
def test_filter():
    assert list(filter(None, objects)) == [1, 3, -2, 5]

nrs = [2, 3, 4]
def test_map():
    assert list(map(lambda n: n*n, nrs)) == [4, 9, 16]

nrs_unsorted = [2, 1, 5, 7, 3, 4, 9, 8, 6, 0]
def test_sorted():
    assert sorted(nrs_unsorted) == [0,1,2,3,4,5,6,7,8,9]

import math

def test_math_pi():
    assert round(math.pi, 2) == 3.14

def test_math_sqrt():
    assert math.sqrt(144) == 12

def test_math_pow():
    assert math.pow(12, 2) == 144

def test_math_hypot():
    assert math.hypot(3, 4) == 5