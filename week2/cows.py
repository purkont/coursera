n = int(input())
if n % 10 == 1 and n != 11:
    print(n, "korova")
elif 10 <= n <= 20 or n % 10 == 0 or 5 <= n % 10 <= 9:
    print(n, "korov")
else:
    print(n, "korovy")
