import sys
import time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
    time.sleep(1.5)

def capitalize_first_word(words: str) -> str:
    return words[0].upper() + words[1:]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def green(text: str):
    print(f"{bcolors.OKGREEN}{text}{bcolors.ENDC}")

def red(text: str):
    print(f"{bcolors.FAIL}{text}{bcolors.ENDC}")