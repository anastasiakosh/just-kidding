import time

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
    for line in star:
        print(line)
        time.sleep(0.2)

if __name__=="__main__":
   print("✨ Drawing a star in the console...")
   print_star()
   print("\n⭐ Done!")
