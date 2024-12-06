with open('f.txt','r') as f1:
    s=[]
    e=[]
    data=f1.readlines()
    for line in data:
        s.append(int(line.split()[0]))
        e.append(int(line.strip('\n').split()[1]))
print(s,e)
