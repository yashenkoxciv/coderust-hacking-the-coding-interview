import sys
sys.path.insert(0, './')  # to import dsa
from dsa.search_rotated_array import search_rotated_array_recursive_client


if __name__ == '__main__':
    nums, target, expected_idx = [6, 7, 1, 2, 3, 4, 5],     3,      4
    
    idx = search_rotated_array_recursive_client(nums, target)

    print(expected_idx, idx)

