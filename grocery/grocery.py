s=[]
while True:
    try:
        g=input()
        s.append(g)
    except EOFError:
        break
s.sort()
for i in range(len(s)):
    flag=0
    for j in range(i):
        if s[j]==s[i]:
            flag=1
    if flag==1:
        pass
    else:
        print(s.count(s[i]),s[i].upper())
