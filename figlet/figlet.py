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
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            figlet.setFont(font=sys.argv[2])
        except Exception:
            sys.exit("Invalid usage")
        s = input("Input: ")
        print(figlet.renderText(s))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")