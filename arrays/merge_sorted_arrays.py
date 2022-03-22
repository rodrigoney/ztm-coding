# Merge 2 sorted arrays into one sorted array
# arr1 = [0,3,4,31] arr2=[4,6,30]
# result = [0,3,4,4,6,30,31]

def merge_sorted_arrays(arr1, arr2):
    result = []
    index1 = 0
    index2 = 0

    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <= arr2[index2]:
            result.append(arr1[index1])
            index1 += 1

        elif arr2[index2] < arr1[index1]:
            result.append(arr2[index2])
            index2 += 1

    return result + arr1[index1:] + arr2[index2:]


assert merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]) == [0, 3, 4, 4, 6, 30, 31]
assert merge_sorted_arrays([0, 3, 4, 31], []) == [0, 3, 4, 31]
assert merge_sorted_arrays([], [4, 6, 30]) == [4, 6, 30]
