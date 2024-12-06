import sys
import csv
if len(sys.argv)>3:
    sys.exit('Too many command-line arguments')
if len(sys.argv)<3:
    sys.exit('Too few command-line arguments')
try:
    with open(sys.argv[1]) as file:
        data=csv.DictReader(file)
        l=[]
        for row in data:
            last=row['name'].split(', ')[0]
            first=row['name'].split(', ')[1]
            house=row['house']
            l.append({'first':first, 'last':last, 'house':house})

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')
with open(sys.argv[2],'w') as f:
    writer=csv.DictWriter(f, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    writer.writerows(l)
