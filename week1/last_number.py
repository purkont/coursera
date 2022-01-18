number = int(input())
amount = 0
count = 0
while count != 3:
    amount += number % 10
    number //= 10
    count += 1
print(amount)
