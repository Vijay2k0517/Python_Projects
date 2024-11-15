def celsiusToFahrenheit(celsius):
    return(celsius * 9/5) + 32

def farenheitToCelsius(fahrenheit):
    return (fahrenheit - 32)* 5/9

print("Temprature Converter")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahernheit to Celsius")

while True:

    x=input("Enter Choice 1/2")

    if x == '1':
        celsius = float(input("Enter temperature in Celsius:"))
        print("Temperature in Fahrenheit:", celsiusToFahrenheit(celsius))

    elif x == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit"))
        print("Temperature in Celsius:",farenheitToCelsius(fahrenheit))

    else:
        print("Invalid input")

    repeatCalculation = input('Do you want to repeat the calculation? (Y/N): ').strip().upper()

    if repeatCalculation == 'N':
        break
