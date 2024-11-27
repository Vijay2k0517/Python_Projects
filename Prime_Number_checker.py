import math

def is_prime():
    while True:
        try:
            num = int(input("Enter a number: "))

            if num <= 1:
                print("It is not a prime number!")
            else:
                is_prime_flag = True
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        is_prime_flag = False
                        break

                if is_prime_flag:
                    print(f"{num} is a prime number!")
                else:
                    print(f"{num} is not a prime number!")

        except ValueError:
            print("Invalid input! Please enter an integer.")

        repeat = input("Do you want to repeat? (y/n): ").lower()
        if repeat == "n":
            print("Goodbye!")
            break

is_prime()
