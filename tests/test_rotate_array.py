import pytest
from dsa.arrays.rotate_array_by_n import rotate_array_by_n_v3


examples = [
    ([-1, -100, 3, 99], 2,                          [3, 99, -1, -100]),
    ([1, 2, 3, 4, 5], 2,                            [4, 5, 1, 2, 3]),
    ([1, 2, 3, 4, 5, 6, 7], 3,                      [5, 6, 7, 1, 2, 3, 4]),
    ([1, 10, 20, 0, 59, 86, 32, 11, 9, 40], -3,     [0, 59, 86, 32, 11, 9, 40, 1, 10, 20]),
    ([1, 2], 1,                                     [2, 1]),
    ([0, 1, 2, 3, 4], 2,                            [3, 4, 0, 1, 2]),
    ([0, 1, 2, 3, 4], -2,                           [2, 3, 4, 0, 1]),
]

test_cases = [
    *examples
]


@pytest.mark.parametrize('nums,n,expected_nums', test_cases)
def test_binary_search(nums, n, expected_nums):
    rotated_nums = rotate_array_by_n_v3(nums, n)

    assert rotated_nums == expected_nums

