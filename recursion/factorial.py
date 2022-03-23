
def find_factorical_recursive(number):  # O(n)
    if number == 1:
        return 1
    return number * find_factorical_recursive(number - 1)


def find_factorical_iterative(number):  # O(n)
    res = number
    next = number - 1
    while next != 0:
        res = res * next
        next -= 1
    return res


print(find_factorical_recursive(2))
print(find_factorical_recursive(3))
print(find_factorical_recursive(10))
print(find_factorical_iterative(2))
print(find_factorical_iterative(3))
print(find_factorical_iterative(10))
