x = int(input())
y = int(input())
kolkv = y - x + 1
kolpd = y // (y - x + 1)
if y == (kolkv * kolpd):
    print('YES')
else:
    print('NO')
