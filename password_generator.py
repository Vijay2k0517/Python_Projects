import random
import string

length = int(input("Enter the lenth of the password:"))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = "".join([random.choice(chars) for i in range(length)])

print ("Your password is:", password)
