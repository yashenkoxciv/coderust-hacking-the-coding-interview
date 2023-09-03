def naive_move_all_zeros_to_the_beginning(nums):
    # it actually operates on lists
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            nums.pop(i)
            nums.insert(0, 0)


def move_all_zeros_to_the_beginning(nums):
    n = len(nums) - 1
    read_idx = n
    write_idx = n
    while read_idx >= 0:
        if nums[read_idx] != 0:
            nums[write_idx] = nums[read_idx]
            write_idx -= 1
        read_idx -= 1
    
    while write_idx >= 0:
        nums[write_idx] = 0
        write_idx -= 1


if __name__ == '__main__':
    nums = [1, 10, 20, 0, 59, 63, 0, 88, 0]
    move_all_zeros_to_the_beginning(nums)
        


