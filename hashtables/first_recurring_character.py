# Return the first recurring character
# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# should return 1

def find_recur(arr):  # O(n)
    key_map = {}
    for i in range(0, len(arr)):
        if key_map.get(arr[i], None) is None:
            key_map[arr[i]] = 1
        else:
            return arr[i]
    return None


assert find_recur([2, 5, 1, 2, 3, 5, 1, 2, 4]) == 2
assert find_recur([2, 1, 1, 2, 3, 5, 1, 2, 4]) == 1
