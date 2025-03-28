import time
import sys
from colorama import Fore, Style, init

def loading_dots():
    print("Loading", end="")
    for _ in range(5):
        time.sleep(0.5)  # Delay
        print(".", end="", flush=True)
    print("\nDone!")

loading_dots()

print(Fore.RED + r"""

-----------------------

/  __ \   | |        | |
| /  \/ __| | ___  __| |
| |    / _` |/ _ \/ _` |
| \__/\ (_| |  __/ (_| |
 \____/\__,_|\___|\__,_|

-----------------------
MY DISCORD IS CMOSS23 
 
""")

choice = input("1 For PayloadMaker: ")

if choice == '1':
	print("Wait...")
