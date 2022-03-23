
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    num = 1
    last = 1
    second_last = 0
    for i in range(2, n+1):
        num = last + second_last
        second_last = last
        last = num
    return num



print(fibonacci_recursive(0))
print(fibonacci_recursive(1))
print(fibonacci_recursive(2))
print(fibonacci_recursive(3))
print(fibonacci_recursive(10))
print('--------------')
print(fibonacci_iterative(0))
print(fibonacci_iterative(1))
print(fibonacci_iterative(2))
print(fibonacci_iterative(3))
print(fibonacci_iterative(10))