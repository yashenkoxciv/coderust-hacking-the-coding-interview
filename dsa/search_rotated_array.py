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


def search_rotated_array_recursive(nums, low, high, target):
    if low > high:
        return -1
    
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid
    
    if nums[low] <= nums[mid]:
        if nums[low] <= target < nums[mid]:
            return search_rotated_array_recursive(nums, low, mid - 1, target)
        else:
            return search_rotated_array_recursive(nums, mid + 1, high, target)
    else:
        if nums[mid] < target <= nums[high]:
            return search_rotated_array_recursive(nums, mid + 1, high, target)
        else:
            return search_rotated_array_recursive(nums, low, mid - 1, target)


def search_rotated_array_recursive_client(nums, target):
    return search_rotated_array_recursive(nums, 0, len(nums) - 1, target)

