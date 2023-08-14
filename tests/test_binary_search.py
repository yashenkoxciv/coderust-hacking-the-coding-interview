import pytest
from dsa.binary_search import binary_search, binary_search_recursive


def generate_test_cases(nums):
    test_cases = []
    for i in range(len(nums)):
        test_case = (nums, nums[i], i)
        test_cases.append(test_case)
    return test_cases


coderust_cases = generate_test_cases([1, 3, 9, 10, 12])
coderust_cases_v2 = [
    ([], 12, -1),
    ([0, 1], 1, 1),
    ([1, 2, 3], 3, 2),
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1)
]
even_len_cases = generate_test_cases([0, 3, 5, 8])

test_cases = [
    *coderust_cases,
    *even_len_cases,
    *coderust_cases_v2
]


@pytest.mark.parametrize('nums,target,expected_idx', test_cases)
def test_binary_search(nums, target, expected_idx):
    result_idx = binary_search(nums, target)

    assert result_idx == expected_idx


@pytest.mark.parametrize('nums,target,expected_idx', test_cases)
def test_binary_search_recursive(nums, target, expected_idx):
    result_idx = binary_search_recursive(nums, target)

    assert result_idx == expected_idx
