import pytest
from dsa.arrays.move_all_zeros_to_the_beginning import (
    naive_move_all_zeros_to_the_beginning,
    move_all_zeros_to_the_beginning
)


examples = [
    ([1, 10, 20, 0, 59, 63, 0, 88, 0],      [0, 0, 0, 1, 10, 20, 59, 63, 88]),
    ([1, 0, 2, 3, 0],                       [0, 0, 1, 2, 3]),
    ([0],                                   [0]),
    ([-1, 0, 0, -2, 9],                     [0, 0, -1, -2, 9]),
    ([1, 2, 3, 4, 5],                       [1, 2, 3, 4, 5]),
    ([2],                                   [2]),
]

test_cases = [
    *examples
]


@pytest.mark.parametrize('nums,expected_nums', test_cases)
def test_naive_move_all_zeros_to_the_beginning(nums, expected_nums):
    nums_example = nums.copy()
    naive_move_all_zeros_to_the_beginning(nums_example)

    assert nums_example == expected_nums


@pytest.mark.parametrize('nums,expected_nums', test_cases)
def test_move_all_zeros_to_the_beginning(nums, expected_nums):
    nums_example = nums.copy()
    move_all_zeros_to_the_beginning(nums_example)

    assert nums_example == expected_nums


