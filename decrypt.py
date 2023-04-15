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
print("\n", processing, "\n")
def countdown(n):
    if(n==0):
        print ("\n\33[45m\033[3mThank you for your patience\033[0m" + "\33[45m\033[3m!\033[0m\n")
    else: 
        print(n)
        countdown(n-1)
countdown(5)
print("." * 94)

# a, e, i, o, u assigned to *, &, #, +, ! respectively using Tuple
tuple_char = ("*", "&", "#", "+", "!")
decrypted_input = ""
# Checking
  # If *, change to "a"
for i in range (len(user_input)):
    if user_input[i] == tuple_char[0]:
        decrypted_input += "a"

  # If &, change to "e"
    elif user_input[i] == tuple_char[1]:
        decrypted_input += "e"
  # If #, change to "i"
    elif user_input[i] == tuple_char[2]:
        decrypted_input += "i"
  # If +, change to "o"
    elif user_input[i] == tuple_char[3]:
        decrypted_input += "o"
  # If !, change to "u"
    elif user_input[i] == tuple_char[4]:
        decrypted_input += "u"
    else:
        decrypted_input += user_input[i]
# Print the decrypted input
present_decryption = Figlet(font = "standard")
print(colored(present_decryption.renderText("Here it is.."), "red"))
print("\033[43m\033[1mThe encrypted code you entered a while a go is: \033[0m", decrypted_input, '\n\n')

# Program closing
closing_mess = Figlet(font = "digital")
print("\033[44m=\033[0m" * 94)
print(colored(closing_mess.renderText("\nThank you for availing our services !"), "green"))
print("\033[107mHope to see you again...\033[0m\n")
print("\033[44m=\033[0m" * 94)