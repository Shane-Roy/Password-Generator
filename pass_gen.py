import random

# This program takes a user input for password length and then returns a random password including numbers and symbols
# No duplicate chars are used in the password output

strings = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){}[]\/<>~`-=?,."
passwordlength = int(input("Enter desired password length: "))
output = "".join(random.sample(strings, passwordlength))
print(output)
