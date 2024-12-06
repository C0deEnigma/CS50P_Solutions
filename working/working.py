import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'([0-9]{1,2})(:[0-9]{2})? (AM|PM) to ([0-9]{1,2})(:[0-9]{2})? (AM|PM)',s):
        try:
            if match.group(2) == None:
                M1=0
            else:
                M1=int(match.group(2).lstrip(':'))
            if match.group(5) == None:
                M2=0
            else:
                M2=int(match.group(5).lstrip(':'))
            H1=int(match.group(1))
            T1=match.group(3)
            H2=int(match.group(4))
            T2=match.group(6)
        except ValueError:
            raise ValueError
        if M1>=60 or M2>=60:
            raise ValueError
        if T1 == 'PM':
            H1=H1+12
        if T2 == 'PM':
            if H2==12:
                pass
            else:
                H2=H2+12
        if H1==12 and T1=='AM':
            H1=0
        if H2==12 and T2=='AM':
            H2=0
        return f'{H1:02d}:{M1:02d} to {H2:02d}:{M2:02d}'
    else:
        raise ValueError

if __name__ == "__main__":
    main()
