import pytest
from dsa.arrays.smallest_common_number_from_arrays import smallest_common_number_from_arrays


examples = [
    ([6, 7, 10, 25, 30, 63, 64],    [0, 4, 5, 6, 7, 8, 50],     [1, 6, 10, 14],     6),
    ([6, 7, 10, 25],                [0, 4, 5, 6],               [1, 6, 10, 14],     6),
]

test_cases = [
    *examples
]


@pytest.mark.parametrize('nums0,nums1,nums2,expected_n', test_cases)
def test_smallest_common_number_from_arrays(nums0, nums1, nums2, expected_n):
    c = smallest_common_number_from_arrays(nums0, nums1, nums2)

    assert c == expected_n

