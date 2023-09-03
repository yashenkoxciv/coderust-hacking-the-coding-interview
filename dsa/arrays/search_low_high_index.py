def naive_search_low_high_target_index(nums, target):
    low = -1
    high = -1
    for i, n in enumerate(nums):
        if (n == target) and (low == -1):
            low = i
        
        if (n == target) and (low != -1):
            high = i
    return low, high


def search_low_target_index(nums, target):
    target_low = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] >= target:
            high = mid - 1
        
        if nums[mid] < target:
            low = mid + 1
    
    if nums[low] == target:
        target_low = low
    return target_low


def search_high_target_index(nums, target):
    target_high = -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] > target:
            high = mid - 1
        
        if nums[mid] <= target:
            low = mid + 1
    
    if (low > high) and (nums[high] == target):
        target_high = high
    return target_high


def search_low_high_target_index(nums, target):
    low = search_low_target_index(nums, target)
    high = search_high_target_index(nums, target)
    return low, high


