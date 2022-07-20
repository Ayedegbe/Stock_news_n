temperature = [10, -20, -289,100]
def celcius_farenheit(degree):
    farenheit = degree * 9 / 5 + 32
    return farenheit
for f in temperature:
    if celcius_farenheit(f) < -273.15:
        print('Matter can not exist')
    elif celcius_farenheit(f) == 273.15:
        print('Matter will seize to exist soon')
    else:
        print('The temperature in Farenheit is ' + str((celcius_farenheit(f))))

