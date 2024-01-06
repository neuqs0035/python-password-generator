from random import choice, shuffle

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "~!@#$%^&*"

print("\n\t\t\tRandom Password Generator\n")

letter_size = num_size = special_char_size = 0
password_length = 0

letter_confirm = input("Do you want to add letters? (y/n): ")

if letter_confirm.lower() == "y":
    letter_size = int(input("Enter the count of letters: "))
    if letter_size > 0:
        password_length += letter_size
    else:
        print("\nLetter size cannot be zero.")

num_confirm = input("\nDo you want to add numbers? (y/n): ")

if num_confirm.lower() == "y":
    num_size = int(input("Enter the count of numbers: "))
    if num_size > 0:
        password_length += num_size
    else:
        print("\nNumber size cannot be zero.")

special_char_confirm = input("\nDo you want to add special characters? (y/n): ")

if special_char_confirm.lower() == "y":
    special_char_size = int(input("Enter the count of special characters: "))
    if special_char_size > 0:
        password_length += special_char_size
    else:
        print("\nSpecial character size cannot be zero.")

if password_length == 0:
    print("\nYou entered 'no' to every question. The password cannot be empty.")
else:
    password = ""

    for _ in range(letter_size):
        password += choice(letters)

    for _ in range(num_size):
        password += choice(numbers)

    for _ in range(special_char_size):
        password += choice(special_chars)

    password_list = list(password)
    shuffle(password_list)

    password = ""
    
    for i in password_list:
        password += i

    print("\nGenerated Password: " + password)
