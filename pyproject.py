print('Welcome to the simple calculator')
print('Enter 2 numbers')

num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))

print('Select operation!')
print('1: Addition')
print('2: Subtraction')
print('3: Multiplication')
print('4: Division')

while True:
    x = int(input('Enter the operation (1-4): '))

    if x == 1:
        print("You've selected addition")
        numA = num1 + num2
        print('Result:', numA)

    elif x == 2:
        print("You've selected subtraction")
        numS = num1 - num2
        print('Result:', numS)

    elif x == 3:
        print("You've selected multiplication")
        numM = num1 * num2
        print('Result:', numM)

    elif x == 4:
        if num2 == 0:
            print("You can't divide by 0")
        else:
            print("You've selected division")
            numD = num1 / num2
            print('Result:', numD)

    else:
        print("Invalid operation choice. Please enter a number between 1 and 4.")
        continue

    repeatCalculation = input('Do you want to repeat the calculation? (Y/N): ').strip().upper()
    if repeatCalculation == 'N':
        break
