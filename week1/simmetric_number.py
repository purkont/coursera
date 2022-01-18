number = int(input())
first = number // 100
second = number % 100
first = str(first)
second = str(second)
if len(first) < 2:
    first = '0' + first
if len(second) < 2:
    second = '0' + second
if first == second[::-1]:
    print(1)
else:
    print(0)
