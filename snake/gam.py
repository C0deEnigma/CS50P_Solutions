# Returns a dictionary with initial posn as key and final posn as value.
from numpy import random
def readsnakes():
    f=open('snake.txt')
    data=f.readlines()
    D={}
    for i in data:
        D[int(i.split()[2])]=int(i.split()[1])
    f.close()
    return D

def readladders():
    f=open('ladder.txt')
    data=f.readlines()
    D={}
    for i in data:
        D[int(i.split()[1])]=int(i.split()[2])
    f.close()
    return D

def snakebite(a,i):
    snakes=readsnakes()
    print(f'Player{i} got bitten by a snake comes to {snakes[a]} from {a}')
    a=snakes[a]
    return a

def ladderjump(a,i):
    ladders=readladders()
    print(f'Player{i} catches a ladder goes to {ladders[a]} from {a}')
    a=ladders[a]
    return a


def rolldice(a,i):
    total=0
    while True:
        p=random.randint(1,7)
        if a==-1:
            if p==6:
                print(f'Player{i} got 6 gets another chance')
                a=0
            else:
                print(f'Player{i} got {p} still not on board')
                return 0
        else:
            if p==6:
                print(f'Player{i} got 6 gets another chance')
                total+=6
            else:
                total+=p
                print(f'Player{i} got {p} moves from {a} to {a+total}')
                return total
n=int(input('Enter No of Players: '))
D=[-1]*n
def main():
    j=1
    while True:
        print(f'Roll{j}:')
        for i in range(n):
            p=rolldice(D[i],i+1)
            D[i]+=p
            if D[i] in readsnakes().keys():
                snakebite(D[i],i+1)
            if D[i] in readladders().keys():
                ladderjump(D[i],i+1)
            if D[i]==100:
                return f'Player{i+1} won the game'
            if D[i]>100:
                D[i]=D[i]-p
        j+=1
print(main())
