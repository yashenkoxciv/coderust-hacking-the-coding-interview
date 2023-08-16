
def binary_search_v2(nums, target) -> int:
    idx = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) // 2)

        mid_value = nums[mid]
        if mid_value == target:
            idx = mid
            break

        if mid_value > target:
            high = mid - 1
        else:
            low = mid + 1
    return idx
