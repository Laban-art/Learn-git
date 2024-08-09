unit = unit("is this temperature in celcius or fahrenheit (C/F): ")
temp = float(input("enter the temperature. "))

if unit == "C":
    pass
elif unit == "F":
    pass
else:
    print(f"{unit}is an invalid unit of measurement")
    