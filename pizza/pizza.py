import sys
import csv
import tabulate
if len(sys.argv)>2:
    sys.exit('Too many command-line arguments')
if len(sys.argv)<2:
    sys.exit('Too few command-line arguments')
if sys.argv[1].split('.')[-1]!='csv':
    sys.exit('Not a CSV file')
try:
    l=[]
    with open (sys.argv[1]) as f:
        reader=csv.reader(f)
        for row in reader:
            l.append(row)
        print(tabulate.tabulate(l[1:], headers=l[0], tablefmt='grid'))
except FileNotFoundError:
    sys.exit('File does not exist')
