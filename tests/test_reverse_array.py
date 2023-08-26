import pytest
from dsa.rotate_array_by_n import reverse_array


# def generate_test_cases(nums):
#     test_cases = []
#     for i in range(len(nums)):
#         test_case = (nums, nums[i], i)
#         test_cases.append(test_case)
#     return test_cases


examples = [
    ([1, 2, 3], 0, 2, [3, 2, 1]),
    ([1, 2, 3], 0, 1, [2, 1, 3]),
    ([], 0, 0, [])
]

test_cases = [
    *examples
]


@pytest.mark.parametrize('nums,start,end,expected_nums', test_cases)
def test_binary_search(nums, start, end, expected_nums):
    reverse_array(nums, start, end)

    assert nums == expected_nums

