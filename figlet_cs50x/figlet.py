from sys import argv, exit
from cs50 import get_string
from pyfiglet import Figlet

figlet = Figlet()
fronts = figlet.getFonts()


lenght = len(argv)
if lenght == 3:
    if argv[1] not in ["-f", "--font"] or argv[2] not in fronts:
        print("Invalid usage")
        exit(1)
    figlet.setFont(font=argv[2])
if lenght not in [1, 3]:
    print("Invalid usage")
    exit(1)
text = get_string("Input: ")
print(figlet.renderText(text))
