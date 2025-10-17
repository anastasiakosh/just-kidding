import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

star = [
    "    *    ",
    "   ***   ",
    "  *****  ",
    " ******* ",
    "*********",
    " ******* ",
    "  *****  ",
    "   ***   ",
    "    *    "
]

def print_star():
    for _ in range(10):  
        for line in star:
            colored_line = "".join(
                random.choice(colors) + ch + Style.RESET_ALL if ch == "*" else " "
                for ch in line
            )
            print(colored_line)
        time.sleep(0.3)
        print("\033[H\033[J", end="")  # очистка экрана

if __name__ == "__main__":
    print("✨ Blinking star is starting...")
    print_star()
    print("⭐ Done! Merry Coding! 🎄")
