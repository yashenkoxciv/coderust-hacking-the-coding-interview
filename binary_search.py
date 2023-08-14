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


if __name__ == '__main__':
    r = binary_search([1, 3, 9, 10, 12], 9)
    print(r)

    r = binary_search([1, 3, 9, 10, 12], 1)
    print(r)

    r = binary_search([1, 3, 9, 10, 12], 12)
    print(r)

    print('*'*12)

    # r = binary_search_recursive([1, 3, 9, 10, 12], 9)
    # print(r)

    # r = binary_search_recursive([1, 3, 9, 10, 12], 1)
    # print(r)

    r = binary_search_recursive([1, 3, 9, 10, 12], 12)
    print(r)

    # r = binary_search([1, 2, 3, 4, 5], 2)
    # print(r)

    # r = binary_search([1, 2, 4, 5], 1)
    # print(r)


