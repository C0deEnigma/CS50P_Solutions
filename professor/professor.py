import random

def main():
    score=0
    level=get_level()
    for _ in range (10):
        x,y = generate_integer(level), generate_integer(level)
        for i in range(3):
            print(f'{x} + {y} = ',end='')
            z=int(input(''))
            if z==x+y:
                score+=1
                break
            else:
                print('EEE')
        if z!=x+y:
            print(f'{x} + {y} = {x+y}')
    print(f'Score: {score}')

def get_level():
    level=-1
    while level not in [1,2,3]:
        try:
            level=int(input('Level: '))
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
