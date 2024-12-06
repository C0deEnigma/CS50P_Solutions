import random
while True:
    try:
        n=int(input('Level: '))
        r=random.randint(1,n)
    except ValueError:
        pass
    except:
        if n<1:
            pass
    else:
        break
while True:
    try:
        g=int(input('Guess: '))
    except ValueError:
        pass
    else:
        if g>r:
            print('Too large!')
        elif g<r:
            print('Too small!')
        else:
            print('Just right!')
            break
