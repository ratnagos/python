hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hours < 40:
    pay = hours * rate
elif hours > 40 and hours < 60:
    pay = (40 * rate) + (hours - 40) * rate * 1.5
else:
    pay = 60 * rate + (hours - 60) * (rate * 1.5)
print("Pay:", pay)