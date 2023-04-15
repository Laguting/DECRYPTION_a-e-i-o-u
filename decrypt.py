# Laguting, Maricon Jane G. 
# BSCpE 1-4
# Task: Decrypt an encrypted text entered by the user
# Welcome the user
from pyfiglet import Figlet
from termcolor import colored
welcome_usr = Figlet(font = "banner3-D")
print("=" * 94)
print(colored(welcome_usr.renderText(" Welcome!"), "yellow"))
print("=" * 94)

# Ask an input from the user
# Process the input
# a, e, i, o, u assigned to *, &, #, +, ! respectively using Tuple
# Checking
  # If *, change to "a"
  # If &, change to "e"
  # If #, change to "i"
  # If +, change to "o"
  # If !, change to "u"
# Print the decrypted input
# Program closing