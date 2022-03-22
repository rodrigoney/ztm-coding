# Write a function that reverses a string

def reverse_string(my_string):
    string_reversed = []
    for i in range(len(my_string) - 1, -1, -1):
        string_reversed.append(my_string[i])
    return ''.join(string_reversed)


print(reverse_string('I am rodrigo'))
# Time complexity O(n)
# Space complexity O(n)

# Pythonic
print('I am rodrigo'[::-1])
