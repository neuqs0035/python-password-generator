from random import choice
from random import shuffle

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
specialchars = "~!@#$%^&*"

print("\t\t\tRandom Password Generator\n")

total_pass_size = 0

char_confirm = input("Do You Wanna Add Characters ? ( y / n ) : ")

if char_confirm.lower() == "y":

    char_size = int(input("\nEnter The Count Of Characters : "))

    if char_size > 0:
        
        total_pass_size += char_size
    
    elif char_size == 0:

        print("\nChar Size Cannot Be Zero")

    else:

        print("\nChar Size Cannot Be Zero")


elif char_confirm.lower() == "n":

    print("\nChar Addition Cancled")


num_confirm = input("Do You Wanna Add Numbers ? ( y / n ) : ")

if char_confirm.lower() == "y":

    num_size = int(input("\nEnter The Count Of Characters : "))

    if num_size > 0:
        
        total_pass_size += num_size
    
    elif num_size == 0:

        print("\nChar Size Cannot Be Zero")

    else:

        print("\nChar Size Cannot Be Zero")

    
elif num_confirm.lower() == "n":

    print("\nChar Addition Cancled")
