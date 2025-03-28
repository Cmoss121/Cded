import time
import sys
from colorama import Fore, Style, init

# Initialize colorama to reset colors automatically
init(autoreset=True)

def loading_dots():
    """Red loading animation"""
    print(Fore.RED + "Loading", end="", flush=True)
    for _ in range(5):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\nDone!" + Style.RESET_ALL)

# Run the loading animation
loading_dots()

# Print ASCII Art in red
print(Fore.RED + r"""

-----------------------

/  __ \   | |        | |
| /  \/ __| | ___  __| |
| |    / _` |/ _ \/ _` |
| \__/\ (_| |  __/ (_| |
 \____/\__,_|\___|\__,_|

-----------------------
MY DISCORD IS CMOSS23 
 
""" + Style.RESET_ALL)  # Reset color after ASCII art

# Get user choice
choice = input(Fore.RED + "Enter 1 for PayloadMaker: " + Style.RESET_ALL)

if choice == '1':
    print(Fore.RED + "Wait..." + Style.RESET_ALL)
    time.sleep(2)  # Simulate processing time
    print(Fore.RED + "PayloadMaker is launching..." + Style.RESET_ALL)
