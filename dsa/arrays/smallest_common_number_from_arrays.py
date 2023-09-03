

def smallest_common_number_from_arrays(arr1, arr2, arr3):
    c = -1
    n0, n1, n2 = len(arr1) - 1, len(arr2) - 1, len(arr3) - 1
    i0, i1, i2 = 0, 0, 0
    while (i0 <= n0 and i1 <= n1 and i2 <= n2):
        if arr1[i0] == arr2[i1] == arr3[i2]:
            c = arr1[i0]
            break
        
        if arr1[i0] <= arr2[i1] and arr1[i0] <= arr3[i2]:
            i0 += 1
        elif arr2[i1] <= arr1[i0] and arr2[i1] <= arr3[i2]:
            i1 += 1
        elif arr3[i2] <= arr1[i0] and arr3[i2] <= arr2[i1]:
            i2 += 1
    
    return c

