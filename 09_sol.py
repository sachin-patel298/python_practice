year = 2024

if (year % 400 == 0)or(year % 4 == 0 and year % 100 != 0):
    print(year,"Year Is A Leap Year")
else:
    print(year,"Is Not Leap Year")