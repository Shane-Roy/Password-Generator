import random
import string


class Pass:
    """This class evaluates the necessary characters to make up
    the password generator"""

    def __init__(self, upper, lower, special, numbers):
        self.upper = upper
        self.lower = lower
        self.special = special
        self.numbers = numbers


password = Pass("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "!@#$%^&*(){}[]\/<>~`-=?,.", "0123456789")
print("")
length = int(input("Enter a password length: "))  # First pass user input length for password
pass_data = password.lower + password.upper + password.numbers + password.special  # Grouping all the password data in 1
result_str = ''.join(random.choice(pass_data) for i in range(length))  # Randomization function, including length input
print("Random string of length", length, "is:")  # OUTPUT the password
print(result_str)
print("")
second_length = int(input("Enter a second password length (to add to the first): "))  # Second round
s_result_str = ''.join(random.choice(pass_data) for i in range(second_length)) + result_str  # Joining length 1 and 2
example_length = length + second_length  # Showing the length of passwords 1 and 2 AKA used for an "example"
print("Random string of length", example_length, "is:")  # OUTPUT the second password
print(s_result_str)
print("")
t_length = length * second_length  # Multiplying the lengths to make an even longer password
print("""
-------------------------------
|For additional encryption use|
-------------------------------
""")
print("Random strings of length", t_length, "is:")
for i in range(4):
    t_result_str = ''.join(random.choice(s_result_str) for i in range(t_length))
    print("")
    print(t_result_str)
