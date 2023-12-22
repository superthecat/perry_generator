from colorama import init
from colorama import Fore, Back, Style

name = input ("nickname: ")
print(Back.CYAN,Fore.BLACK)
input("welcome to the Doofenshmirtz meme generator ")
print(Back.RESET,Fore.RESET,Fore.RED)
print("press capslock to enter")
print(Fore.RESET)

late = input ("enter the a what make Doofenshmirtz: ")

print(f"YOU LATE {name} THE PLATYPUS I MAKE A {late}!")
print(Fore.GREEN)
print(Fore.RESET,Fore.CYAN)
input (f"press enter to finish {name} ")