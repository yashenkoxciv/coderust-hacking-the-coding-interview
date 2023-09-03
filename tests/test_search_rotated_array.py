import pytest
from dsa.arrays.search_rotated_array import search_rotated_array, search_rotated_array_recursive_client


examples = [
    ([6, 7, 1, 2, 3, 4, 5],     3,      4),
    ([6, 7, 1, 2, 3, 4, 5],     6,      0),
    ([4, 5, 6, 1, 2, 3],        3,      5),
    ([4, 5, 6, 1, 2, 3],        6,      2),
    ([4, 5, 6, 1, 2, 3],        0,     -1),
]

test_cases = [
    *examples
]


@pytest.mark.parametrize('nums,target,expected_idx', test_cases)
def test_search_rotated_array(nums, target, expected_idx):
    target_idx = search_rotated_array(nums, target)

    assert target_idx == expected_idx


@pytest.mark.parametrize('nums,target,expected_idx', test_cases)
def test_search_rotated_array_recursive(nums, target, expected_idx):
    target_idx = search_rotated_array_recursive_client(nums, target)

    assert target_idx == expected_idx

