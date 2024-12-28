import pyfiglet
from random import choice
from sys import exit, argv


fig = pyfiglet.Figlet()
if len(argv) == 3:
    if argv[1] in ["-f", "--font"] and argv[2] in fig.getFonts():
        fig.setFont(font=argv[2])
    else:
        exit("Invalid usage")
elif len(argv) == 1:
    fig.setFont(font=choice(fig.getFonts()))
else:
    exit("Invalid usage")

text = input("Input: ")
print("Output:\n" + fig.renderText(text))

