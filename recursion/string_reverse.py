def reverse_string(s):
    if len(s) == 1:
        return s[-1]
    return s[-1] + reverse_string(s[:-1])

print(reverse_string('yoyo mastery'))  # Should return: 'yretsam oyoy'
