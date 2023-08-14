def binary_search(nums, target):
    '''
    nums: sorted (asc) list of integers
    '''
    target_idx = -1

    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) // 2)

        if nums[mid] == target:
            target_idx = mid
            break
        
        if nums[mid] > target:
            high = mid - 1
        
        if nums[mid] < target:
            low = mid + 1

    return target_idx


def binary_search_rec(nums, target, low, high):
    if low > high:
        return -1
    
    mid = low + ((high - low) // 2)

    if nums[mid] == target:
        return mid
    
    if nums[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
    
    return binary_search_rec(nums, target, low, high)


def binary_search_recursive(nums, target):
    return binary_search_rec(nums, target, 0, len(nums) - 1)

