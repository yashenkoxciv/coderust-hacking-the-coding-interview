
def reverse_array(nums, start, end):
    while start < end:
        # oneliner: nums[start], nums[end] = nums[end], nums[start]
        t = nums[start]
        nums[start] = nums[end]
        nums[end] = t

        start += 1
        end -= 1


def rotate_array_by_n(nums, n):
    length = len(nums)
    n = n % length
    if n < 0:  # means left rotations
        '''
        Example of the right rotation:
        n = 1
        [1, 2, 3, 4] -> [4, 1, 2, 3]

        Example of the left rotation:
        n = -1
        [1, 2, 3, 4] -> [2, 3, 4, 1]
        therefore, this is the same as 3 right rotations (n + length_of_nums[4])
        '''
        n += length
    print(n)
    # [1, 2, 3, 4]
    nums = nums[::-1]
    # [4, 3, 2, 1]
    print(nums)
    reverse_array(nums, 0, n - 1)
    print(nums)
    reverse_array(nums, n, length - 1)
    print(nums)
    print('*'*4)


def rotate_array_by_n_v2(nums, n):  # not tested
    l = len(nums)
    n = n % l
    n = n + l if n < 0 else n
    nums = nums[::-1]
    nums[0:n] = nums[n-1:-l-1:-1] 
    nums[n:l] = nums[l:n-1:-1]
    return nums


def rotate_array_by_n_v3(nums, n):
    l = len(nums)
    n = n % l
    return nums[-n:l] + nums[0:-n]


'''
** Example 1:
Given:
    nums = [1, 2, 3, 4]
    n = 2
    expected: [3, 4, 1, 2]

Solution:
    0. l = len(nums)
    1. convert to right rotations
        do not need to do
        n = 2
    2. do rotations
        n is the middle of array where we have to do rotations
        so: [1, 2, 3, 4] splits to [1, 2] + [3, 4]
        [3, 4] is the part of the answer, but it should be the first part
        [1, 2] is also the part of the answer
        a = nums[n:l] + nums[0:n]

** Example 2:
Given:
    nums = [1, 2, 3, 4]
    n = -2
    expected: [3, 4, 1, 2]

Solution:
    0. l = len(nums)
    1. convert to right rotations
        n = n % l
        n = -2 % 4 => 2
    then the same as fo Example 1

** Example 3:
Given:
    nums = [1, 2, 3, 4, 5]
    n = -3
    expected: [4, 5, 1, 2, 3]

Solution:
    0. l = len(nums)
    1. convert to right rotations
        n = n % l
        n = -3 % 5 => 2 (two right rotations)
    2. do rotations
        n = 2
        nums[-n:l] + nums[0:-n]

                 v
        [1, 2, 3, 4, 5]

        




'''



if __name__ == '__main__':
    rotate_array_by_n([1, 2, 3, 4], 1)
    rotate_array_by_n([1, 2, 3, 4], -1)

        

