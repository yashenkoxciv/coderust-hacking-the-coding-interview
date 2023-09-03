import pytest
from dsa.search_low_high_index import (
    naive_search_low_high_target_index,
    search_low_target_index,
    search_high_target_index,
    search_low_high_target_index
)


examples = [
    ([1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20],     5,      2,      10),
    ([1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20],     2,      1,      1),
    (
        [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9],
        5, 15, 17
    ),
    (
        [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9],
        2, 3, 7
    ),
    (
        [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9],
        8, -1, -1
    ),
    (
        [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9],
        9, 24, 24
    ),
    (
        [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 9],
        4, 11, 14
    )
]

test_cases = [
    *examples
]


@pytest.mark.parametrize('nums,target,expected_low,expected_high', test_cases)
def test_naive_search_low_high_target_index(nums, target, expected_low, expected_high):
    low, high = naive_search_low_high_target_index(nums, target)

    assert low == expected_low
    assert high == expected_high


@pytest.mark.parametrize('nums,target,expected_low,expected_high', test_cases)
def test_search_low_target_index(nums, target, expected_low, expected_high):
    low = search_low_target_index(nums, target)

    assert low == expected_low


@pytest.mark.parametrize('nums,target,expected_low,expected_high', test_cases)
def test_search_high_target_index(nums, target, expected_low, expected_high):
    high = search_high_target_index(nums, target)

    assert high == expected_high


@pytest.mark.parametrize('nums,target,expected_low,expected_high', test_cases)
def test_search_low_high_target_index(nums, target, expected_low, expected_high):
    low, high = search_low_high_target_index(nums, target)

    assert high == expected_high
    assert low == expected_low

