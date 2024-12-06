def main():
    while True:
        f=input('Fraction:')
        try:
            f1=convert(f)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(f1))


def convert(fraction):
        l=fraction.split('/')
        percentage=(int(l[0])/int(l[1]))*100
        if int(l[0])>int(l[1]) or l[0].isdigit() is False or l[1].isdigit() is False:
            raise ValueError
        elif int(l[1])==0:
            raise ZeroDivisionError
        else:
            return round(percentage)


def gauge(percentage):
    if percentage>=99:
        return 'F'
    elif percentage<=1:
        return 'E'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
