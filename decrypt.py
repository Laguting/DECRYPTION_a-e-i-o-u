# Laguting, Maricon Jane G. 
# BSCpE 1-4
# Task: Decrypt an encrypted text entered by the user
# Welcome the user
from pyfiglet import Figlet
from termcolor import colored
welcome_usr = Figlet(font = "banner3-D")
print("\033[35m=\033[0m" * 94)
print(colored(welcome_usr.renderText(" Welcome! "), "yellow"))
print("\033[35m=\033[0m" * 94)

# Ask an input from the user
greetings_usr = Figlet(font = "bubble")
print(colored(greetings_usr.renderText("Hi, User!"), "blue"))
user_input = input("\033[46m\033[27mPlease enter any encrypted code you have in mind:\033[0m ")
print("*" * 94)
# Process the input
processing = "\033[33m\033[1mPlease wait, we're currently processing the encrypted code you entered.\033[0m"
print("\n\n", processing, "\n\n")
def countdown(n):
    if(n==0):
        print ("\n\33[45m\033[3mThank you for your patience\033[0m" + "\33[45m\033[3m!\033[0m\n")
    else: 
        print(n)
        countdown(n-1)
countdown(5)
print("." * 94)

# a, e, i, o, u assigned to *, &, #, +, ! respectively using Tuple
# Checking
  # If *, change to "a"
  # If &, change to "e"
  # If #, change to "i"
  # If +, change to "o"
  # If !, change to "u"
# Print the decrypted input
# Program closing