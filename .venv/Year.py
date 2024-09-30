year = 2024

if year % 400 == 0:
    print("год високосный")
elif year % 100 == 0:
    print("год не високосный")
elif year % 4 == 0:
    print("год високосный")
else:
    print("Год не високосный")
