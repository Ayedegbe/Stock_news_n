def celcius_farenheit(degree):
    farenheit = degree*9/5 + 32
    return farenheit
degree =float(input("Enter temperature of specified matter:"))
if celcius_farenheit(degree)> -273.15:
    print(celcius_farenheit(degree))
else:
    print(celcius_farenheit(degree))
    print("Matter does not exist")




