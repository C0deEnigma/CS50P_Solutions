while True:
    try:
        f1=input('Fraction:')
        f=f1.split('/')
        x=int(f[0])
        y=int(f[1])
        p1=((x/y)*100)
        p=int(round(p1,0))
        if x>y:
            continue
        if p>=99:
            print('F')
        elif p<=1:
            print('E')
        else:
            print(str(p)+'%')
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break
