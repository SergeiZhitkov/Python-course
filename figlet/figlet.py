import sys
import random
from pyfiglet import Figlet



figlet = Figlet()
s = input("Input: ")
if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or "--font":
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
else:
    sys.exit()