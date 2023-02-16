def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

m = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        n = i * j
        if is_palindrome(n) and n > m:
            print('%d * %d = %d' % (i, j, n))
            m = n
