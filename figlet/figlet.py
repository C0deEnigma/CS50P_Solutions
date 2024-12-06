import sys
import pyfiglet as pyg
import random
if len(sys.argv) not in [1,3]:
    sys.exit('Invalid usage')
else:
    if len(sys.argv) == 3:
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit('Invalid usage')
        elif sys.argv[2] not in pyg.FigletFont.getFonts():
            sys.exit('Invalid usage')
        else:
            s=input('Input: ')
            print(pyg.figlet_format(s, sys.argv[2]))
    if len(sys.argv) == 1:
        s=input('Input: ')
        print(pyg.figlet_format(s, random.choice(pyg.FigletFont.getFonts())))
