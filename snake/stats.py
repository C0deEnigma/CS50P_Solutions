import csv
sum=0
cnt=0
with open ('marks.csv') as f:
    a=csv.reader()
    for l in a:
        sum+=l[2]
        if l[2]>=36:
            cnt+=1
print(sum/1403, cnt)
