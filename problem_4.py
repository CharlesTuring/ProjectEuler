def is_palindrome(n):
    n_str = str(n)
    for i in range(len(n_str)):
        if n_str[i] != n_str[len(n_str) - i - 1]:
            return False
    return True


res = 0
for a in range(999, 99, -1):
    if a % 11 == 0:
        for b in range(999, 99, -1):
            if a * b < res:
                break
            if is_palindrome(a * b):
                res = a * b
    else:
        for b in range(990, 99, -11):
            if (a * b) < res:
                break
            if is_palindrome(a * b):
                res = a * b
print(res)
