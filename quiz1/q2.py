import numpy as np
c=[]
for i in range(1,9):
    for j in range(1,9):
        c.append([i,j])
l=[]
for i in range(10):
    rx1=[]
    ry1=[]
    rx2=[]
    ry2=[]
    ux=np.random.randint(1,9)
    uy=np.random.randint(1,9)
    vx=np.random.randint(1,9)
    vy=np.random.randint(1,9)
    rx1.append(ux)
    ry1.append(uy)
    rx2.append(vx)
    ry2.append(vy)
    u=[ux,uy]
    v=[vx,vy]
    cnt=0
    while True:
        u=([u[0]-1,u[1]-1],[u[0]-1,u[1]],[u[0]-1,u[1]+1],[u[0],u[1]-1],[u[0],u[1]+1],[u[0]+1,u[1]-1],[u[0]+1,u[1]],[u[0]+1,u[1]+1])[np.random.randint(0,8)]
        while True:
            if u not in c:
                u=([u[0]-1,u[1]-1],[u[0]-1,u[1]],[u[0]-1,u[1]+1],[u[0],u[1]-1],[u[0],u[1]+1],[u[0]+1,u[1]-1],[u[0]+1,u[1]],[u[0]+1,u[1]+1])[np.random.randint(0,8)]
            else:
                break
        v=([v[0]-1,v[1]-1],[v[0]-1,v[1]],[v[0]-1,v[1]+1],[v[0],v[1]-1],[v[0],v[1]+1],[v[0]+1,v[1]-1],[v[0]+1,v[1]],[v[0]+1,v[1]+1])[np.random.randint(0,8)]
        while True:
            if v not in c:
                v=([v[0]-1,v[1]-1],[v[0]-1,v[1]],[v[0]-1,v[1]+1],[v[0],v[1]-1],[v[0],v[1]+1],[v[0]+1,v[1]-1],[v[0]+1,v[1]],[v[0]+1,v[1]+1])[np.random.randint(0,8)]
            else:
                break
        rx1.append(u[0])
        ry1.append(u[1])
        rx2.append(v[0])
        ry2.append(v[1])
        cnt+=1
        if u==v:
            l.append(cnt)
            break
print(sum(l)/10)
