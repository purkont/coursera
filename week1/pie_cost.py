rub, kop, pie_number = int(input()), int(input()), int(input())
rub *= 100
pie_cost = (rub + kop) * pie_number
print(pie_cost // 100, pie_cost % 100)
