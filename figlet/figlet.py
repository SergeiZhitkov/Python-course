import sys
import random
from pyfiglet import Figlet



figlet = Figlet()
if len(sys.argv) == 1:
    s = input("Input: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    s = input("Input: ")
    if sys.argv[1] == "-f" or "--font":
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
else:
    sys.exit()