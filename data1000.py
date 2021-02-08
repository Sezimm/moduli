import datetime

today = input("Vedite datu nachala(y-m-d): ")
c = today.split('-')
a = 1000

b = datetime.date(int(c[0]), int(c[1]), int(c[2]))
dayd = datetime.timedelta(days = a)
x = b + dayd
print(x)