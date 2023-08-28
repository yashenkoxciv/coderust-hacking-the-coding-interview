def search_rotated_array(nums, target):
    # modifications of binary search
    idx = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] == target:
            idx = mid
            break

        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return idx
