from colorama import Fore, Style
from config import BANNER, AI_NAME, USER_NAME


def print_computer(text: str):
    print(Fore.GREEN + Style.BRIGHT + "[" + AI_NAME + "] " + text)


def print_human(text: str):
    print(Fore.WHITE + Style.DIM + "[" + USER_NAME + "] " + text)


def print_banner():
    print(Fore.GREEN + BANNER)