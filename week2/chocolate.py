n, m, k = int(input()), int(input()), int(input())
if n * m - m >= k and k % m == 0:
    print('YES')
elif n * m - n >= k and k % n == 0:
    print('YES')
else:
    print('NO')
