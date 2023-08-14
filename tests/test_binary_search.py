import pytest
from binary_search import binary_search, binary_search_recursive


def generate_test_cases(nums):
    test_cases = []
    for i in range(len(nums)):
        test_case = (nums, nums[i], i)
        test_cases.append(test_case)
    return test_cases


coderust_cases = generate_test_cases([1, 3, 9, 10, 12])
even_len_cases = generate_test_cases([0, 3, 5, 8])

test_cases = [
    *coderust_cases,
    *even_len_cases,
]


@pytest.mark.parametrize('nums,target,expected_idx', test_cases)
def test_binary_search(nums, target, expected_idx):
    result_idx = binary_search(nums, target)

    assert result_idx == expected_idx


@pytest.mark.parametrize('nums,target,expected_idx', test_cases)
def test_binary_search_recursive(nums, target, expected_idx):
    result_idx = binary_search_recursive(nums, target)

    assert result_idx == expected_idx
