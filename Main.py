from random import choice
from random import shuffle

lowerchars = "abcdefghijklmnopqrstuvwxyz"
upperchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
specialchars = "~!@#$%^&*"

combine_chars = list(lowerchars + upperchars + nums + specialchars)
shuffle(combine_chars)

password_length = int(input("Enter Password Length : "))

password = ""
for i in range(password_length):
    password += choice(combine_chars)

print("Generated Password : " + password)