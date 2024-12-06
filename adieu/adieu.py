import inflect
print('Adieu, adieu, to', end=' ')
l=[]
while True:
    try:
        n=input()
    except EOFError:
        break
    l.append(n)
p=inflect.engine()
print(p.join(l))
